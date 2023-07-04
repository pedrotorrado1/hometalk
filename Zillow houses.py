import sqlite3

connection = sqlite3.connect("zillow_houses.db")
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS houses (id INTEGER PRIMARY KEY, title TEXT, price TEXT, description TEXT, comments TEXT)")

for house in houses:
    cursor.execute("INSERT INTO houses (title, price, description, comments) VALUES (?, ?, ?, ?)", (house["title"], house["price"], house["description"], house["comments"]))

connection.commit()
