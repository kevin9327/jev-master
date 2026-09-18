# JevBot

Not a chatbot. Jev returns intent / severity / needs_human; code picks a canned template (`reply` / `escalate` / `block`).

Standalone GitHub repo: https://github.com/kevin9327/jev-bot

```bash
python -m jev_master bot --state examples/stripe-ticket.txt
python -m jev_master.apps.jev_bot --state examples/stripe-ticket.txt
```
