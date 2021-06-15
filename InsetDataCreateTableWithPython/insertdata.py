#NAME : Anoop Kunjumon Scariah
#ID: 1001757408

import pymysql
import pandas as pd
from sqlalchemy import create_engine

sqlengine = create_engine("mysql+pymysql://{user}:{pwd}@{host}/{db}"
                       .format(user="axs7408",
                               pwd="Add@5044",
                               host="acadmysqldb001p",
                               db="axs7408"))

dbconnect = sqlengine.connect()

with sqlengine.connect() as con:
        con.execute('SET FOREIGN_KEY_CHECKS = 0')

def execute_query(Table,data_df):
    try:
        data_df.to_sql(Table, con = sqlengine, if_exists = 'append' ,index=False)
    except ValueError as v:
        print(v)
    except Exception as e:
        print(e)
    else:
        print("successfully created table:---"+ Table); 

em_column_list = ["Fname","Minit","Lname","Ssn","Bdate","Address","Sex","Salary","Super_ssn","Dno"]
EMPLOYEE_df = pd.read_csv('Data\EMPLOYEE.txt', quotechar="'",skipinitialspace=True, names=em_column_list)
print(EMPLOYEE_df)

depart_column_list = ["Dname","Dnumber","Mgr_ssn","Mgr_start_date"]
DEPARTMENT_df = pd.read_csv('Data\DEPARTMENT.txt', quotechar="'",skipinitialspace=True, names=depart_column_list)

departLoc_column_list = ["Dnumber","Dlocation"]
DEPT_LOCATIONS_df = pd.read_csv('Data\DEPT_LOCATIONS.txt', quotechar="'",skipinitialspace=True, names=departLoc_column_list)

PROJECT_list = ["Pname","Pnumber","Plocation","Dnum"]
PROJECT_df = pd.read_csv('Data\PROJECT.txt', quotechar="'",skipinitialspace=True, names=PROJECT_list)

WORKS_ON_column_list = ["Essn","Pno","Hours"]
WORKS_ON_df = pd.read_csv('Data\WORKS_ON.txt', quotechar="'",skipinitialspace=True, names=WORKS_ON_column_list)

DEPENDENT_column_list = ["Essn","Dependent_name","Sex","Bdate", "Relationship"]
DEPENDENT_df = pd.read_csv('Data\DEPENDENT.txt', quotechar="'",skipinitialspace=True, names=DEPENDENT_column_list)

# execute_query('EMPLOYEE',EMPLOYEE_df)
# execute_query('DEPARTMENT',DEPARTMENT_df)
# execute_query('DEPT_LOCATIONS',DEPT_LOCATIONS_df)
# execute_query('PROJECT',PROJECT_df)
# execute_query('WORKS_ON',WORKS_ON_df)
# execute_query('DEPENDENT',DEPENDENT_df)

with sqlengine.connect() as con:
        con.execute('SET FOREIGN_KEY_CHECKS = 1')

dbconnect.close()
                               