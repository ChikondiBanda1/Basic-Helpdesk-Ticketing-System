# Project Plan: Basic Helpdesk Ticketing System

## Project Goal
Build a simple, working end-to-end helpdesk ticketing web application. Users can submit support tickets; agents can view, assign, update, and resolve them. This is a portfolio project intended to demonstrate CI/CD pipelines, REST API design, database modeling, and full-stack integration.

## Stakeholders
- **Customers** — end users of a SaaS company who need to file complaints, ask for help, or ask questions.
- **Support officers** — the company's internal support staff who work on the tickets: giving status updates, resolving issues, and escalating where needed.

## Use Cases
**As a customer, I want to:**
- File a complaint
- Ask for help
- Ask a question

**As a support officer, I want to:**
- Record status updates on a ticket
- Give the customer updates
- Resolve issues
- Escalate an issue to another layer/tier of support when I can't resolve it myself

## Business Components
|Component | Used by | Purpose |
|---|---|---|
|Ticket submission | Customer | Where a customer files a complaint, help request, or question |
|Ticket status view | Customer	| Where a customer checks progress on their open tickets |
|Ticket update / resolution | Support officer | Where an officer changes status, adds notes, and resolves a ticket |
|Support ↔ client chat | Both | Live conversation thread attached to each ticket |

## Other core features
- Ticket CRUD (submit/view/update/resolve)
- Instant messaging via WebSockets
- Ticket categories/tags — e.g. billing, technical, account 
- Email notifications — customer gets emailed on status change or new reply
- Customer satisfaction rating — quick thumbs-up/down after resolution

## Pages / Views (by role)
**Customer-facing:**
- Submit a ticket (title, description, priority)
- My tickets — list + status
- Ticket detail — status + live chat with support

**Support-officer-facing:**
- Ticket queue — all open/assigned tickets, filterable by status/priority
- Ticket detail — status/priority controls, resolve button, live chat with customer

## Tech Stack
- **Backend:** Python + Flask
- **Real-time messaging:** Flask-SocketIO
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy (Flask-SQLAlchemy)
- **Frontend:** HTML, CSS, JavaScript (vanilla — no frontend framework)
- **API style:** RESTful JSON endpoints

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
- Multi-tenant support (multiple SaaS companies on one instance)
- File attachments on tickets/messages
- Escalation tiers / ticket reassignment between officers
- Typing indicators, read receipts, or other chat-app polish

## Deliverables
- Working local app (backend + frontend)
- Clean git history with meaningful commits
- CI/CD pipeline
- Production deployment / hosting
