import sqlite3
from hashlib import file_digest

import bcrypt


def create_db(name: str) -> int:
    connection = sqlite3.connect(name)
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS users (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   username TEXT UNIQUE,
                   password TEXT,
                   records TEXT,
                   mush_count TEXT
                   )""")

    connection.commit()
    connection.close()

    return 0


def add_data(data: str, database: file_digest, username: str) -> int:
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE username = ?",
        (username,),
    )
    old_records = cursor.fetchone()[3]
    new_records = old_records + "," + data

    cursor.execute(
        "UPDATE users SET records = ? WHERE username = ?",
        (new_records, username),
    )

    connection.commit()
    connection.close()

    return 0


def sign_in(username: str, password: str, database: file_digest) -> int:
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    password = password.encode("utf-8")

    hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())

    cursor.execute(
        "INSERT INTO users (username, password, records, mush_count) VALUES (?, ?, '', '0')",
        (username, hashed_password),
    )

    connection.commit()
    connection.close()

    return 0


def log_in(username: str, password: str, database: file_digest) -> bool:
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))

    password = password.encode("utf-8")
    existing_password = cursor.fetchone()

    if existing_password == None:
        connection.commit()
        connection.close()
        return False
    if bcrypt.checkpw(password, existing_password[2]):
        connection.commit()
        connection.close()
        return True
    else:
        connection.commit()
        connection.close()
        return False


def delete_table(database: file_digest) -> None:
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    cursor.execute("DROP TABLE if EXISTS users")

    connection.commit()
    connection.close()


def print_datas(database: file_digest) -> None:
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM users")

    for c in cursor:
        print(c)

    connection.commit()
    connection.close()


def sort_datas(database: file_digest) -> int:
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    users = cursor.execute("SELECT * FROM users").fetchall()

    for user in users:
        sorted_data = (user[3]).split(",")
        sorted_data = [int(r) for r in sorted_data if r]
        sorted_data.sort()
        data = ",".join([str(r) for r in sorted_data])
        cursor.execute(
            "UPDATE users set records = ? WHERE username = ?", (data, user[1])
        )

    connection.commit()
    connection.close()

    return 0


def modify_db(data: str, database: file_digest, username: str) -> None:
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    cursor.execute("UPDATE users set records = ? WHERE username = ?", (data, username))

    connection.commit()
    connection.close()


def global_ten(database: file_digest) -> None:
    sort_datas(database)

    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    users = cursor.execute("SELECT * FROM USERS").fetchall()

    times = []
    top_ten = []
    worst_time = -1

    for _, _, _, record, _ in users:
        records = record.split(",")
        best_time = list(int(r) for r in records if r)
        if len(best_time) > 0:
            best_time.sort()
            if len(times) < 10:
                times.append(best_time[0])
                times.sort()
                worst_time = times[-1]
            else:
                if best_time[0] < worst_time:
                    times.sort()
                    times.pop()
                    times.append(best_time[0])
                    times.sort()
                    worst_time = times[-1]

    times.sort()

    for time in times:
        for _, username, _, record, mush_count in users:
            records = record.split(",")
            best_time = list(int(r) for r in records if r)
            if len(best_time) > 0:
                if best_time[0] == time:
                    top_ten.append((username, best_time[0], mush_count))
                    break

    connection.commit()
    connection.close()

    return top_ten[:10]


def top_ten_times(username: str, database: file_digest) -> list:
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    records = cursor.execute(
        "SELECT * FROM users WHERE username = ?",
        (username,),
    ).fetchall()

    records = (list(c for r in records for c in r)[3]).split(",")
    records = [int(r) for r in records if r]
    records.sort()

    connection.commit()
    connection.close()

    return records[:10]


def is_new(username: str, database: file_digest) -> bool:
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    records = cursor.execute(
        "SELECT * FROM users WHERE username = ?",
        (username,),
    ).fetchall()

    return len(records) == 0


def delete_account(username: str, database: str) -> None:
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    cursor.execute("DELETE FROM users WHERE username = ?", (username,))

    connection.commit()
    connection.close()
