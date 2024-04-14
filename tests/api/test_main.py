from fastapi.testclient import TestClient

from main import app  # Import the main application


def test_app_returns_hello_world():
    """
    This tests verifies that the application returns a basic response.
    """
    with TestClient(app) as client:
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"message": "Hello, world!"}  # Replace with expected response
