/*
====================================================================
TUGAS PRAKTIKUM BASIS DATA: INNER JOIN & LEFT JOIN
Mata Pelajaran : Basis Data / Software Engineering
File           : TUGAS_JOIN.sql
====================================================================

SKENARIO KASUS:
Sebagai seorang Database Administrator sekolah, Anda diminta untuk 
merancang basis data sederhana untuk pengelolaan data kelas dan murid,
mengisi data awal, serta membuat laporan gabungan menggunakan JOIN.

PETUNJUK SISWA:
1. Kerjakan semua instruksi SQL di bawah ini.
2. Tuliskan query SQL Anda persis di bawah baris perintah soal masing-masing.
3. Setelah selesai, lakukan COMMIT dan PUSH file ini ke GitHub.
====================================================================
*/

-- =================================================================
-- SOAL 1: MEMBUAT TABEL KELAS
-- =================================================================
-- Buatlah tabel bernama 'kelas' dengan ketentuan:
-- - kd_kls : Karakter maksimal 10, sebagai PRIMARY KEY
-- - nm_kls : Karakter maksimal 25

-- Tulis Query Soal 1 di bawah ini:




-- =================================================================
-- SOAL 2: INPUT DATA TABEL KELAS
-- =================================================================
-- Masukkan data berikut ke dalam tabel 'kelas':
-- 1. kd_kls: K001 | nm_kls: X RPL
-- 2. kd_kls: K002 | nm_kls: XI RPL
-- 3. kd_kls: K003 | nm_kls: XII RPL

-- Tulis Query Soal 2 di bawah ini:




-- =================================================================
-- SOAL 3: MEMBUAT TABEL MURID
-- =================================================================
-- Buatlah tabel bernama 'murid' dengan ketentuan:
-- - nisn   : Karakter maksimal 10, sebagai PRIMARY KEY
-- - nama   : Karakter maksimal 50
-- - kd_kls : Karakter maksimal 10, sebagai FOREIGN KEY merujuk ke 'kelas(kd_kls)'

-- Tulis Query Soal 3 di bawah ini:




-- =================================================================
-- SOAL 4: INPUT DATA TABEL MURID
-- =================================================================
-- Masukkan data berikut ke dalam tabel 'murid':
-- 1. nisn: 1001 | nama: almer | kd_kls: K001
-- 2. nisn: 1002 | nama: adila | kd_kls: K002
-- 3. nisn: 1003 | nama: farel | kd_kls: K001

-- Tulis Query Soal 4 di bawah ini:




-- =================================================================
-- SOAL 5: IMPLEMENTASI INNER JOIN
-- =================================================================
-- Tampilkan kolom: nisn, nama (dari tabel murid), dan nm_kls (dari tabel kelas)
-- Menggunakan perintah INNER JOIN.

-- Tulis Query Soal 5 di bawah ini:




-- =================================================================
-- SOAL 6: IMPLEMENTASI LEFT JOIN
-- =================================================================
-- Tampilkan kolom: nisn, nama (dari tabel murid), dan nm_kls (dari tabel kelas)
-- Menggunakan perintah LEFT JOIN dengan posisi tabel 'kelas' di sebelah kiri.

-- Tulis Query Soal 6 di bawah ini:




/* 
====================================================================
END OF FILE
====================================================================
*/
