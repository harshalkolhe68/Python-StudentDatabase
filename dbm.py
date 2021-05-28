import pymysql as p
def getConnection():
    return p.connect (host='localhost', user='root', password='', database='harshal')

def addStudent(t):
    db=getConnection()
    sql='insert into student values(%s,%s,%s,%s,%s,%s)'
    cr=db.cursor()
    cr.execute(sql,t)
    db.commit()
    db.close()

def selectAllStudent():
    db=getConnection()
    sql='select * from student'
    cr=db.cursor()
    cr.execute(sql)
    slist=cr.fetchall()
    db.commit()
    db.close()
    return slist

def deleteStudent(id):
    db=getConnection()
    sql= 'delete from student where id=%s'
    cr=db.cursor()
    cr.execute(sql,id)
    db.commit()
    db.close

def selectStudentByrollno(id):
    db=getConnection()
    sql='select * from student where id=%s'  
    cr=db.cursor()
    cr.execute(sql,id)
    slist=cr.fetchall()
    db.commit()
    db.close()
    return slist[0]

def updateStudent(t):
    db=getConnection()
    sql='update student set name=%s,college=%s,email=%s,age=%s,gender=%s where id=%s'
    cr=db.cursor()
    cr.execute(sql,t)
    db.commit()
    db.close()
    
