import pytest
from rest_framework.test import APIClient
from rest_framework import status
from unittest.mock import patch


@pytest.fixture
def client():
    return APIClient()


@patch("api.views.WordService")
def test_get_not_allowed(MockWordService, client):
    response = client.get("/api/validate-word/")
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED


@patch("api.views.WordService")
def test_validate_word_post(MockWordService, client):
    # Mock the get_word_for_today method to return a specific word
    MockWordService.return_value.get_word_for_today.return_value = "apple"

    # Test a valid word
    response = client.post("/api/validate-word/", {"word": "apple"})
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 5
    for letter_status in response.data:
        assert letter_status["status"] == "correct"


@patch("api.views.WordService")
def test_validate_short_word(MockWordService, client):
    MockWordService.return_value.get_word_for_today.return_value = "apple"

    # Test a word shorter than 5 letters
    response = client.post("/api/validate-word/", {"word": "app"})
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@patch("api.views.WordService")
def test_validate_long_word(MockWordService, client):
    MockWordService.return_value.get_word_for_today.return_value = "apple"

    # Test a word longer than 5 letters
    response = client.post("/api/validate-word/", {"word": "bananas"})
    assert response.status_code == status.HTTP_400_BAD_REQUEST
