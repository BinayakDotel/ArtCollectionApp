from fileinput import filename
import mimetypes
from pickletools import read_bytes1
import MySQLdb
from flask import Flask, jsonify, render_template, request, redirect, session, sessions, Response, url_for
from flask_mysqldb import MySQL
from werkzeug.utils import secure_filename

import cv2 as cv
import sys,os

sys.path.append('components/')
from users import User

IMAGE_FOLDER= 'static/images/'
ALLOWED_EXTENSIONS=set(['png','jpg','jpeg','gif'])

app = Flask(__name__,template_folder='./FrontEnd/Templates',static_folder='./FrontEnd/static')

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'newsportal'
app.config['IMAGE_FOLDER'] = IMAGE_FOLDER

def allowed_file(filename):
    '''eg:
        filename= 'image.jpg'
        filename.rsplit('.',1) gives ['image', 'jpg']
    '''
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

mysql = MySQL(app)

@app.route('/api/users', methods=['GET','POST','DELETE'])
def login():
    if request.method=='GET':
        login_details= request.json
        email = login_details['email']
        password= login_details['password']

        cur= mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("SELECT * FROM users WHERE email=%s and password=%s",(email,password,))
        data= cur.fetchone()

        cur.close()

        if data is not None and len(data)>0:
            return jsonify({"status":"success",
                            "userid":data['userid'], 
                            "name": data['full_name'], 
                            "email":data['email'],
                            "phone_number":data['phone_number'], 
                            "role":data['role'],   
                            })
        else:
            return jsonify({"status":"error"})
    
    if request.method=='POST':
        details = request.json
        full_name= details['name']
        email= details['email']
        phone_number= details['phone_number']
        role= "user"
        password= details['password']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(full_name, email, password, phone_number, role) VALUES (%s, %s, %s, %s, %s)", (full_name, email, password, phone_number, role,))
        mysql.connection.commit()
        cur.close()
        
        return jsonify({"status":"success"})

@app.route('/api/users/edit/<int:id>', methods=['PUT'])
def edit(id):
    if request.method=='PUT':
        new_details= request.json
        
        cur= mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("UPDATE users SET full_name=%s, email=%s, phone_number=%s, role=%s WHERE users.userid = %s", (new_details['name'], new_details['email'], new_details['phone_number'], new_details['role'], id,))
        mysql.connection.commit()
        cur.close()

        return jsonify({"status":"success"})

@app.route('/api/category/edit/<int:id>', methods=['PUT'])
def edit_category(id):
    if request.method=='PUT':
        new_details= request.json
        
        cur= mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("UPDATE category SET title=%s,category=%s WHERE category.categoryid=%s", (new_details['title'],new_details['category'], id,))
        mysql.connection.commit()
        cur.close()

        return jsonify({"status":"success"})


#This is for updating the rating to any category item having category id = <int:id>
@app.route('/api/category/edit/rate/<int:id>', methods=['PUT'])
def rate_category(id):
    if request.method=='PUT':
        new_details= request.json
        
        cur= mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("UPDATE category SET rating=%s WHERE category.categoryid=%s", (new_details['rating'], id,))
        mysql.connection.commit()
        cur.close()

        return jsonify({"status":"success"})

#Uploading the image file to the static images folder
@app.route('/api/category/upload', methods=['GET','PUT','POST','DELETE'])
def upload_image():
    if request.method=='POST':
        image= request.files['image']

        if image:
            filename = secure_filename(image.filename).lower()
            mimetype = image.mimetype.lower()
            if not allowed_file(filename) or not filename or not mimetype:
                return jsonify({"status":"error"})

            image.save(os.path.join(app.config['IMAGE_FOLDER'], filename))
            return jsonify({"status":"success"})
        
        return jsonify({"status":"error"})
    
@app.route('/api/category/upload/<string:name>', methods=['GET'])
def get_image(name):
    if request.method=='GET':
        extension= name.rsplit('.',1)[1].lower()  

        if extension == 'jpg' or extension == 'jpeg':
            mimetype = f'image/jpeg'
        else:
            mimetype = f'image/{extension}'
        
        print(f"{extension} and {mimetype}")

        try:
            np_image= cv.imread(os.path.join(app.config['IMAGE_FOLDER'], name.lower()))

            _, img_encoded = cv.imencode(f".{extension}", np_image)
            image = img_encoded.tobytes()

            return Response(image, mimetype=mimetype)
        except:
            return jsonify({"status":"error"})
       
@app.route('/api/category', methods=['GET','PUT','POST','DELETE'])
def AddCategory():
    if request.method=='POST':
        details = request.json
        userid= details['userid']
        title= details['title']
        category= details['category']
        image= details['image']
        rating = "0"
        
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO category(title, image, category, rating, userid) VALUES (%s,%s,%s,%s,%s)",(title, image, category, rating, userid,))
        mysql.connection.commit()
        cur.close()

        return jsonify({"status":"success"})

    if request.method=='GET':
        cur= mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("SELECT category.categoryid, users.full_name, users.userid, category.title,category.category,category.image,category.rating from category JOIN users WHERE category.userid=users.userid;")
        data=cur.fetchall()

        print(data)
        cur.close()

        if not data:
            return "NO DATA FOUND", 404
        
        return jsonify(data)


if __name__ == '__main__':
    app.secret_key="!@#$%^&*"
    app.run()