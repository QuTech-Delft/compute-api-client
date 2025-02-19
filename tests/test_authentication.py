import time
from typing import Any
from unittest.mock import MagicMock

import pytest
import responses
from responses import matchers

from qi2_shared.authentication import AuthorisationError, IdentityProvider, OauthDeviceSession
from qi2_shared.settings import ApiSettings, AuthSettings, TokenInfo


@pytest.fixture
def identity_provider_mock() -> MagicMock:
    return MagicMock(spec=IdentityProvider)


@pytest.fixture
def api_settings_mock(auth_settings: AuthSettings) -> MagicMock:
    api_settings = MagicMock(spec=ApiSettings)
    api_settings.default_host = "https://host.com"
    api_settings.auths = {api_settings.default_host: auth_settings}
    return api_settings


def test_oauth_device_session_refresh_no_token(api_settings_mock: MagicMock, identity_provider_mock: MagicMock) -> None:
    # Arrange
    api_settings_mock.auths[api_settings_mock.default_host].tokens = None
    session = OauthDeviceSession("https://host.com", api_settings_mock, identity_provider_mock)

    # Act & Assert
    with pytest.raises(AuthorisationError):
        session.refresh()


def test_oauth_device_session_refresh_token_not_expired(
    api_settings_mock: MagicMock, identity_provider_mock: MagicMock
) -> None:
    # Arrange
    auth_settings = api_settings_mock.auths[api_settings_mock.default_host]
    auth_settings.tokens.generated_at = time.time()

    # Act
    token_info = OauthDeviceSession("https://host.com", api_settings_mock, identity_provider_mock).refresh()

    # Assert
    assert token_info == auth_settings.tokens

    identity_provider_mock.refresh_access_token.assert_not_called()


def test_oauth_device_session_refresh_token_expired(
    api_settings_mock: MagicMock, identity_provider_mock: MagicMock
) -> None:
    # Arrange
    session = OauthDeviceSession("https://host.com", api_settings_mock, identity_provider_mock)
    new_token_info: dict[str, Any] = {
        "access_token": "new_access_token",
        "expires_in": 100,
        "refresh_token": "new_refresh_token",
        "refresh_expires_in": 1000,
        "generated_at": time.time(),
    }

    identity_provider_mock.refresh_access_token.return_value = new_token_info

    # Act
    token_info = session.refresh()

    # Assert
    assert token_info == TokenInfo(**new_token_info)

    identity_provider_mock.refresh_access_token.assert_called_once_with("client_id", "refresh_token")
    api_settings_mock.store_tokens.assert_called_once_with("https://host.com", token_info)


@responses.activate
def test_identity_provider_refresh_access_token() -> None:
    # Arrange
    token_info = {"token": "something", "some": "other_data"}
    client_id = "some_client"
    old_refresh_token = "old_token"

    responses.get(
        "https://host.com/well-known-endpoint",
        json={
            "token_endpoint": "https://host.com/token-endpoint",
            "device_authorization_endpoint": "https://host.com/device-endpoint",
        },
    )
    responses.post(
        "https://host.com/token-endpoint",
        json=token_info,
        match=[
            matchers.urlencoded_params_matcher(
                {"grant_type": "refresh_token", "client_id": client_id, "refresh_token": old_refresh_token}
            )
        ],
    )

    # Act
    token = IdentityProvider("https://host.com/well-known-endpoint").refresh_access_token(client_id, old_refresh_token)

    # Assert
    assert token == token_info
