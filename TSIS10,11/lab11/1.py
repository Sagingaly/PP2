

import psycopg2
import re



DB_HOST = "localhost"
DB_PORT = 5432
DB_USER = "postgres"
DB_PASSWORD = ""

conn = psycopg2.connect(
    host=DB_HOST,
    port=DB_PORT,
    user=DB_USER,
    password=DB_PASSWORD,
)

cur = conn.cursor()


# 1
def do_task1(pattern):
    if re.match(r"^-?\d+$", pattern):
        query = f"SELECT * FROM public.phonebook WHERE phone::text LIKE '%{pattern}%'"
    else:
        query = f"SELECT * FROM public.phonebook WHERE username LIKE '%{pattern}%'"

    cur.execute(query)
    records = cur.fetchall()

    if not records:
        print("Nothing found")
        return

    for record in records:
        phone = record[0]
        username = record[1]

        print("Phone - %i    Username - %s" % (phone, username))


# 2
def do_task2(username, phone):
    create_procedure_for_insert_user()
    cur.execute("CALL insert_or_update_user(%s, %s)", (username, phone))
    conn.commit()


# 3
def do_task3():
    create_procedure_for_insert_many_users()
    phone_list = ['87472341442000', '87472341441', '87472341543', '87472341401', '87472424441']
    name_list = ['Dana', 'Aidana', 'Ayakoz', 'Botagoz', 'Adiya']

    cur.callproc('insert_phonebook_data', (phone_list, name_list))
    results = cur.fetchall()

    for result in results:
        print("Invalid phone number:", result[0], "Username:", result[1])

    conn.commit()

def do_task4(limit, offset):
    cur.execute(f"""
        SELECT * FROM public.phonebook LIMIT {limit} OFFSET {offset}
    """)

    records = cur.fetchall()

    for record in records:
        phone = record[0]
        username = record[1]

        print("Phone - %i    Username - %s" % (phone, username))


def do_task5(username_or_phone):
    create_procedure_for_delete_user()
    cur.execute("""CALL delete_user(%s)""", [username_or_phone])

    conn.commit()


def create_procedure_for_insert_user():
    cur.execute("""
        CREATE OR REPLACE PROCEDURE insert_or_update_user(
            IN p_username TEXT,
            IN p_phone BIGINT
        )
        LANGUAGE plpgsql
        AS $$
        BEGIN
            IF EXISTS (SELECT 1 FROM public.phonebook WHERE username = p_username) THEN
                
                UPDATE public.phonebook SET phone = p_phone WHERE username = p_username;
            ELSE
                INSERT INTO public.phonebook (username, phone) VALUES (p_username, p_phone);
            END IF;
        END;
        $$;
    """)

    conn.commit()


def create_procedure_for_insert_many_users():
    cur.execute("""CREATE OR REPLACE FUNCTION insert_phonebook_data(
        phone_list text[],
        name_list text[]
    )
        RETURNS TABLE (
            invalid_phone bigint,
            invalid_username text
        )
        AS $$
        DECLARE
            i integer := 1;
            phone bigint;
        BEGIN
        
            CREATE TEMPORARY TABLE temp_invalid_data (
                invalid_phone bigint,
                invalid_username text
            );
        
        
            FOR i IN 1..array_length(phone_list, 1) LOOP
          
                phone := phone_list[i]::bigint;
        
                IF phone >= 10000000000 AND phone <= 99999999999 THEN
                   
                    INSERT INTO phonebook(phone, username)
                    VALUES(phone, name_list[i]);
                ELSE
                    
                    INSERT INTO temp_invalid_data(invalid_phone, invalid_username)
                    VALUES(phone, name_list[i]);
                END IF;
            END LOOP;
            
           
            RETURN QUERY SELECT * FROM temp_invalid_data;
        END;
        $$ LANGUAGE plpgsql;
    
        """)
    conn.commit()



def create_procedure_for_delete_user():
    cur.execute("""
        CREATE OR REPLACE PROCEDURE delete_user(input_value TEXT)
            LANGUAGE plpgsql
            AS $$
            BEGIN
                IF input_value ~ '^\d+$' THEN
                    DELETE FROM phonebook WHERE phone = input_value::BIGINT;
                ELSE
                    DELETE FROM phonebook WHERE username = input_value;
                END IF;
            END;
            $$;
    """)
    conn.commit()






def main():
    print(
        "1. Function that returns all records based on a pattern (example of pattern: part of name, surname, phone number)")
    print("2. Create procedure to insert new user by name and phone, update phone if user already exists")
    print(
        "3. Create procedure to insert many new users by list of name and phone. Use loop and if statement in stored procedure. Check correctness of phone in procedure and return all incorrect data.")
    print("4. Create function to querying data from the tables with pagination (by limit and offset)")
    print("5. Implement procedure to deleting data from tables by username or phone")
    select = input("Select: ")

    if select == "1":
        pattern = input("Enter pattern: ")
        do_task1(pattern)
    elif select == "2":
        username = input("Enter username: ")
        phone = int(input("Enter phone: "))
        do_task2(username, phone)

    elif select == "3":

        do_task3()

    elif select == "4":
        limit = int(input("Enter limit: "))
        offset = int(input("Enter offset: "))
        do_task4(limit, offset)

    elif select == "5":

        username_or_phone = input("Enter username or phone: ")
        do_task5(username_or_phone)

main()
