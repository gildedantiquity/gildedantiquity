---
title: "Perceive–Plan–Act: Anatomi Satu Loop Agen"
date: 2026-07-27T08:00:00+07:00
draft: false
theme: Fondasi
readingTime: 7
lede: Hampir semua sistem agentic yang berguna bisa digambar ulang sebagai loop tiga tahap. Memahami loop ini lebih penting daripada mengejar framework terbaru.
---

## 1. Perceive — baca dunia apa adanya

Agen mengumpulkan sinyal: pesan user, state ticket, isi file, hasil query, atau screenshot UI. Perceive yang buruk menghasilkan rencana yang anggun tapi salah sasaran.

- Normalisasi input (hapus noise, standarisasi format).
- Ambil hanya fakta yang relevan untuk goal saat ini.
- Catat ketidakpastian: “data X belum tersedia” lebih baik daripada mengarang.

## 2. Plan — pecah goal jadi langkah

Perencanaan mengubah goal kabur menjadi urutan aksi yang bisa dicek. Rencana bagus biasanya pendek, punya kriteria selesai, dan menyebut tools yang akan dipakai.

Contoh skeleton rencana:

- Ambil issue #142 dari GitHub.
- Ringkas reproduksi bug dari komentar.
- Cari file terkait di repo.
- Usulkan patch + checklist tes.
- Berhenti dan minta approval sebelum push.

## 3. Act — eksekusi dengan kontrak jelas

Aksi adalah pemanggilan tool: HTTP request, query SQL read-only, jalankan tes, atau buka halaman. Setiap tool harus punya skema input/output dan batas izin.

Setelah aksi, hasilnya kembali ke tahap Perceive. Loop berlanjut sampai goal tercapai, budget habis, atau human approval dibutuhkan.

## Stop conditions yang wajib ada

- Maksimal N iterasi per tugas.
- Budget token / biaya maksimum.
- Daftar aksi berbahaya yang selalu butuh konfirmasi manusia.
- Timeout wall-clock agar loop tidak hidup selamanya.

## Latihan 15 menit

Ambil satu workflow harian Anda (misalnya ringkas email inbound). Tuliskan secara eksplisit: apa yang di-perceive, bagaimana rencana default, tools apa yang boleh dipanggil, dan kapan harus berhenti. Itu fondasi desain agen yang jauh lebih berguna daripada demo “auto-GPT”.
