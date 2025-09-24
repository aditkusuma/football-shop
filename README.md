Assignment 2

1. Explain how you implemented the checklist above step-by-step (not just by following the tutorial). • I first make a directory named football-shop • Then create and activate the virtual environment • Then by creating and filling the requirements.txt, I can now install django • Then I create the .env and .env.prod • I modify the settings to load variables from .env, add the allowed hosts,and change the configuration for production and databases. That’s how we make and cofigure a django project • Then to create and app called main by running “python manage.py startapp main” on terminal and then register main in the installed apps of settings.py • The crate Product in models.py following the criteria needed • Then in views.py we create a function which handles HTTP request and return the intended view which is the data we want to send • Then in main.html we display the data that are sent from views.py • Then we configure the URL routing for the main app, then the project url routing • To connect to pws, we need to configure the envornment variables • Then add the pws deployment url to allowed hosts in the settings.py in the project root • Then we sync it to git and link to the pws by using commands

2. Create a diagram showing the client request to the Django-based web application and its response, and explain the relationship between urls.py, views.py, models.py, and the HTML file in the diagram.

request -> urls.py -> view -> model -> HTML file rendered by view -> HTTP response

browser sned HTTP request, urls.py matches the path to a view, view runs logic to reads/write Model, view then renders HTML file with a context dict to HTML string, and finally view wraps the html in an HTTP Response and returns it to the browser

3. Explain the role of settings.py in a Django project! It centralizes project configuration. One place where Django reads all project settings at startup. It is for security & environment, project wiring, templates, database, locale & time, static & media, authorization, and best practice where it keep secrets/ config in environment variables, set Debug=False in production

4. How does database migration work in Django? After we edit models, run makemigration which generates migration files, then we run migrat which applies those files to the DB, Django tracks applied migrations in the django_migration tables so it knows whats pending.

5. In your opinion, among all existing frameworks, why is the Django framework chosen as the starting point for learning software development? Django teaches web developtment with good defaults and limitations, letting beginners build meaningful apps quickly while implementing industry best practices. It has a faster learning loop, clear architecture, strong data model, instant back office, security by default, excellent docs & community, python ecosystem, scales from mini to serious and testing support.

6. Do you have any feedback for the teaching assistant for Tutorial 1 that you previously completed? No, I think that the teaching assistant have been really helpful

Assignment 3

1.	Answer the following questions in the README.md file in the root folder.
-	Why do we need data delivery in implementing a platform?
In today’s web development landscape, a single platform often needs to serve many different clients such as desktop browsers, mobile apps, and even third-party services. To support this flexibility, it’s crucial to separate the data layer from the presentation layer. By doing so, the same data can be provided to multiple front-ends without being tied to one specific interface. Exposing the application’s data in machine-readable formats like JSON or XML makes this possible.

-	 In your opinion, which is better, XML or JSON? Why is JSON more popular than XML?
XML supports complex document schemas but is complicated. JSON is lighter, faster to parse, and maps directly to Python objects and JavaScript, which explains its dominance in modern web APIs. For Football Shop, JSON is the natural default.

-	What is the purpose of the is_valid() method in Django forms, and why do we need it?
The is_valid() method ensures that all user input passes validation before it is stored in the database. When called, it runs every field validator and returns True only if the data is clean and correct. It also provides a cleaned_data dictionary containing safely processed values. In Football Shop, this mechanism guarantees that information such as product name, price, and image URL is accurate and secure, preventing invalid or unsafe data from being saved.

-	Why do we need a csrf_token when making forms in Django? What can happen if we don't include a csrf_token in a Django form? How can this be exploited by an attacker?
Every POST form in Football Shop includes a {% csrf_token %} to protect against Cross-Site Request Forgery (CSRF) attacks. A CSRF attack occurs when a malicious site tricks a logged in user into submitting an unwanted request such as creating or editing a product using the user’s credentials. Django checks the token on each submission to ensure that the action really comes from the Football Shop site. Without this protection, an attacker could forge requests and compromise the integrity of the application.
-	Explain how you implemented the checklist above step-by-step (not just following the tutorial).
a Product model was defined with six required fields such as name, price, description, thumbnail, category, and is_featured to represent the key attributes of each item. A ProductForm model form was added to simplify input and validation. Views were implemented to list all products (show_main), add a new product (add_product), and show product details (show_detail). Four data-delivery views show_json, show_xml, show_json_by_id, and show_xml_by_id use Django’s serializers to output data in JSON or XML. All views were connected through urls.py, templates were created to match the Football Shop theme, and the app was deployed to PWS with the proper ALLOWED_HOSTS and CSRF_TRUSTED_ORIGINS settings. 
-	Do you have any feedback for the teaching assistants for Tutorial 2?
Tutorial 2 was clear and the teaching assistant is very helpful
2.	Access the four URLs in point 2 using Postman, take screenshots of the URL access results in Postman, and add them to your README.md.

![JSON](images/json.png)
![XML](images/xml.png)
![JSON_id](images/json_id.png)
![XML_id](images/xml_id.png)

Assignment 4

1. What is Django's AuthenticationForm? Explain its advantages and disadvantages.
AuthenticationForm is Django’s built-in login form that validates a user’s username and password against the configured authentication backends. It integrates seamlessly with authenticate() and login(), provides secure password checking and generic error messages to prevent user enumeration. Its downsides are limited default fields and generic error messages that may be less user friendly if you need to distinguish between “wrong password” and “user not found.”
2. What is the difference between authentication and authorization? How does Django implement the two concepts?
Authentication verifies who a user is, while authorization determines what that authenticated user is allowed to do. Django handles authentication through its User model, authentication backends, the authenticate() and login() functions, and AuthenticationMiddleware which sets request.user. Authorization is handled via permissions (user.has_perm()), groups, and decorators/mixins like @login_required or @permission_required. Together they ensure only verified users access resources and only within their allowed privileges.
3. What are the benefits and drawbacks of using sessions and cookies in storing the state of a web application?
Cookies store small key value data directly in the browser, making them lightweight and requiring no server storage, but they are size limited and vulnerable to tampering or theft if not properly secured. Sessions keep state on the server and store only a session ID in a cookie, allowing larger and safer storage, centralized invalidation, and easier sensitive data handling, but require server storage and scaling considerations. Django defaults to database backed sessions with automatic session key rotation on login, balancing security
4. in web development, is the usage of cookies secure by default, or is there any potential risk that we should be aware of? How does Django handle this problem?
Cookies are not secure by default, they can be intercepted over plain HTTP, read by malicious JavaScript (XSS), or abused for CSRF attacks if not configured correctly. Django mitigates these risks with defaults and settings such as SESSION_COOKIE_HTTPONLY=True (blocks JavaScript access), SESSION_COOKIE_SAMESITE='Lax' (helps against CSRF), and recommended production settings like SESSION_COOKIE_SECURE=True and CSRF_COOKIE_SECURE=True to force HTTPS. It also cryptographically signs data in signed-cookie sessions and rotates session keys on login to prevent session fixation, making cookies safe when these measures are properly enabled.
5. Explain how you implemented the checklist above step-by-step (not just following the tutorial).
In my football-shop product app, I first set up user authentication by adding register, login, and logout views: register uses UserCreationForm to create new accounts, login_view uses AuthenticationForm and login() to authenticate and set a last_login cookie, and logout_view calls logout() while deleting the cookie. I updated urls.py with these routes and secured pages like show_main and add_product with @login_required. Next, I connected each Product to its owner by adding a user = models.ForeignKey(User, on_delete=models.CASCADE) field, running makemigrations and migrate, and modifying add_product to assign request.user before saving. In show_main, I filtered products with Product.objects.filter(user=request.user) and passed the username plus both the last_login cookie and Django’s built-in request.user.last_login to the template. Finally, the home page displays the logged-in user’s name and last login time while ensuring that only the owner’s products are visible.