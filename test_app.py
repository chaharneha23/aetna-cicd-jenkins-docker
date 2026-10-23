from app import app

def test_home_page():
    response = app.test_client().get("/")
    assert response.status_code == 200
    assert response.json["project"] == "Aetna CI/CD Pipeline"

def test_health_endpoint():
    response = app.test_client().get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "healthy"
