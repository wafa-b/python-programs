import MySQLdb

db = MySQLdb.connect("localhost","test","1234","employees")

curser = db.curser()

# query = """CREATE TABLE EMPLOYEES-DETAILES(
#             NAME CHAR(50),
#             DEPARTMENT CHAR(5))"""
# try:
#     curser.execute(query)
# except:
#     print('Can not add new table')
# else:
#     print('table dded')

# query2 = """INSERT INTO EMPLOYEES-DETAILES(NAME,DEPARTMENT) VALUES ('MAHMOOD','IT') """
#
# try:
#     curser.execute(query2)
# except:
#     print('Can not add new row')
# else:
#     print('Row Inserted')

query3 = "SELECT * FROM EMPLOYEES-DETAILES"

try:
    curser.execute(query3)
    data = curser.fetchall()
    for row in data:
        name = row[0]
        department = row[1]
        print("Name= %s ,Department= %s "%(name,department))
except:
    print('Can not fetched data')
else:
    print('data fetched')

db.close()
