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

VSCode

- On my local machine I used VSCode to add and edit my code. This enabled me to download my own necessary dependencies.

Django

- This web application framework was used to create the entire app using programming language Python.

Python

HTML5

- HTML was used to add and maintain structure for the pages on the app. In conjunction with Bootstrap's grid system, the HTML supports all content on the site.

Jinja

CSS3

JavaScript

jQuery

- This was used to make some Bootstrap elements functional. For example, the collapsible navbar on mobile and its ability to be tapped into a dropdown.

Bootstrap

- This technology added structured and well-designed content from the box. Primilary used for its grid layout, this technology enable my app to be responsive.

Heroku

SQLite3

PostgreSQL

Github

Balsamiq

- This technology was used at the start of the project, during the Skeleton Plane, to plot out the look of the web page.

Travis

Google Fonts

- The main font used on the site is Quicksand with font weights of 400, 500 and 700.

## Testing

### Continous Integration

From the beginning of this project, Continuous Integration - which means to test code in smaller chunks more often - was employed. In this project, Travis was used. To set this up, you'll need an account with Travis > connect it to the Github repository. Add a .yml file to the root directory of your project, where language, version, requirements and script are specified. Then the first build takes place, which takes a few seconds as Travis tests all the code submitted. A build icon is placed at the top of this README.md file and is used to keep track of passing or failing code.
