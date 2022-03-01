# ArtCollectionApp
This is the python Flask backend enables the user to interact with data.

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
  
  
  
