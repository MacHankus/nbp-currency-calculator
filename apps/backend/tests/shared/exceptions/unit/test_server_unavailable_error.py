import pytest

from shared.exceptions.server_unavailable_error import ServerUnavailableError
from tests.helpers.random import get_random_string


def test_should_raise_server_unavailable_error():
    with pytest.raises(expected_exception=ServerUnavailableError):
        raise ServerUnavailableError()


def test_should_have_default_message():
    # Arrange
    # Act
    error = ServerUnavailableError()

    # Assert

    assert str(error) == ServerUnavailableError._MESSAGE


def test_should_have_provided_message():
    # Arrange
    message = get_random_string()

    # Act
    error = ServerUnavailableError(message)

    # Assert

    assert str(error) == message
