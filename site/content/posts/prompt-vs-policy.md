---
title: "Prompt vs Policy: Menulis Instruksi yang Bisa Dieksekusi"
date: 2026-07-27T08:00:00+07:00
draft: false
theme: Teknik
readingTime: 5
lede: "Prompt adalah niat; policy adalah kontrak yang bisa diaudit."
generated_by: "scripts/generate_daily_posts.py"
---
## Batas prompt

Prompt saja tidak cukup untuk produksi.

- Non-deterministik
- Sulit diuji
- Mudah di-bypass

## Isi policy

Tulis aturan yang bisa dicek mesin.

- Tools boleh/tidak
- Escalation
- Format keluaran

## Uji policy

Perlakukan seperti kode.

- Fixture skenario
- Regression suite
- Versioning

## Penutup

Ringkasnya: Dari prompt longgar ke kebijakan operasional yang jelas dan teruji. Jadikan ini satu eksperimen kecil hari ini, ukur hasilnya, lalu baru skala.
