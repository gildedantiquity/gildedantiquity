---
title: "Tool Use & Function Calling untuk Otomasi Nyata"
date: 2026-07-26T09:00:00+07:00
draft: false
theme: Teknik
readingTime: 8
lede: Tanpa tools, agen hanya bercerita tentang pekerjaan. Dengan function calling yang rapi, agen mulai mengerjakan pekerjaan itu—di dalam pagar yang Anda tentukan.
---

## Ide intinya sederhana

Model memilih nama fungsi dan argumen terstruktur. Runtime Anda yang mengeksekusi. Hasil eksekusi dikembalikan ke model sebagai observasi berikutnya. Model tidak “langsung menyentuh” produksi; ia mengajukan niat, sistem yang memutuskan boleh tidaknya.

## Kontrak tool yang baik

- **Nama jelas** — `create_draft_pr` lebih baik daripada `do_stuff`.
- **Schema ketat** — tipe, enum, required fields, contoh valid.
- **Deskripsi jujur** — kapan dipakai, kapan tidak, efek sampingnya apa.
- **Output stabil** — JSON konsisten agar loop berikutnya tidak bingung.

## Pola izin berlapis

Kelompokkan tools menurut risiko:

- **Read** — query, fetch issue, baca docs. Default boleh.
- **Write draft** — buat draft email/PR. Boleh dengan logging.
- **Mutate** — merge, bayar, hapus. Wajib human-in-the-loop.

Jangan berikan satu “supertool” yang bisa melakukan apa saja. Semakin sempit permukaan aksi, semakin mudah diaudit.

## Kesalahan klasik

- Model mengarang argumen yang tidak ada di schema.
- Tool gagal diam-diam tanpa error message yang berguna.
- Tidak ada idempotency: retry membuat duplikat side effect.
- Secrets ikut masuk ke prompt atau log.

## Checklist sebelum production

- Allowlist tools per agent role.
- Timeout + retry dengan backoff untuk pemanggilan jaringan.
- Redaksi credential di semua log.
- Tes skenario: happy path, tool error, dan argumen invalid.

Tulis ulang satu otomasi Anda sebagai daftar tools + schema—bukan sebagai “prompt panjang yang magis”.
