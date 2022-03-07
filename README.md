# ArtCollectionApp
This is the python Flask backend enables the user to interact with data.<br>
It contains functionality:
  <li>Register and Login </li> 
  <li>Add new category(Art) along with its title, category and image</li> 
  <li>Edit User Data </li> 
  <li>Edit the category title and category name (Allowed to only the author of the category)</li> 
  
 # Screenshot
 <b> Sample app create in unity to access the api and render the data </b>
 
 <b>Login and Register screen</b><br>
for logging in to the system:<br>
  -> <b>API EndPoint URL</b> : api/users/ <br><br>
  -> <b>HTTP method</b>: GET<br>
  -> <b>Parameters</b>:<br>
      -email: This is the email address of the registerd user.<br>
      -password: This is the password of the email address.<br><br>
      
  -> <b>eg payload</b>:<br>
    {<br>
      "email": "your email",<br>
      "password": "your password"<br>
    }<br><br>
   
   -><b>Response</b>:<br>
     if success:<br>
      {<br>
        "email": "your email",<br>
        "name": "your name",<br>
        "phone_number": "number",<br>
        "role": "admin",<br>
        "status": "success",<br>
        "userid": "Id of the logged in user"<br>
      }<br><br>
      if error:<br>
      {<br>
        "status": "error"<br>
      }<br><br>
      
   for Registering user into the system:<br>
  -> <b>API EndPoint URL</b> : api/users/ <br><br>
  -> <b>HTTP method</b>: POST<br>
  -> <b>Parameters</b>:<br>
      -email: This is the email address of the registerd user.<br>
      -password: This is the password of the email address.<br><br>
      
  -> <b>eg payload</b>:<br>
    {<br>
      "name": "your Name",<br>
      "email": "your email",<br>
      "password": "your password"<br>
      "phone_number": "your password"<br>
      "password": "your password"<br>
      "role": "Admin or User"<br>
    }<br><br>
   
   -><b>Response</b>:<br>
     if success:<br>
      {<br>
        "status": "success"<br>
      }<br>
      if error:<br>
      {<br>
        "status": "error"<br>
      }<br>
 <p align="center">
  <img src="screenshots/Login.jpg" width="350" title="hover text">
  <img src="screenshots/Register.jpg" width="350" alt="accessibility text">
</p>
<br><br><hr>
<b>Home Screen</b><br><br>
This is the HomePage where all the arts from the database are retreived from the database and displayed.<br>
  -> <b>API EndPoint URL</b> : api/category/ <br><br>
  -> <b>HTTP method</b>: GET<br><br>
  
  -><b>Response Format</b>:{<br>
  "userid": "ID of the user who uploaded the Art",<br>
  "categoryid": "CategoryId of the Art",<br>
  "title" : "Name of Art",<br>
  "category": "Brief description of Art",<br>
  "rating" : "Rating of the Art",<br>
  "author_name": "Name of author who uploaded the Art",<br>
}<br><br>
<p align="center">
  <img src="screenshots/HomePage.jpg" width="350" title="hover text">
</p><br><br><hr>

for Adding New Art Category:<br>
  -> <b>API EndPoint URL</b> : api/category/ <br><br>
  -> <b>HTTP method</b>: POST<br>
  -> <b>Parameters</b>:<br>
      -userid: This is the userid of the registerd user who is adding the category.<br>
      -title: Title name.<br>
      -category: Category name.<br>
      -image: Image name.<br>
      -rating: "Total ratings of the Art"<br><br>
   
   -><b>Response</b>:<br>
     if success:<br>
      {<br>
        "status": "success"<br>
      }<br>
      if error:<br>
      {<br>
        "status": "error"<br>
      }<br>
<p align="center">
  <img src="screenshots/AddNewCategory.jpg" width="350" title="hover text">
</p><br><br><hr>

for Editing The User profile:<br>
  -> <b>API EndPoint URL</b> : api/users/edit/<int:id> <br><br>
  -> <b>HTTP method</b>: PUT<br>
  -> <b>Parameters</b>:<br>
        "email": "your email",<br>
        "name": "your name",<br>
        "phone_number": "number",<br>
        "role": "admin",<br>
  
   -><b>Response</b>:<br>
     if success:<br>
      {<br>
        "status": "success"<br>
      }<br>
      if error:<br>
      {<br>
        "status": "error"<br>
      }<br>
<p align="center">
  <img src="screenshots/EditProfile.jpg" width="350" title="hover text">
</p>


  
