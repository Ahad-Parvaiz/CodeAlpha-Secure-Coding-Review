import sqlite3
import bcrypt

# Connect to the SQLite database (it will create it if not exists)
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Create users table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
)
''')

# Insert a test user
username = 'admin'
plain_password = 'password123'
hashed_password = bcrypt.hashpw(plain_password.encode('utf-8'), bcrypt.gensalt()).decode()

cursor.execute('INSERT OR IGNORE INTO users (username, password) VALUES (?, ?)', (username, hashed_password))

# Save and close
conn.commit()
conn.close()

print("✅ Database and user created.")
