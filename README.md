# ArtCollectionApp
This is the python Flask backend enables the user to interact with data.

API:  
url :- api/users/ <br>
for logging in to the system:
  -> Parameters:
      -email: This is the email address of the registerd user.
      -password: This is the password of the email address.
   
  -> eg payload:
    {
      "email": "your email",
      "password": "your password"
    }
   
   -> eg Response:
     if success:
      {
        "email": "your email",
        "name": "your name",
        "phone_number": "number",
        "role": "admin",
        "status": "success",
        "userid": "Id of the logged in user"
      }
      if error:
      {
        "status": "error"
      }
  
  
  
