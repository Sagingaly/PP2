import psycopg2
import pandas as pd
import re

DB_HOST = "localhost"
DB_PORT = 5432
DB_USER = "postgres"
DB_PASSWORD = "138311"


class PostgresSQL():
    def __init__(self):
        self.connection = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD,
        )
        self.cursor = self.connection.cursor()

    def fetchall(self, query=None, vars=None):
        if not query:
            return self.cursor.fetchall()

        self.cursor.execute(query, vars)
        return self.cursor.fetchall()

    def fetchone(self, query=None, vars=None):
        if not query:
            return self.cursor.fetchone()

        self.cursor.execute(query, vars)
        return self.cursor.fetchone()

    def execute(self, query, vars=None):

        if not vars:
            self.cursor.execute(query)
            return
        self.cursor.execute(query, vars)

        self.connection.commit()

    def commit(self, query=None, vars=None):
        if not query:
            self.connection.commit()

        self.cursor.execute(query, vars)
        self.connection.commit()

    def is_phone_exists(self, phone):
        return self.fetchone("""SELECT EXISTS(SELECT 1 FROM public.phonebook WHERE phone = %s);""", [phone])[0]


def main():
    db = PostgresSQL()
    db.commit("""CREATE TABLE IF NOT EXISTS
                public.phonebook(
                            phone bigint PRIMARY KEY,
                            username varchar(50)
                        );
                """)

    way = int(
        input("Please, select way:\n1. Upload data from csv file\n2. Entering user name, phone from console\nInput: "))

    if way == 1:
        path = input("Path to csv: ")
        df = pd.read_csv(path, low_memory=False)

        usernames, phones = list(df["username"]), list(df["phone"])
    else:
        usernames, phones = [input("Username: ")], [int(input("Phone: "))]

    for username, phone in zip(usernames, phones):

        if db.is_phone_exists(phone):
            db.commit("""UPDATE public.phonebook SET username=%s WHERE phone=%s;""", [username, phone])
            print("%i number owner is updated" % phone)

        else:
            db.commit("""INSERT INTO public.phonebook VALUES(%s, %s);""", [phone, username])

            print("%s inserted to table" % username)

    data = db.fetchall("""SELECT * FROM public.phonebook;""")
    print("\n\n\n")
    for d in data:
        phone = d[0]
        username = d[1]

        print("%s - %i" % (username, phone))

    print("\n\n\n")
    cin = input("Select the user or phone to delete: ")

    if re.match(r"^\d{11}$", cin):
        db.execute("""DELETE FROM public.phonebook WHERE phone=%s;""", [int(cin)])
        print("Phone %s is deleted" % cin)
    else:
        db.execute("""DELETE FROM public.phonebook WHERE username=%s;""", [cin])
        print("User %s is deleted" % cin)




main()