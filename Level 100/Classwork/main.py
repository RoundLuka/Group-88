import sqlite3

connection = sqlite3.connect("Project.db")

cursor = connection.cursor()


# cursor.execute("""
#     create table users (
#         ID INTEGER PRIMARY KEY,
#         Name TEXT,
#         Email Text,
#         Balance INTEGER
#     )
# """)

# cursor.execute("""
#     INSERT INTO users (Name, Email, Balance)
#     VALUES ('Luka', 'example@gmail.com', 1000)
# """)  

# cursor.execute("""
#     INSERT INTO users (Name, Email, Balance)
#     VALUES ('{}', '{}', {})
# """.format('Giorgi', 'giorgi@gmail.com', 1500))

# cursor.execute("""
#     INSERT INTO users (Name, Email, Balance)
#     VALUES (?, ?, ?)
# """, ('Qeti', 'qeti@gmail.com', 2000))

# cursor.execute("""
#     INSERT INTO users (Name, Email, Balance)
#     VALUES (:name, :email, :bal)
# """, {"name": "nika", "email": "kankia@gmail.com", "bal": 500})

def add_user(username, email, balance):
    cursor.execute("""
    INSERT INTO users (Name, Email, Balance)
    VALUES (?, ?, ?)
    """, (username, email, balance))


# cursor.execute("DELETE from users where email = 'example@gmail.com'")
cursor.execute('UPDATE users SET balance = 4500 where id = 2')

result = list(cursor.execute("select * from users where balance > 500")) # iterator

print(result)

# print(cursor.fetchall())
# print(cursor.fetchmany(2))
# print(cursor.fetchone())

connection.commit()
connection.close()
