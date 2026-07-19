import pytest

from backend import create_app
from backend.config import TestConfig
from backend.models import db


@pytest.fixture()
def client():
    app = create_app(TestConfig)
    with app.test_client() as client:
        yield client
    with app.app_context():
        db.drop_all()


def test_health(client):
    resp = client.get("/api/health")
    assert resp.status_code == 200
    assert resp.get_json() == {"status": "ok"}


def test_create_and_list_ticket(client):
    resp = client.post(
        "/api/tickets",
        json={"title": "Printer broken", "description": "Won't turn on", "priority": "high"},
    )
    assert resp.status_code == 201
    ticket = resp.get_json()
    assert ticket["title"] == "Printer broken"
    assert ticket["status"] == "open"

    resp = client.get("/api/tickets")
    assert resp.status_code == 200
    assert len(resp.get_json()) == 1


def test_create_ticket_missing_fields(client):
    resp = client.post("/api/tickets", json={"title": "No description"})
    assert resp.status_code == 400


def test_create_ticket_invalid_priority(client):
    resp = client.post(
        "/api/tickets",
        json={"title": "Bad priority", "description": "x", "priority": "urgent"},
    )
    assert resp.status_code == 400


def test_update_ticket_status(client):
    create_resp = client.post(
        "/api/tickets",
        json={"title": "VPN issue", "description": "Can't connect"},
    )
    ticket_id = create_resp.get_json()["id"]

    resp = client.put(f"/api/tickets/{ticket_id}", json={"status": "in_progress"})
    assert resp.status_code == 200
    assert resp.get_json()["status"] == "in_progress"


def test_get_missing_ticket_returns_404(client):
    resp = client.get("/api/tickets/999")
    assert resp.status_code == 404


def test_delete_ticket(client):
    create_resp = client.post(
        "/api/tickets",
        json={"title": "Old ticket", "description": "Stale"},
    )
    ticket_id = create_resp.get_json()["id"]

    resp = client.delete(f"/api/tickets/{ticket_id}")
    assert resp.status_code == 204

    resp = client.get(f"/api/tickets/{ticket_id}")
    assert resp.status_code == 404
