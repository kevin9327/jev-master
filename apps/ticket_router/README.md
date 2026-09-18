# ticket_router — intent routing

Pattern: [Intent routing](https://docs.typesafe.ai/patterns/intent-routing)

One `POST /v1/systemone` with **Choice** (department) + **Score** (frustration) + **Noul** (is_urgent). Code composes `department` + `escalate`/`act` + a handler queue. No generated prose is parsed.

```bash
python -m jev_master ticket --state examples/stripe-ticket.txt
python -m jev_master.apps.ticket_router --state examples/stripe-ticket.txt
```
