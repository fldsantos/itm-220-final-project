# Path to the SQLite database file
DB_PATH = "database.sqlite"

# Table name to interact with
TABLE_NAME = "member"

# Columns to manage (excluding ID)
COLUMNS = {
    "first_name": "TEXT",
    "last_name": "TEXT",
    "email": "TEXT",
    "phone": "TEXT",
    "points": "INTEGER",
    "join_date": "DATE"
}