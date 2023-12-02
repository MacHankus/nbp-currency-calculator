import pytest

from shared.exceptions.server_failed_request_error import ServerFailedRequestError
from tests.helpers.random import get_random_string


def test_should_raise_server_unavailable_error():
    with pytest.raises(expected_exception=ServerFailedRequestError):
        raise ServerFailedRequestError()


def test_should_have_default_message():
    # Arrange
    # Act
    error = ServerFailedRequestError()

    # Assert

    assert str(error) == ServerFailedRequestError._MESSAGE


def test_should_have_provided_message():
    # Arrange
    message = get_random_string()

    # Act
    error = ServerFailedRequestError(message)

    # Assert

    assert str(error) == message
