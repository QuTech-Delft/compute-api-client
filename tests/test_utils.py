import asyncio

from qi2_shared.utils import run_async


def test_async_run_no_loop() -> None:
    async def t_coro() -> None:
        await asyncio.sleep(1)

    run_async(t_coro())


def test_async_run_loop() -> None:
    async def t_coro() -> None:
        await asyncio.sleep(1)

    async def main() -> None:
        run_async(t_coro())

    asyncio.run(main())
