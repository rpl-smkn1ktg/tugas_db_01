import mysql.connector
import os
import sys

def run_test():
    # 1. Koneksi ke MySQL Server
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
        print(f"❌ Gagal terhubung ke Database: {e}")
        sys.exit(1)

    # 2. Baca file TUGAS_JOIN.sql milik siswa
    file_path = "TUGAS_JOIN.sql"
    if not os.path.exists(file_path):
        print(f"❌ File {file_path} tidak ditemukan!")
        sys.exit(1)

    with open(file_path, "r") as f:
        sql_script = f.read()

    # 3. Eksekusi seluruh statement DDL, DML, dan DQL siswa
    commands = [cmd.strip() for cmd in sql_script.split(";") if cmd.strip()]
    select_results = []

    for command in commands:
        # Abaikan komentar murni
        if command.startswith("/*") or command.startswith("--"):
            continue
        try:
            cursor.execute(command)
            if cursor.description:  # Jika perintah menghasilkan data (SELECT)
                select_results.append(cursor.fetchall())
            db.commit()
        except Exception as e:
            print(f"❌ Error saat mengeksekusi query:\n{command}\n--> Pesan Error: {e}")
            sys.exit(1)

    # 4. Validasi Hasil Query JOIN
    if len(select_results) < 2:
        print("❌ Kurang query SELECT! Pastikan ada query INNER JOIN dan LEFT JOIN.")
        sys.exit(1)

    # Output Ekspektasi
    expected_inner = [
        ('1001', 'almer', 'X RPL'),
        ('1002', 'adila', 'XI RPL'),
        ('1003', 'farel', 'X RPL')
    ]

    expected_left = [
        ('1001', 'almer', 'X RPL'),
        ('1003', 'farel', 'X RPL'),
        ('1002', 'adila', 'XI RPL'),
        (None, None, 'XII RPL')
    ]

    inner_result = select_results[0]
    left_result = select_results[1]

    # Cek INNER JOIN
    success = True
    if sorted(inner_result) == sorted(expected_inner):
        print("✅ SOAL 5 (INNER JOIN): BENAR")
    else:
        print(f"❌ SOAL 5 (INNER JOIN): SALAH\n   Hasil Siswa: {inner_result}\n   Ekspektasi  : {expected_inner}")
        success = False

    # Cek LEFT JOIN
    # Mengurutkan berdasarkan nama kelas / NISN untuk validasi fleksibel
    if len(left_result) == 4 and any(row[2] == 'XII RPL' and row[0] is None for row in left_result):
        print("✅ SOAL 6 (LEFT JOIN): BENAR")
    else:
        print(f"❌ SOAL 6 (LEFT JOIN): SALAH\n   Hasil Siswa: {left_result}\n   Ekspektasi  : Harus menampilkan kelas 'XII RPL' dengan murid NULL")
        success = False

    if not success:
        sys.exit(1)

    print("\n🎉 SELAMAT! Semua query SQL berhasil diuji dan bernilai 100.")

if __name__ == "__main__":
    run_test()
