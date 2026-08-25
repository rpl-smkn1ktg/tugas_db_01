import mysql.connector
import os
import sys

def run_test():
    total_score = 0
    max_score = 100

    print("==================================================")
    print("      AUTOMATED SQL GRADER - REPORT CARD          ")
    print("==================================================\n")

    # 1. Koneksi Database
    try:
        db = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="rootpassword",
            database="db_sekolah",
            port=3306
        )
        cursor = db.cursor()
    except Exception as e:
        print(f"❌ Critical Error: Gagal koneksi database ({e})")
        sys.exit(1)

    # 2. Baca file TUGAS_JOIN.sql
    file_path = "TUGAS_JOIN.sql"
    if not os.path.exists(file_path):
        print(f"❌ Critical Error: File {file_path} tidak ditemukan!")
        sys.exit(1)

    with open(file_path, "r") as f:
        sql_script = f.read()

    commands = [cmd.strip() for cmd in sql_script.split(";") if cmd.strip()]

    # Execute all queries
    select_results = []
    for command in commands:
        if command.startswith("/*") or command.startswith("--"):
            continue
        try:
            cursor.execute(command)
            if cursor.description:
                select_results.append(cursor.fetchall())
            db.commit()
        except Exception as e:
            pass

    # --- SOAL 1: Cek Tabel kelas (10 Poin) ---
    try:
        cursor.execute("DESCRIBE kelas;")
        cols = {row[0]: row[1].decode() if isinstance(row[1], bytes) else row[1] for row in cursor.fetchall()}
        if 'kd_kls' in cols and 'nm_kls' in cols:
            print("✅ Soal 1: Tabel 'kelas' berhasil dibuat (+10 Poin)")
            total_score += 10
        else:
            print("❌ Soal 1: Kolom tabel 'kelas' tidak sesuai (0/10 Poin)")
    except Exception:
        print("❌ Soal 1: Tabel 'kelas' belum dibuat (0/10 Poin)")

    # --- SOAL 2: Cek Data kelas (10 Poin) ---
    try:
        cursor.execute("SELECT * FROM kelas ORDER BY kd_kls;")
        kelas_data = cursor.fetchall()
        expected_kelas = [('K001', 'X RPL'), ('K002', 'XI RPL'), ('K003', 'XII RPL')]
        if kelas_data == expected_kelas:
            print("✅ Soal 2: Data tabel 'kelas' sesuai (+10 Poin)")
            total_score += 10
        else:
            print("❌ Soal 2: Data tabel 'kelas' tidak pas/kurang (0/10 Poin)")
    except Exception:
        print("❌ Soal 2: Gagal mengecek data tabel 'kelas' (0/10 Poin)")

    # --- SOAL 3: Cek Tabel murid & FK (15 Poin) ---
    try:
        cursor.execute("DESCRIBE murid;")
        cols = {row[0]: row[1].decode() if isinstance(row[1], bytes) else row[1] for row in cursor.fetchall()}
        
        # Cek ketersediaan foreign key
        cursor.execute("""
            SELECT CONSTRAINT_NAME 
            FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE 
            WHERE TABLE_NAME = 'murid' AND REFERENCED_TABLE_NAME = 'kelas';
        """)
        fk_exists = cursor.fetchall()

        if 'nisn' in cols and 'nama' in cols and 'kd_kls' in cols and len(fk_exists) > 0:
            print("✅ Soal 3: Tabel 'murid' dan Foreign Key berhasil dibuat (+15 Poin)")
            total_score += 15
        else:
            print("❌ Soal 3: Struktur tabel 'murid' / Foreign Key belum tepat (0/15 Poin)")
    except Exception:
        print("❌ Soal 3: Tabel 'murid' belum dibuat (0/15 Poin)")

    # --- SOAL 4: Cek Data murid (10 Poin) ---
    try:
        cursor.execute("SELECT nisn, nama, kd_kls FROM murid ORDER BY nisn;")
        murid_data = cursor.fetchall()
        expected_murid = [('1001', 'almer', 'K001'), ('1002', 'adila', 'K002'), ('1003', 'farel', 'K001')]
        if murid_data == expected_murid:
            print("✅ Soal 4: Data tabel 'murid' sesuai (+10 Poin)")
            total_score += 10
        else:
            print("❌ Soal 4: Data tabel 'murid' tidak pas/kurang (0/10 Poin)")
    except Exception:
        print("❌ Soal 4: Gagal mengecek data tabel 'murid' (0/10 Poin)")

    # Ekspektasi JOIN
    expected_inner = [('1001', 'almer', 'X RPL'), ('1002', 'adila', 'XI RPL'), ('1003', 'farel', 'X RPL')]

    # --- SOAL 5: Cek INNER JOIN (25 Poin) ---
    inner_correct = False
    for res in select_results:
        if len(res) == 3 and sorted(res) == sorted(expected_inner):
            inner_correct = True
            break
    
    if inner_correct:
        print("✅ Soal 5: Query INNER JOIN tepat (+25 Poin)")
        total_score += 25
    else:
        print("❌ Soal 5: Perintah/Output INNER JOIN salah (0/25 Poin)")

    # --- SOAL 6: Cek LEFT JOIN (30 Poin) ---
    left_correct = False
    for res in select_results:
        if len(res) == 4 and any(row[2] == 'XII RPL' and row[0] is None for row in res):
            left_correct = True
            break

    if left_correct:
        print("✅ Soal 6: Query LEFT JOIN tepat (+30 Poin)")
        total_score += 30
    else:
        print("❌ Soal 6: Perintah/Output LEFT JOIN salah (0/30 Poin)")

    print("\n--------------------------------------------------")
    print(f"📊 TOTAL SKOR AKHIR: {total_score} / {max_score}")
    print("--------------------------------------------------")

    if total_score == max_score:
        print("🎉 EXCELLENT! Tugas diselesaikan dengan sempurna.\n")
        sys.exit(0)
    else:
        print("⚠️ Masih ada tugas yang belum sesuai. Silakan perbaiki lalu PUSH kembali.\n")
        sys.exit(1)

if __name__ == "__main__":
    run_test()
