# Build Plan: Basic Helpdesk Ticketing System

## Project Goal
Build a simple, working end-to-end helpdesk ticketing web application. Users can submit support tickets; agents can view, assign, update, and resolve them. This is a portfolio project intended to demonstrate CI/CD pipelines, REST API design, database modeling, and full-stack integration.

## Tech Stack
- **Backend:** Python + Flask
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy (Flask-SQLAlchemy)
- **Frontend:** HTML, CSS, JavaScript (vanilla — no frontend framework)
- **API style:** RESTful JSON endpoints
- **Environment/config:** `.env` file for DB credentials (never commit secrets)

## Core Entities

### Ticket
| Field | Type | Notes |
|---|---|---|
| id | integer, PK | auto-increment |
| title | string | required |
| description | text | required |
| priority | enum | low / medium / high |
| status | enum | open / in_progress / resolved |
| assignee | string, nullable | agent name/id |
| created_at | timestamp | auto-set on creation |
| updated_at | timestamp | auto-updated on change |

### Comment (optional, stretch goal)
| Field | Type | Notes |
|---|---|---|
| id | integer, PK | |
| ticket_id | integer, FK | references Ticket |
| body | text | |
| created_at | timestamp | |

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | /api/tickets | List all tickets (support query params: status, priority, assignee) |
| GET | /api/tickets/:id | Get a single ticket by id |
| POST | /api/tickets | Create a new ticket |
| PUT | /api/tickets/:id | Update a ticket (status, assignee, priority) |
| DELETE | /api/tickets/:id | Delete a ticket |
| POST | /api/tickets/:id/comments | Add a comment to a ticket (stretch goal) |

## Frontend Pages
1. **Ticket list / dashboard** — table of all tickets, filterable by status and priority, shows counts (open/in-progress/resolved)
2. **Create ticket form** — title, description, priority
3. **Ticket detail view** — full ticket info, status dropdown, assignee field, comment thread (stretch goal)

## Build Order (suggested phases)

1. **Setup**
   - Initialize Flask app, connect to PostgreSQL, set up SQLAlchemy models
   - Set up `.env` for DB config, add `.gitignore`
2. **Backend core**
   - Implement Ticket model and migrations
   - Implement all REST endpoints (list, create, get, update, delete)
   - Add basic input validation (required fields, valid enum values)
3. **Frontend core**
   - Build ticket list page that calls GET /api/tickets and renders a table
   - Build create-ticket form that calls POST /api/tickets
   - Build ticket detail page with status/assignee update calling PUT /api/tickets/:id
4. **Polish**
   - Add filtering/search on the list page
   - Add simple styling (clean, minimal CSS)
   - Add dashboard summary counts
5. **Stretch goals**
   - Comments on tickets
   - Basic auth (login for agents)
   - Email notification stub on status change
   - GitHub Actions CI (lint + run tests on push)

## Non-Goals (out of scope for v1)
- User authentication / roles
- Multi-tenant support
- File attachments on tickets

## Deliverables
- Working local app (backend + frontend)
- Clean git history with meaningful commits
- CI/CD pipeline
- Production deployment / hosting
