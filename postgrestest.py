import psycopg2

con = psycopg2.connect(dbname="d2u7bl3cupfi4a", user="zdlzhorfdrsbfz",
                  password="e6ba37e8bb58288971214a6bab5d0f0cbfec184d0850d8b08e984a4c782bb4b3",
                  host="ec2-52-213-167-210.eu-west-1.compute.amazonaws.com")
cur = con.cursor()
# cur.execute(f"""INSERT INTO main.theatres (id, name, city, password)
# VALUES (0, 'first', 'Стерлипариж', '12345')""")
# con.commit()
cur.execute(f"""SELECT * from main.theatres""")
print(cur.fetchall())
cur.close()
con.close()
