# pitch_score — composite scoring

Pattern: [Composite scoring](https://docs.typesafe.ai/patterns/composite-scoring)

Do not ask Jev to "rate this startup pitch." Ask market, feasibility, and differentiation as separate Scores, plus a stage Choice and a traction Noul. Weights live in code so you change a coefficient instead of a prompt.

```bash
python -m jev_master pitch --state examples/pitch.txt
python -m jev_master.apps.pitch_score --state examples/pitch.txt
```
