# ArtCollectionApp
This is the python Flask backend enables the user to interact with data.<br>
It contains functionality:
  <li>Register and Login </li> 
  <li>Add new category(Art) along with its title, category and image</li> 
  <li>Edit User Data </li> 
  <li>Edit the category title and category name (Allowed to only the author of the category)</li> 

API:  
url :- api/users/ <br><br>
for logging in to the system:<br>
  -> Parameters:<br>
      -email: This is the email address of the registerd user.<br>
      -password: This is the password of the email address.<br><br>
   
  -> eg payload:<br>
    {<br>
      "email": "your email",<br>
      "password": "your password"<br>
    }<br><br>
   
   -> eg Response:<br>
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
      }<br>
  
 # Screenshot
 
 <b>Login and Register screen</b>
 <p align="center">
  <img src="screenshots/Login.jpg" width="350" title="hover text">
  <img src="screenshots/Register.jpg" width="350" alt="accessibility text">
</p>
<br><br><hr>
<b>Home Screen</b><br><br>
This is the HomePage where all the arts from the database are retreived from the database and displayed.<br>
Response Format:{<br>
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

<p align="center">
  <img src="screenshots/AddNewCategory.jpg" width="350" title="hover text">
</p><br><br><hr>

<p align="center">
  <img src="screenshots/EditProfile.jpg" width="350" title="hover text">
</p>


  
