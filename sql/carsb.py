import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()
    # insert multiple records using a tuple
    cars = [
            ('Ford', 'Pinto', 42),
            ('Ford', 'Prefect', 1),
            ('Ford', 'Fiesta', 17),
            ('Honda', 'Accord', 150),
            ('Honda', 'Pilot', 226)
             ]

    c.executemany("INSERT INTO inventory(Make, Model, Quantity) values (?, ?, ?)", cars)


