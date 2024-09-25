import psycopg2

try:
    connect_str = "dbname='shubham'  user='shubham' host='localhost' " + "password='9504'"
    conn = psycopg2.connect(connect_str)
    cursor = conn.cursor()
    # cursor.execute("""CREATE TABLE test(name char(40));""")
    # cursor.execute("""SELECT * from test""")

    cursor.execute("""CREATE TABLE test()""")
    conn.commit()
    rows = cursor.fetchall()
    print(rows)
    cursor.close()
    conn.close()
except Exception as e:
    print("Exception occured cant connect : ", e)
