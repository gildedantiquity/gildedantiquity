---
title: "Observability: Melacak Jejak Keputusan Agen"
date: 2026-07-28T08:00:00+07:00
draft: false
theme: Operasional
readingTime: 5
lede: "Kalau tidak bisa menjelaskan kenapa agen bertindak, Anda tidak bisa memperbaikinya."
generated_by: "scripts/generate_daily_posts.py"
---
## Apa yang di-log

Jejak yang cukup untuk replay.

- Plan steps
- Tool args/results
- Policy decisions

## Privacy & redaksi

Observability jangan jadi kebocoran.

- Mask secret
- PII policy
- Retention

## Replay

Ulangi kegagalan dengan input yang sama.

- Deterministic harness
- Fixture tools
- Diff output

## Penutup

Ringkasnya: Logging, traces, dan replay untuk debug perilaku non-deterministik. Jadikan ini satu eksperimen kecil hari ini, ukur hasilnya, lalu baru skala.
