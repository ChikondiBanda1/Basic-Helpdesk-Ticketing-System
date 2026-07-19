const API_BASE = "/api/tickets";

const ticketList = document.getElementById("ticket-list");
const ticketForm = document.getElementById("ticket-form");

async function loadTickets() {
  const response = await fetch(API_BASE);
  const tickets = await response.json();
  renderTickets(tickets);
}

function renderTickets(tickets) {
  ticketList.innerHTML = "";
  for (const ticket of tickets) {
    const row = document.createElement("tr");
    row.innerHTML = `
      <td>${ticket.id}</td>
      <td>${ticket.title}</td>
      <td>${ticket.priority}</td>
      <td>${ticket.status}</td>
      <td>${ticket.assignee ?? ""}</td>
    `;
    ticketList.appendChild(row);
  }
}

ticketForm.addEventListener("submit", async (event) => {
  event.preventDefault();
  const formData = new FormData(ticketForm);

  await fetch(API_BASE, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      title: formData.get("title"),
      description: formData.get("description"),
      priority: formData.get("priority"),
    }),
  });

  ticketForm.reset();
  loadTickets();
});

loadTickets();
