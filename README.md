#  Seventh Week Assignment.

# Project Task/Challenge
The challenge was to create a Django application that manages a movie rental system: the app must provide the following functionality for any film (movie or series):   
- Add a film  
- Modify a film  
- List/Read a film  
- Delete a film  

The main logic of the app has to be implemented first in Django admin and then in using Django Rest Framework.

One piece of information that was given was that the film has a title, description, stock, price, availability, season (prequel and sequel), release date, price by rent day, and an image that should be saved on Amason S3 services.  

Also has a category system for the movies, manages the cast of any film (actors, director, …), and should organize the chapters by season (only for series).  Additionally, the app has to support the logic to have clients that should be able to rent copies of the films, another rule is that the film could only be rented for a max of 15 days, if the client doesn't return it on time, must be punished with the extra tax (the price of any extra day + $2 by day).

Talking about security the app should define JWT authentication, and permission by endpoints depending on the type of user. For example, should support an anonymous role that can see all the GET endpoints, on the other hand, the employee role has permission to see all, and also work with the renting process, finally, the administrator role should be able to see and modify all the information on the site.
 
The final requisites were that the app has to be published into Heroku using Docker, add Django-admin-command to seed records by table using Faker, also add the Postman collection. 


# Logic Diagram of the project.
![Diagram](https://github.com/Thevic16/trainee-python-week-7/blob/main/img/Sixth%20Week%20Assignement%20UML.drawio.png)

# Instruction to run the app.

- You have to specify the environment variables (see .env-example).
- There are some details to consider when specifying those variables:
    - The environment variable "DEBUG_STATE" (True / False) defines if the
      Django app runs in debugger mode or not. 
    - The environment variable "DATABASE_STATE" (Local / Deploy) define if the
        Django app uses the local database or specified URL database. 
      - If DATABASE_STATE=Local you have to specify DATABASE_STATE,
        DATABASE_NAME, DATABASE_USER, DATABASE_PASS, DATABASE_HOST and 
        DATABASE_PORT. (these are already defined for local docker-compose app).
      - If DATABASE_STATE=Deploy you only have to define DATABASE_URL.



# Heroku app credential (pre-created-accounts) for testing JWT.
- Account with administrator permission. <br />
Email: admin@filmrentalsystem.com <br />
Password: admin12345678 

- Account with employee permission. <br />
Email: employee@filmrentalsystem.com <br />
Password: employee12345678 

Also, If you wish you can create your accounts using the followings links.<br />

- Register your account. <br />
link: https://week7-film-rental-system.herokuapp.com/api/register/

- And then log in into admin view with some credential above to assign
your role (admin/employee). Note: You are also able to register accounts from
the admin view directly. <br />
link: https://week7-film-rental-system.herokuapp.com/admin/

# Heroku URLs for generate and refresh JWT token.
Note: This is using "Bearer" as the JWT prefix. 

link: https://week7-film-rental-system.herokuapp.com/api/auth/jwt/

link: https://week7-film-rental-system.herokuapp.com/api/auth/jwt/refresh/

# Heroku URl for API documentation. 
link: https://week7-film-rental-system.herokuapp.com/doc/

# Django-admin-command to seed ten records by table.
Note: It would be a good idea to run the commands in the same order that
appears down to avoid errors for nonexistent data dependency.

- python manage.py accountsgen (-a argument to create as admins or
-e argument to create as employees).
- python manage.py categoriesgen
- python manage.py filmsgen
- python manage.py seasonsgen
- python manage.py chaptersgen
- python manage.py rolesgen
- python manage.py personsgen
- python manage.py clientsgen
- python manage.py filmspersonsrolesgen
- python manage.py rentsgen

# Heroku URLs API apps (categories, films, seasons, chapters, persons, roles, films-persons-roles, clients and rents).
link: https://week7-film-rental-system.herokuapp.com/api/categories/

link: https://week7-film-rental-system.herokuapp.com/api/films/

link: https://week7-film-rental-system.herokuapp.com/api/seasons/

link: https://week7-film-rental-system.herokuapp.com/api/chapters/

link: https://week7-film-rental-system.herokuapp.com/api/persons/

link: https://week7-film-rental-system.herokuapp.com/api/roles/

link: https://week7-film-rental-system.herokuapp.com/api/films-persons-roles/

link: https://week7-film-rental-system.herokuapp.com/api/clients/

link: https://week7-film-rental-system.herokuapp.com/api/rents/

# Note about Phone number format in clients App.
The app receive phone number of the following format: "XXX-XXXX-XXXX" 
where X = number 
