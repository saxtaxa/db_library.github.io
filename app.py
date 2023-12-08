import mysql.connector

def create_table(cursor, table_name):
    # Function to create a table with the specified name
    try:
        cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
                harga INT,
                penulis VARCHAR(100),
                ISBN VARCHAR(20) PRIMARY KEY,
                tahun INT,
                judul VARCHAR(100)
            )
        """)
        print(f"Table '{table_name}' created successfully.")
    except mysql.connector.Error as e:
        print(f"Error creating table: {e}")

def edit_table_name(cursor, old_table_name, new_table_name):
    try:
        # Check if the old table exists before attempting to rename
        if not check_table(cursor, old_table_name):
            print(f"Table '{old_table_name}' does not exist.")
            return

        # Execute the table name change using a parameterized query
        update_query = "ALTER TABLE {} RENAME TO {}".format(old_table_name, new_table_name)
        cursor.execute(update_query)
        print(f"Table name '{old_table_name}' changed to '{new_table_name}' successfully.")
        connection.commit()  # Commit the changes
    except mysql.connector.Error as e:
        print(f"Error editing table name: {e}")


def insert_data(cursor, table_name):
    try:
        # Get column names
        cursor.execute(f"DESCRIBE {table_name}")
        columns = [column[0] for column in cursor.fetchall()]

        # Inform the user about the order of columns
        print(f"Columns in the '{table_name}' table: {', '.join(columns[0:])}")

        # Prepare the INSERT INTO statement with column names
        columns_str = ', '.join(columns[0:])  # Exclude the first column (usually an auto-increment ID)
        placeholders = ', '.join(['%s' for _ in columns[0:]])
        insert_query = f"INSERT INTO {table_name} ({columns_str}) VALUES ({placeholders})"

        # Gather data from the user
        data = []
        for column in columns[0:]:
            value = input(f"Enter {column}: ")
            data.append(value)

        # Execute the INSERT INTO statement with user-inputted data
        cursor.execute(insert_query, tuple(data))

        print(f"Data inserted into the '{table_name}' table successfully.")
        connection.commit()  # Commit the transaction after inserting data
    except mysql.connector.Error as e:
        print(f"Error inserting data: {e}")

def edit_data(cursor, table_name, isbn, new_title):
    # Function to edit data in the specified table
    try:
        update_query = f"UPDATE {table_name} SET judul = %s WHERE ISBN = %s"
        cursor.execute(update_query, (new_title, isbn))
        print(f"Data in the '{table_name}' table edited successfully.")
        connection.commit()  # Commit the changes
    except mysql.connector.Error as e:
        print(f"Error editing data: {e}")


def check_table(cursor, table_name):
    # Function to check if the table exists and display all tables
    try:
        cursor.execute("SHOW TABLES")
        all_tables = [table[0] for table in cursor.fetchall()]
        
        if table_name in all_tables:
            print(f"Table '{table_name}' exists.")
            return True
        else:
            print(f"Table '{table_name}' does not exist.")
            return False
    except mysql.connector.Error as e:
        print(f"Error checking table existence: {e}")
        return False

def drop_table(cursor, table_name):
    # Function to drop the specified table
    try:
        cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
        print(f"Table '{table_name}' dropped successfully.")
    except mysql.connector.Error as e:
        print(f"Error dropping table: {e}")

def retrieve_all_data(cursor, table_name):
    # Function to retrieve all data from the specified table
    try:
        cursor.execute(f"SELECT * FROM {table_name}")
        return cursor.fetchall()
    except mysql.connector.Error as e:
        print(f"Error retrieving all data: {e}")
        return []

def retrieve_data_by_rank(cursor, table_name, rank):
    # Function to retrieve data from the specified table by rank
    try:
        cursor.execute(f"SELECT * FROM {table_name} ORDER BY harga DESC LIMIT {int(rank)}")
        return cursor.fetchall()
    except mysql.connector.Error as e:
        print(f"Error retrieving data by rank: {e}")
        return []

# Main code
host = 'localhost'
user = 'root'
password = '@Santamena1'
database = 'perpustakaan'
table_name = 'book'

try:
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    if connection.is_connected():
        print("Connected to MySQL database")

        cursor = connection.cursor()

        while True:
            print("\nChoose an operation:")
            print("1. Create Table")
            print("2. Edit Table Name")
            print("3. Insert Data")
            print("4. Edit Data")
            print("5. Check Table Existence")
            print("6. Drop Table")
            print("7. Retrieve All Data")
            print("8. Retrieve Data by Rank")
            print("0. Exit")

            choice = input("Enter your choice (0-8): ")

            if choice == '1':
                new_table_name = input("Enter the new table name: ")
                create_table(cursor, new_table_name)
            elif choice == '2':
                old_table_name = table_name
                new_table_name = input("Enter the new table name: ")
                edit_table_name(cursor, old_table_name, new_table_name)
                table_name = new_table_name
            elif choice == '3':
                insert_data(cursor, table_name)
            elif choice == '4':
                isbn = input("Enter the ISBN to edit data: ")
                new_title = input("Enter the new title: ")
                edit_data(cursor, table_name, isbn, new_title)
            elif choice == '5':
                if check_table(cursor, table_name):
                    print(f"Table '{table_name}' exists.")
                else:
                    print(f"Table '{table_name}' does not exist.")
            elif choice == '6':
                drop_table(cursor, table_name)
            elif choice == '7':
                all_data = retrieve_all_data(cursor, table_name)
                print(f"\nAll Data from '{table_name}' Table:")
                for row in all_data:
                    print(row)
            elif choice == '8':
                rank = input("Enter the rank: ")
                rank_data = retrieve_data_by_rank(cursor, table_name, rank)
                print(f"\nData from '{table_name}' Table with Rank '{rank}':")
                for row in rank_data:
                    print(row)
            elif choice == '0':
                break
            else:
                print("Invalid choice. Please enter a number between 0 and 8.")

except mysql.connector.Error as e:
    print(f"Error: {e}")
finally:
    # Close the cursor and connection in the 'finally' block to ensure they are always closed
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("MySQL connection closed")