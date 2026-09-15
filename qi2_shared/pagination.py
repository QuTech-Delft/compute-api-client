from collections.abc import Awaitable, Callable
from typing import Annotated, Any, Generic, TypeVar, cast

from pydantic import BaseModel, Field

PageType = TypeVar("PageType")
ItemType = TypeVar("ItemType")


class PageInterface(BaseModel, Generic[ItemType]):
    """The page models in the generated API client don't inherit from a common base class, so we have to trick the
    typing system a bit with this fake base class."""

    items: list[ItemType]
    total: Annotated[int, Field(strict=True, ge=0)] | None
    page: Annotated[int, Field(strict=True, ge=1)] | None
    size: Annotated[int, Field(strict=True, ge=1)] | None
    pages: Annotated[int, Field(strict=True, ge=0)] | None = None


class PageReader(Generic[PageType, ItemType]):
    """Helper class for reading fastapi-pagination style pages returned by the compute_api_client."""

    async def get_all(self, api_call: Callable[..., Awaitable[PageType]], **kwargs: Any) -> list[ItemType]:
        """Get all items from an API call that supports paging."""
        items: list[ItemType] = []
        page = 1

        while True:
            response = cast(PageInterface[ItemType], await api_call(page=page, **kwargs))

            items.extend(response.items)
            page += 1
            if response.pages is None or page > response.pages:
                break
        return items

    async def get_single(self, api_call: Callable[..., Awaitable[PageType]], **kwargs: Any) -> ItemType | None:
        """Get a single item from an API call that supports paging."""
        response = cast(PageInterface[ItemType], await api_call(**kwargs))
        if len(response.items) > 1:
            raise RuntimeError(f"Response contains more than one item -> {kwargs}.")

        return response.items[0] if response.items else None
