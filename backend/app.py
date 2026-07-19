from flask import Flask, jsonify, request

from backend.config import Config
from backend.models import PRIORITIES, STATUSES, Ticket, db


def create_app(config_object=Config):
    app = Flask(__name__)
    app.config.from_object(config_object)
    db.init_app(app)

    with app.app_context():
        db.create_all()

    register_routes(app)
    return app


def register_routes(app):
    @app.get("/api/health")
    def health():
        return jsonify(status="ok")

    @app.get("/api/tickets")
    def list_tickets():
        query = Ticket.query
        for field in ("status", "priority", "assignee"):
            value = request.args.get(field)
            if value:
                query = query.filter_by(**{field: value})
        tickets = query.order_by(Ticket.created_at.desc()).all()
        return jsonify([t.to_dict() for t in tickets])

    @app.get("/api/tickets/<int:ticket_id>")
    def get_ticket(ticket_id):
        ticket = db.session.get(Ticket, ticket_id)
        if ticket is None:
            return jsonify(error="ticket not found"), 404
        return jsonify(ticket.to_dict())

    @app.post("/api/tickets")
    def create_ticket():
        data = request.get_json(silent=True) or {}
        title = data.get("title")
        description = data.get("description")
        priority = data.get("priority", "medium")

        if not title or not description:
            return jsonify(error="title and description are required"), 400
        if priority not in PRIORITIES:
            return jsonify(error=f"priority must be one of {PRIORITIES}"), 400

        ticket = Ticket(title=title, description=description, priority=priority)
        db.session.add(ticket)
        db.session.commit()
        return jsonify(ticket.to_dict()), 201

    @app.put("/api/tickets/<int:ticket_id>")
    def update_ticket(ticket_id):
        ticket = db.session.get(Ticket, ticket_id)
        if ticket is None:
            return jsonify(error="ticket not found"), 404

        data = request.get_json(silent=True) or {}

        if "status" in data:
            if data["status"] not in STATUSES:
                return jsonify(error=f"status must be one of {STATUSES}"), 400
            ticket.status = data["status"]
        if "priority" in data:
            if data["priority"] not in PRIORITIES:
                return jsonify(error=f"priority must be one of {PRIORITIES}"), 400
            ticket.priority = data["priority"]
        if "assignee" in data:
            ticket.assignee = data["assignee"]
        if "title" in data:
            ticket.title = data["title"]
        if "description" in data:
            ticket.description = data["description"]

        db.session.commit()
        return jsonify(ticket.to_dict())

    @app.delete("/api/tickets/<int:ticket_id>")
    def delete_ticket(ticket_id):
        ticket = db.session.get(Ticket, ticket_id)
        if ticket is None:
            return jsonify(error="ticket not found"), 404
        db.session.delete(ticket)
        db.session.commit()
        return "", 204


if __name__ == "__main__":
    create_app().run(debug=True)
