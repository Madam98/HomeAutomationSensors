sqlite_create_tables = {
    "users": """ CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                email TEXT NOT NULL,
                password TEXT NOT NULL); 
            """,

    "hum_temp":  """ CREATE TABLE IF NOT EXISTS humidity_temperature (
                    id INTEGER PRIMARY KEY,
                    date_time TEXT NOT NULL,
                    humidity REAL,
                    temperature REAL); 
                """
}

