import mysql.connector

# Replace 'your_password_here' with your correct password
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sowmya@123",
    dat abase="music_analytics"  # You can create this DB if not already created
)

cursor = conn.cursor()

# Confirm connection
print("✅ Connected to MySQL!")

# Optional: Check existing databases
cursor.execute("SHOW DATABASES;")
for db in cursor.fetchall():
    print("📁", db[0])

conn.close()
