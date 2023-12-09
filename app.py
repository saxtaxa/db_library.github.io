import mysql.connector

# Fungsi untuk menguji koneksi ke database
def test_db_connection():
    try:
        # Gantilah parameter sesuai dengan konfigurasi database Anda
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='@Santamena1',
            database='perpustakaan'
        )

        # Jika koneksi berhasil, cetak pesan "connected"
        print("Connected to the database")

        # Jangan lupa untuk menutup koneksi setelah selesai
        connection.close()

    except mysql.connector.Error as e:
        # Jika terjadi kesalahan, cetak pesan "not connected" dan detail kesalahan
        print(f"Not connected to the database. Error: {e}")

# Fungsi untuk membuat tabel
def create_table(create_table_query):
    try:
        # Gantilah parameter sesuai dengan konfigurasi database Anda
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='@Santamena1',
            database='perpustakaan'
        )

        # Membuat objek cursor
        cursor = connection.cursor()

        # Menjalankan query untuk membuat tabel
        cursor.execute(create_table_query)

        # Commit perubahan ke database
        connection.commit()

        # Menutup kursor dan koneksi
        cursor.close()
        connection.close()

        print("Table created successfully")

    except mysql.connector.Error as e:
        print(f"Error creating table. {e}")

# Fungsi untuk menghapus tabel
def drop_table():
    try:
        # Gantilah parameter sesuai dengan konfigurasi database Anda
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='@Santamena1',
            database='perpustakaan'
        )

        # Membuat objek cursor
        cursor = connection.cursor()

        # Query untuk menghapus tabel
        drop_table_query = "DROP TABLE IF EXISTS books"

        # Menjalankan query
        cursor.execute(drop_table_query)

        # Commit perubahan ke database
        connection.commit()

        # Menutup kursor dan koneksi
        cursor.close()
        connection.close()

        print("Table dropped successfully")

    except mysql.connector.Error as e:
        print(f"Error dropping table. {e}")

# Fungsi untuk mengedit nama tabel
def rename_table(old_table_name, new_table_name):
    try:
        # Gantilah parameter sesuai dengan konfigurasi database Anda
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='@Santamena1',
            database='perpustakaan'
        )

        # Membuat objek cursor
        cursor = connection.cursor()

        # Query untuk mengedit nama tabel
        rename_table_query = f"ALTER TABLE {old_table_name} RENAME TO {new_table_name}"

        # Menjalankan query
        cursor.execute(rename_table_query)

        # Commit perubahan ke database
        connection.commit()

        # Menutup kursor dan koneksi
        cursor.close()
        connection.close()

        print(f"Table renamed from {old_table_name} to {new_table_name} successfully")

    except mysql.connector.Error as e:
        print(f"Error renaming table. {e}")

# Fungsi main untuk menampilkan menu dan memanggil fungsi-fungsi
def main():
    while True:
        print("\nMenu:")
        print("1. Test Database Connection")
        print("2. Create Table")
        print("3. Drop Table")
        print("4. Rename Table")
        print("0. Exit")

        choice = input("Enter your choice (0-4): ")

        if choice == "1":
            test_db_connection()
        elif choice == "2":
            custom_create_table_query = input("Enter your CREATE TABLE query: ")
            create_table(custom_create_table_query)
        elif choice == "3":
            drop_table()
        elif choice == "4":
            old_table_name = input("Enter the old table name: ")
            new_table_name = input("Enter the new table name: ")
            rename_table(old_table_name, new_table_name)
        elif choice == "0":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 0 and 4.")

if __name__ == "__main__":
    main()
