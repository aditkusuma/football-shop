1.	Explain how you implemented the checklist above step-by-step (not just by following the tutorial).
•	I first  make a directory named football-shop
•	Then create and activate the virtual environment
•	Then by creating and filling the requirements.txt, I can now install django 
•	Then I create the .env and .env.prod
•	I modify the settings to load variables from .env, add the allowed hosts,and change the configuration for production and databases. That’s how we make and cofigure a django project
•	Then to create and app called main by running “python manage.py startapp main” on terminal and then register main in the installed apps of settings.py
•	The crate Product in models.py following the criteria needed
•	Then in views.py we create a function which handles HTTP request and return the intended view which is the data we want to send
•	Then in main.html we display the data that are sent from views.py
•	Then we configure the URL routing for the main app, then the project url routing
•	To connect to pws, we need to configure the envornment variables
•	Then add the pws deployment url to allowed hosts in the settings.py in the project root
•	Then we sync it to git and link to the pws by using commands

2.	Create a diagram showing the client request to the Django-based web application and its response, and explain the relationship between urls.py, views.py, models.py, and the HTML file in the diagram.

request -> urls.py -> view -> model -> HTML file rendered by view -> HTTP response

browser sned HTTP request, urls.py matches the path to a view, view runs logic to reads/write Model, view then renders HTML file with a context dict to HTML string, and finally view wraps the html in an HTTP Response and returns it to the browser

3.	Explain the role of settings.py in a Django project!
It centralizes project configuration. One place where Django reads all project settings at startup. It is for security & environment, project wiring, templates, database, locale & time, static & media, authorization, and best practice where it keep secrets/ config in environment variables, set Debug=False in production

4.	How does database migration work in Django?
After we edit models, run makemigration which generates migration files, then we run migrat which applies those files to the DB, Django tracks applied migrations in the django_migration tables so it knows whats pending.

5.	In your opinion, among all existing frameworks, why is the Django framework chosen as the starting point for learning software development?
Django teaches web developtment with good defaults and limitations, letting beginners build meaningful apps quickly while implementing industry best practices. It has a faster learning loop, clear architecture, strong data model, instant back office, security by default, excellent docs & community, python ecosystem, scales from mini to serious and testing support.

6.	Do you have any feedback for the teaching assistant for Tutorial 1 that you previously completed?
No, I think that the teaching assistant have been really helpful


