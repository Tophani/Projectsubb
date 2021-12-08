

import os
from flask import Flask, render_template, request, redirect, flash
from db import mydb, mycursor
from werkzeug.utils import secure_filename

LINKERS='static\img'
app = Flask(__name__)
app.config['UPLOAD FOLDER']= LINKERS
@app.route('/', methods=["GET", "POST"])
def index():
    
    if request.method=='POST':
        _hidden = request.form['moth']

        if _hidden=='login':
            _name= request.form['name']
            _email = request.form['email']
            mycursor.execute(f'SELECT * FROM Account WHERE name = "{_name}" and  Email="{_email}"')
            verf= mycursor.fetchone()
            if verf:
                return redirect(f'/home/{_name}')

        if _hidden == 'register':
            _inpName= request.form['name']
            # _inpAdress= request.form['address']
            _inpEmail = request.form['email']
            _inpPhone_no = request.form['phone_no']
            # _inpAge = request.form['age']
            _inpPassword = request.form['password']
            # _inptype = request.form['student']
            # _inptype = request.form['moth']
            mycursor.execute(f'INSERT INTO Account(name, Email, Phone_number, password, type) VALUES("{_inpName}", "{_inpEmail}", "{_inpPhone_no}", "{_inpPassword}", "student" )')
            mydb.commit()
            return redirect(f'/home/{_inpName}')
    # mycursor.execute('SELECT * FROM Account')
    # account = mycursor.fetchall()
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def clear():
    
    if request.methods == "post":
        _name = request.form['name']
        _email =request.form['email']
        _phone_no = request.form['phone_no']
        mycursor.execute(f'INSERT INTO Account(name, email, phone_no) VALUES (%s, %s, %s, )')
    return redirect('/clear')



@app.route('/home/<name>',methods=['GET', 'POST'])
def paste(name):
    message=''
    if request.method== 'POST':
        _type = request.form['user']
        if _type == "admin":
            _bkname = request.form['bkname']
            _author = request.form['author']
            _view = request.form['view']
            # mycursor.execute(f'SELECT * FROM Upload ')
        # _location = request.form['location']
        # _genre = request.form['genre']
            f = request.files['file']
            filename= secure_filename(f.filename)
            f.save(os.path.join(app.config['UPLOAD FOLDER'], filename))
            mycursor.execute(f'INSERT INTO Upload(Book,Author,View,location) VALUES ("{_bkname}","{_author}","{_view}", "/static/img/{filename}")')
            mydb.commit()
            message= "Successfully Added"
            # flash("Succefully Added!!!")
            # return redirect('/')

    mycursor.execute(f'SELECT * FROM Account WHERE name="{name}"')

    user = mycursor.fetchone()

    mycursor.execute('SELECT * FROM Upload')
    book= mycursor.fetchall()
    return render_template('mainpage.html', user=user, msg=message, book=book, name=name)
    # if request.method == "GET":
    #     mycursor.execute(f'SELECT * FROM Account')
    #     account = mycursor.fetchall()
    #     return render_template('view.html')
    

@app.route('/login', methods =['GET', 'POST'])
def chair():
    if request.method =="GET":
        return render_template('register.html')



if __name__ == '__main__':
    app.run(debug=True)