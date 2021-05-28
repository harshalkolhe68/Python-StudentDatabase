from flask import *
from dbm import addStudent,selectAllStudent,deleteStudent,selectStudentByrollno,updateStudent
f=Flask(__name__)

@f.route('/')
def home():
    return render_template('home.html')

@f.route('/reg')
def register():
    return render_template('register.html')


@f.route('/addStudent',methods=['POST'])
def add_student():
    
    id=request.form['id']
    name=request.form['name']
    college=request.form['college']
    email=request.form['email']
    age=request.form['age']
    gender=request.form['gender']
    t=(id,name,college,email,age,gender)
    addStudent(t)
    return redirect('/')

@f.route('/studentlist')
def student_list():
    sl=selectAllStudent()
    return render_template("studentlist.html",slist=sl)

@f.route('/deleteStudent')
def delete_Student():
    id=request.args.get('id')
    deleteStudent(id)
    return redirect('/studentlist')

@f.route('/editStudent')
def edit_Student():
    id=request.args.get('id')
    student=selectStudentByrollno(id)
    return render_template('updateStudent.html',e=student)

@f.route('/updateStudent',methods=['POST'])
def update_student():
    
    id=request.form['id']
    name=request.form['name']
    college=request.form['college']
    email=request.form['email']
    age=request.form['age']
    gender=request.form['gender']
    t=(name,college,email,age,gender,id)
    updateStudent(t)
    return redirect('/studentlist')

if __name__=='__main__':
    f.run(debug=True)
