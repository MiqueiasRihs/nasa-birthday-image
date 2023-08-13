from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200

def test_get_image():
    response = client.get("/nasa-image?date=2023-08-01")
    assert response.status_code == 200
