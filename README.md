#  Seventh Week Assignment.

# Logic Diagram of the project.
![Diagram](https://gitlab.com/t7501/fifth-week-assignment/-/blob/feature/django/models/img/Fifth%20Week%20Assignement%20UML.drawio.png)

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
- python manage.py clientsgen
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