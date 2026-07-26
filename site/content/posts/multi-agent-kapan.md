---
title: "Multi-Agent: Kapan Satu Agen Tidak Cukup"
date: 2026-07-27T08:00:00+07:00
draft: false
theme: Arsitektur
readingTime: 5
lede: "Tambah agen hanya jika pembagian peran menurunkan error, bukan ego arsitektur."
generated_by: "scripts/generate_daily_posts.py"
---
## Sinyal butuh multi-agen

Kompleksitas peran vs kompleksitas tugas.

- Konflik objective
- Butuh review independen
- Parallel research

## Pola orkestrasi

Mulai dari pola sederhana.

- Supervisor-worker
- Pipeline stages
- Debate terbatas

## Biaya koordinasi

Setiap hop antar-agen punya harga.

- Token overhead
- Latency
- Failure propagation

## Penutup

Ringkasnya: Pola orkestrasi researcher–executor–reviewer untuk tugas kompleks. Jadikan ini satu eksperimen kecil hari ini, ukur hasilnya, lalu baru skala.
