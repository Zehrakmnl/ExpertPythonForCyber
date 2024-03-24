import sqlite3
from employee import Employee

# conn = sqlite3.connect('employee.db')
conn = sqlite3.connect(':memory:') # her seferinde sıfırdan başlar.

c = conn.cursor()

c.execute("""CREATE TABLE employees (
          first text,
          last text,
          pay integer
          ) """)

c.execute("INSERT INTO employees VALUES ('Emp2','sname', 1000)")

def insert_emp(emp):
    with conn:
        c. execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': emp.first, 'last': emp.last, 'pay': emp.pay})
        return c.fetchall()
    

def get_emps_by_name (lastname):
    c.execute("SELECT * FROM employees WHERE last=:last", {'last': lastname})

def update_pay (emp, pay) :
    with conn:
        c. execute ("""UPDATE employees SET pay = :pay WHERE first = :first AND last = :last""", {'first': emp.first, 'last': emp.last, 'pay': pay})
def remove_emp (emp) :
    with conn:
        c. execute("DELETE from employees WHERE first = :first AND last = :last",
        {'first': emp.first, 'last': emp. last})


emp_1 = Employee('Emp1','sname1', 12000)
emp_2 = Employee('Emp2','sname2', 13000)
emp_3 = Employee('Emp3','sname3', 12000)
emp_4 = Employee('Emp4','sname4', 12500)

insert_emp(emp_1)
insert_emp(emp_2)

emps = get_emps_by_name('emp1')
print(emps)

update_pay(emp_2, 9000)
remove_emp(emp_4)


# c. execute("INSERT INTO employees VALUES (?, ?, ?)", (emp_1.first, emp_1. last, emp_1. pay))
# conn.commit()

# c. execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first':emp_1.first, 'last':emp_1. last, 'pay':emp_1. pay})
# conn.commit()

# c.execute("SELECT * FROM employees WHERE last='sname'")

# #c.fetchone() / fetchall / c.fetchmany(5)
# print(c.fetchall())

conn.commit()

conn.close()
