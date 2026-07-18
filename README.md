# Basic Helpdesk Ticketing System

A full-stack web application for creating, assigning, and tracking support tickets. Users can submit tickets with a title, description, and priority; agents can view, update status (open/in-progress/resolved), assign tickets to themselves, and leave comments. 

## Overview

This project simulates a simple internal helpdesk tool where end users can submit support tickets and agents can manage them through their full lifecycle — from creation to resolution. It was built as a hands-on exercise in designing REST APIs, structuring a client-server application, and implementing common support/ops workflows such as ticket triage, prioritization, and status tracking.

## Features

- **Ticket creation** — submit a ticket with a title, description, and priority level (low/medium/high)
- **Status tracking** — move tickets through open → in-progress → resolved states
- **Agent assignment** — assign tickets to specific agents for ownership and accountability
- **Search & filtering** — filter tickets by status, priority, or assignee
- **Comments** — add updates or notes to a ticket as it's being worked
- **Dashboard view** — see ticket volume and resolution status at a glance

## Tech Stack

- **Backend:**  Python + Flask
- **Database:** PostgreSQL
- **Frontend:** HTML, CSS, JavaScript
- **API:** RESTful endpoints for ticket CRUD operations

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /tickets | List all tickets |
| GET | /tickets/:id | Get a single ticket |
| POST | /tickets | Create a new ticket |
| PUT | /tickets/:id | Update a ticket (status, assignee, etc.) |
| DELETE | /tickets/:id | Delete a ticket |

## Project Structure

```
helpdesk-ticketing-system/
├── backend/
├── frontend/
├── README.md
└── ...
```

