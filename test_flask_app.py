import pytest
import json
from app import app

@pytest.fixture
def client():
    return app.test_client()

def test_ping(client):
    resp = client.get('/ping')
    assert resp.status_code == 200
    assert resp.json  == {"message":"Hi there, I am working"}


def test_predict(client):
    test_data = {
            "Gender":"Male",
            "Married":"Unmarried",
            "ApplicantIncome":50000,
            "Credit_History":"Cleared Debts",
            "LoanAmount":500000
        }
    resp = client.post("/predict",json=test_data)
    assert resp.status_code == 200
    assert resp.json == {'loan_approval_status':"Rejected"}