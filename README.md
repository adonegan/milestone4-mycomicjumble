# My Comic Jumble

[![Build Status](https://travis-ci.org/adonegan/milestone4-mycomicjumble.svg?branch=master)](https://travis-ci.org/adonegan/milestone4-mycomicjumble)
My Comic Jumble is a small online store selling second-hand comic books. The owner of My Comic Jumble is selling comics from their own comic book collection because they want to downsize. The purpose of My Comic Jumble is to display, describe and sell second-hand comic lovers.

## UX

This is a simple app where customers can browse, view, purchase and give feedback on the product, a miscellaneous collection of comic books. The website is for comic book collectors and enthusiasts looking for specific issues of their favourite comics. As a user of this site I want / need / expect to:

- Browse comics by category and name
- Save comics to my cart and continue to browse
- Use my credit card at checkout to purchase what I want
- Give feedback or leave a note on what I think about the site and the collection of comics
- Search for comics on the store by name and category
- Click buttons to easily see comics by category
- See how old the second-hand product item is
- Find out the grade and condition of the issue I want to buy
- Be able to register to the website and then login to my own account

## Features

### Existing Features

#### All pages

Navbar

- Every page features a navbar which signals where users can find each page or main feature. The navbar hosts the following links: Home, About, Comics, Search, Register and Login. The navbar also shows the site's name so it can be viewed on each page too. The navbar is reponsive and the links collapse on smaller screens, to be replaced by a hamburger menu icon.

Footer

- This is a simple section signalling the end of the website on the page. In this section, the user will find social icons and links to other sections of the site. It also includes...

Both section features have been created on the base.html page and follow templating language. The area between both sections changes depending on the page it is extending to.

Home Page

- Jumbotron: this is the main text area that introduces users to the website, its mission and what users can find on the platform.

- Info cards: these colorful Bootstrap cards give the user a taste of what they can find on the website. They link to various places on the website.

About Page

- This page features two images and two text boxes and gives more information to the user about the purpose of the site and its creator.

Comics Page

- This page is the main product page and showcases all the comics that can be purchased on the app. With minimal information in mind, this page only showcases comic covers, name and price.

- Pagination:

Details Page

- Once a visitor clicks on an item in the Comics Page they will be taken to that item's detail page. Here they can see a larger version of the comic and find out specific information about it, including: name, price, description, penciler, writer, cover artist, price, grade and condition.

- Checkout button:

Glossary Page

- A single page with information on the kind of terms used to talk about comics. This page is primarily for comic novices.

Register Page

-

Login Page

-

Search Page

- Here users will find a search bar and button. Users type in a keyword and can retrieve information based on these keywords. Comic names and grade can be searched.

- Results are displayed immediately and are in the same form that can be found on the Comics page to keep uniformity - the comic cover, name and price. Clicking on a comic here will redirect the user to the details page of that specific item.

### Features Left to Implement

## Information Architecture

SQLite3

- This database was used for testing purposes pre-deployment.

PostgreSQL

- On deployment, this database was used to host moels and store data.

### Data models

Comics app

IMAGE

## Technologies Used

### VSCode

On my local machine I used VSCode to add and edit my code. This enabled me to download my own necessary dependencies and packages. You can download VSCode for your machine on Visual Studio Code's website here <https://code.visualstudio.com/docs/setup/setup-overview>. You can add extensions to help with your project. Use its source control tab to commit and push changes to your local repository.

### Django

This web application framework is used to create the entire app and is written in Python. It is installed via pip3 install django(ADD VERSION) through your code editor. Once you add your project using django-admin startproject PROJECTNAME (dot), then you'll have access to Settings.py, URLs.py and other files. Then you can add apps, which are smaller self-contained components within the project.

### HTML5

HTML is the standard markup for web pages and stands for Hyper Text Markup Language. It is used to add and maintain structure for the content of information on web pages on the app. In conjunction with Bootstrap's grid system, the HTML supports all content on the site. The base.html page is created first by declaring its HTML5 structure using <!DOCTYPE html> and then addition elements, including head, title and body elements.

### Django's templating language

A template system is incorporated in this project. First, create your base.html and then in additonal pages add {% extends "base.html" %} to the top of the page. This means anything on the base.html page will display on the new page. The unique code is written between {% block content %} and {% endblock %} placeholders in each other page. Templating is very helpful when avoiding repeated coding structures and when displaying the navbar and footer on each page, for example.

### CSS3

Custom CSS and style attributes have been added via an external CSS stylesheet that is added to the head of the base.html file - CSS is rendered on each page that extends from the base.html page. While the CSS sheet contains most code, other styling attributes have been added inline using style tags in the HTML structure and for Bootstrap's inline spacing and color specifications.

### JavaScript

In this project JavaScript was used primarily for the Stripe set up, using an external stripe.js file which is the library that Stripe itself provides. It helps users on a store complete checkout and enables the developer to collect important and private payment information safely. More information on this can be found here <https://stripe.com/docs/stripe-js>. JavaScript was also copied from W3schools for the collapsible feature on the glossary page. And Bootstrap is dependent on JavaScript and its library, along with jQuery and Popper.js is added to the base.html page.

### jQuery

This was used to make some Bootstrap elements functional. For example, the collapsible navbar on mobile and its ability to be tapped into a dropdown was created visually with CSS, but only works because of the jQuery that is involved. The jQuery library is added to the head element.

### Bootstrap 4

This technology aides in the development of information structure on the page. This service provides well-designed, structured containers that require little additional modification. Aside from components on the page, Bootstrap is also used for its grid layout, which enables my app to be responsive on all devices. Its emphasis on spacing by padding and margin on the x and y axis has been employed inline throughout the html code per page: mx-auto for margin-right and margin-left automatic spacing, for example.

### Heroku

This platform is used to build, run and deploy the project and is hosting my project in production. It hosts the database used in project too, PostgreSQL. You need to create an app, set config variables and then deploy. See Heroku Deployment for more indepth information.

### SQLite3

This database, by default, comes with the Django package and is used primarily in development. Tables within the database are created using modelsa and using python3 manage.py makemigration and then migrate. In production this set up is mirrored in the new PostreSQL database.

### PostgreSQL

This is the database used in production. It can be accessed as an add-on feature in Heroku at multiple pricing brackets, including a free tier. Go to the Resources tab and in the add-on section, type in PostgreSQL to see options. Initialise the database by python3 manage.py makemigrations and migrate.

### Github

Github is my local repository. Here you can see the development of the code I've added, from the first file to the last. To start you initialise git by typing in 'git init' in your terminal and then you can add commit messages that when pushed to the repository can be viewed online. Its purpose is version control, to highlight the changes of the code during the project.

### Balsamiq

This technology is generally used at the start of a project, during the Skeleton Plane, to plot out the look of the app and its primary pages. In the formation of the project, it helps to visualise elements pre-coding but you can also use it to develop pages mid-project.

### Travis

This is a tool for continuous integration and testing. Its purpose is to test smaller chunks of code continously. After pushing changes to Github Travis will let you know if your code passes the requirements you've set. When Travis is synced up to Github repository you can see if your build passes or fails and then see your project's build history.

### Google Fonts

The font used on the site is Quicksand with font weights of 400, 500 and 700 to differentiate between different types of text - paragraph, heading and special text, for example. While it is possible to add additional weights and styles of this font, I used minimal specifications to keep my site loading quickly.

## Testing

### Continous Integration - Travis

From the beginning of this project, Continuous Integration - which means to test code in smaller chunks more often - was employed. In this project, Travis was used. To set this up, you'll need an account with Travis > connect it to the Github repository. Add a .travis.yml file to the root directory of your project, where language, version, requirements and script are specified - you'll also need a dummy SECRET_KEY. See below for an example:

![travis](/media/images/travis.png)

Then the first build takes place, which takes a few seconds as Travis tests all the code submitted. A build icon can be placed at the top of your README.md file, which is used to keep track of passing or failing code. When you click on the build icon you'll be redirected to the Travis website to see the build's code history.

## Deployment

### Running the project locally

This project was created, developed on run locally using a MacBook Air and VSCode as an IDE. To start the project, first create a workspace on your local machine and then open the folder on VSCode or an IDE of your choice. Add the README.md file as the first file and then create a .gitignore file in anticipation for the files that would need to be ignored for the project.

Following this, create a virtual environment using Python3 -m venv env and then activate it by opening a new terminal on your IDE. Next, install Django by using pip3 install Django==1.11.28 - or another version of your choice. Then add your project folder - in my case it's 'mycomicjumble' - in order to access the Settings.py file and additional files for the project.

Before initialising git and pushing to your local repositiory on Github, ensure that the SECRET_KEY contained in the Settings.py file has been added to an env.py file - this file stores all the environment variables needed throughout the project and makes sure important private inforamtion isn't pushed to Github. Then initialise git, add a commit message and then push everything to your online repository. For me, this is at Github - accessible here: <https://github.com/adonegan/milestone4-mycomicjumble>.

The project is now visible and accessible locally by using python3 manage.py runserver on your IDE. To exit the project, press Control-C, if using VSCode. Initialise the database and create tables within it by using python3 manage.py migrate. Following this, add a base.html page as a top level file for the project and when adding new apps (by using python3 manage.py startapp Home, for example) extend the base.html file to new pages.

### Heroku Deployment

Deploying to Heroku can take place at the start, in the middle or at the end of the project. I deployed my project to Heroku at the end of the project so I could focus on the build in development.

To deploy, create an app in your Heroku account. In the resources tab you can opt for a PostgreSQL database for the project - I chose the free one for this project. Selecting this database option pushed my Database URL to the config vars section in the Settings tab in Heroku.

Locally, use pip3 to install dj-database-url to your project - this is so the PostgreSQL database can be supported. In the Settings.py file comment out the SQLite database that comes with Django in favour of using Heroku's PostgreSQL database. Use this code: DATABASES = {'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))} and import dj_database_url at the top of the Settings.py file. In addition to this, insall psycopg2-binary==2.8.4 and gunicorn for Heroku deployment.

Add all keys and urls in the env.py file to the config vars section of the Settings tab within Heroku so they can be supported there. Use python3 manage.py makemigrations and python3 manage.py migrate to create tables in the database. Then create a superuser by using python3 manage.py createsuperuser - this is done again here (like the first time with the SQLite database) because PostgreSQL is the new database.

Static and Media files are served through Amazon Web Services S3 (see Technologies for more information on this) and once that is set up, use pip3 freeze --local > requirements.txt to ensure all dependencies are in place. After this, create the Procfile, which is needed for Heroku to determine what type of app it is (web: gunicorn mycomicjumble.wsgi:application is mine, for example).

When the Heroku app url is generated, add it - via an environment variable - to the ALLOWED_HOSTS section in the Settings.py file. When the project is complete, change Debug = False.

## Credits

- The text for the glossary page, in the Grades and Conditions sections, was copied from mycomicshop.com/help/grading <https://www.mycomicshop.com/help/grading> and modifed by me.

- The comic cover images were sourced on Marvels official website <marvel.com>, and Boom! Studio's official website <www.boom-studios.com>.

- The text beside comics on each details page was copied from marvel.com (for all Marvel comics), from Boom! Studios and buffy.fandom.com/wiki (for Buffy and Angel comics).

- Text on the Privacy Policy page was generated from <https://www.privacypolicygenerator.info/>. Likewise, text on the Terms & Conditions page is from <https://www.termsandconditionsgenerator.com/>.
