import pytest
from fastapi.testclient import TestClient # type: ignore
from app.main import app

# Create a TestClient instance
client = TestClient(app)

def test_generate_text():
    """
    Test the /generate endpoint of the FastAPI app.
    """

    # Sample input data
    input_data = {"text": "Once upon a time"}

    # POST request to the /generate endpoint
    response = client.post("/generate/", json=input_data)

    # response status code is 200 (success)
    assert response.status_code == 200

    # response contains the expected content (model-generated text)
    response_json = response.json()
    assert "generated_text" in response_json
    assert len(response_json["generated_text"]) > 0  # Ensure some text is returned

def test_generate_missing_text():
    """
    Test the /generate endpoint when no text is provided in the request.
    """

    # POST request to the /generate endpoint without the text field
    response = client.post("/generate/", json={})

    # response status code is 422 (Unprocessable Entity)
    assert response.status_code == 422
