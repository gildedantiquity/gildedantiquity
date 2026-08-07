---
title: "Sandboxing Eksekusi Kode Agen"
date: 2026-08-07T08:00:00+07:00
draft: false
theme: Keamanan
readingTime: 5
lede: "Batas CPU, jaringan, dan filesystem untuk code tools."
generated_by: "scripts/generate_daily_posts.py"
---
## Mengapa ini penting

Dalam praktik Agentic AI Automation, tema Keamanan sering menjadi penentu apakah otomasi bisa dipercaya.

- Batas CPU, jaringan, dan filesystem untuk code tools.
- Fokus pada outcome yang bisa diukur, bukan demo yang semata impresif.
- Libatkan pemilik risiko sejak desain awal.

Tuliskan success metric sebelum menulis prompt pertama.

## Langkah penerapan

Kerangka kerja singkat yang bisa dicoba dalam satu cycle sprint.

- Petakan input, tools, dan side effects.
- Tambahkan guardrails dan stop conditions.
- Buat 5 skenario evaluasi (sukses, gagal tool, input adversial).
- Jalankan shadow mode sebelum cutover penuh.

## Checklist rilis

Jangan ship tanpa centang ini.

- Log/trace cukup untuk replay.
- Budget biaya terpasang.
- Jalur eskalasi ke manusia jelas.
- Rollback atau kill switch tersedia.

## Penutup

Ringkasnya: Batas CPU, jaringan, dan filesystem untuk code tools. Jadikan ini satu eksperimen kecil hari ini, ukur hasilnya, lalu baru skala.
