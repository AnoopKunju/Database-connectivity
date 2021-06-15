import pymysql
import csv

conn = pymysql.connect(
  host="acadmysqldb001p.uta.edu",
  user="srn3489",
  passwd="Ran@0802",
  database="srn3489"
)
try:
    cursor = conn.cursor()
    print("Connected")
except:
    print("DB connection failed")

cursor.execute("SET FOREIGN_KEY_CHECKS = 0")

with open('EMPLOYEE.txt', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar="'")
    for row in reader:
        if len(row)==0:
            continue
        rows = []
        for i in range(0,len(row)):
            row[i] = row[i].replace("'","")
            row[i] = row[i].lstrip()
            if i!=5:
                row[i] = row[i].replace(",","")
            if row[i] != 'null':
                # print(row[i])
                rows.append(row[i])
            else:
                rows.append(None)
        print(rows);
        try:
            cursor.execute('INSERT INTO EMPLOYEE VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', rows)
            conn.commit()
        except pymysql.IntegrityError as err:
            # print("Error: {}".format(err))
            print("Error encountered! Ignoring that line and continuing")
            continue
conn.commit()

with open('DEPARTMENT.txt', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar="'")
    for row in reader:
        if len(row)==0:
            continue
        rows = []
        for i in range(0,len(row)):
            row[i] = row[i].replace("'","")
            row[i] = row[i].replace(",","")
            row[i] = row[i].lstrip()
            if row[i] == 'null':
                rows.append(None)
                continue
            else:
                rows.append(row[i])
                # print(row[i])
        print(rows)
        try:
            cursor.execute('INSERT INTO DEPARTMENT VALUES(%s,%s,%s,%s)', rows)
        except pymysql.IntegrityError as err:
            # print("Error: {}".format(err))
            print("Error encountered! Ignoring that line and continuing")
            continue
# conn.commit()
# cursor.execute('ALTER TABLE EMPLOYEE ADD CONSTRAINT FK_DEPARTMENT FOREIGN KEY (Dno) REFERENCES DEPARTMENT (Dnumber)')
conn.commit()

# cursor.execute('ALTER TABLE EMPLOYEE ADD CONSTRAINT FK_DEPARTMENT FOREIGN KEY (Dno) REFERENCES DEPARTMENT (Dnumber)')
cursor.execute("SET FOREIGN_KEY_CHECKS = 1");
conn.commit()

with open('DEPT_LOCATIONS.txt', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        if len(row)==0:
            continue
        rows = []
        for i in range(0,len(row)):
            row[i] = row[i].replace("'","")
            row[i] = row[i].lstrip()
            rows.append(row[i])
            # print(row[i])
        print(rows)
        try:
            cursor.execute('INSERT INTO DEPT_LOCATIONS VALUES(%s,%s)', rows)
        except pymysql.IntegrityError as err:
            # print("Error: {}".format(err))
            print("Error encountered! Ignoring that line and continuing")
            continue
conn.commit()

with open('PROJECT.txt', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        if len(row)==0:
            continue;
        rows = []
        for i in range(0,len(row)):
            row[i] = row[i].replace("'","")
            row[i] = row[i].lstrip()
            rows.append(row[i])
            # print(row[i])
        print(rows)
        try:
            cursor.execute('INSERT INTO PROJECT VALUES(%s,%s,%s,%s)', rows)
        except pymysql.IntegrityError as err:
            # print("Error: {}".format(err))
            print("Error encountered! Ignoring that line and continuing")
            continue
conn.commit()

with open('WORKS_ON.txt', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        if len(row)==0:
            continue;
        for i in range(0,len(row)):
            row[i] = row[i].replace(",","")
            row[i] = row[i].replace("'","")
            row[i] = row[i].lstrip()
            # print(row[i])
        print(row)
        try:
            cursor.execute('INSERT INTO WORKS_ON VALUES(%s,%s,%s)', row)
        except pymysql.IntegrityError as err:
            # print("Error: {}".format(err))
            print("Error encountered! Ignoring that line and continuing")
            continue
conn.commit()

with open('DEPENDENT.txt', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        if len(row)==0:
            continue;
        for i in range(0,len(row)):
            row[i] = row[i].replace("'","")
            row[i] = row[i].lstrip()
        print(row)
        try:
            cursor.execute('INSERT INTO DEPENDENT VALUES(%s,%s,%s,%s,%s)', row)
        except pymysql.IntegrityError as err:
            # print("Error: {}".format(err))
            print("Error encountered! Ignoring that line and continuing")
            continue
conn.commit()
cursor.close()
