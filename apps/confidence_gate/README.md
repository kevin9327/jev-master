# confidence_gate — confidence-gated routing

Pattern: [Confidence-gated routing](https://docs.typesafe.ai/patterns/confidence-routing)

The Choice is *what*; `confidence` is *whether to act*. High-stakes `approve_transfer` needs a higher bar than `check_balance`. Code returns `act` / `confirm` / `escalate`.

```bash
python -m jev_master gate --state examples/voice-command.txt
python -m jev_master.apps.confidence_gate --state examples/voice-command.txt
```
