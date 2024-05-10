import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


#tester la creation d'un compte avec succes puis l'effacer apres le test
def test_create_account_success(cleanup):
    response = client.post("/auth/signup", json={"email": "test_adama@example.com", "password": "testpassword"})
    assert response.status_code == 201
    assert "message" in response.json()
    assert "id" in response.json()["message"]


# Tester si un compte existe déja
def test_create_account_conflict(cleanup):
    response = client.post("/auth/signup", json={"email": "adama@example.com", "password": "testpassword"})
    assert response.status_code == 409  # Conflict

#tester la connexion avec un user existant
def test_login(cleanup):
    response_create = client.post("/auth/signup", json={"email": "test_test@example.com", "password": "testpassword"})
    assert response_create.status_code == 201

    response_login = client.post("/auth/login", data={"username": "test_test@example.com", "password": "testpassword"})
    assert response_login.status_code == 200
    assert "access_token" in response_login.json()

#tester la connexion avec un user inexistant
def test_login_user_not_exists():
    response = client.post("/auth/login", data={"username": "utilisateur_inconnu@example.com", "password": "mot_de_passe_incorrect"})

    #code d'état est 401 (Non autorisé)
    assert response.status_code == 401
    assert "Invalid Credentials" in response.json()["detail"]
