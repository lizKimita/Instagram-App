# Instagram

#### This is a clone of Instagram, 18/05/2019

#### By **Elizabeth Wanjiku Kimita**

## Description
This site is a clone of the original Instagram application. Users can sign up, log in, upload pictures, view other users post, comment and like their photos and even follow the users they like. Users can also navigate to their profiles to view all their posts and can search for other users using their usernames.

## BDD Specifications
| User Requirements             | Input                                                                                                                         | Output                                                                                             |
|-------------------------------|-------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| Sign up/Login                 | To create a new account click the sign up link and fill the form details To login click the login button and fill the details | If login is successful user is navigated to the home page                                          |
| To add a new post             | click the profile icon and then the create new post link                                                                      | You will be navigated to a page where you can create a new post                                    |
| To Comment on a post          | User the comments section at the bottom of each post and submit                                                               | Comment will be added to the post's comments section                                               |
| To create a profile           | On the navbar click the profile tab and create new profile                                                                    | New profile for the user will be created                                                           |
| To edit profile               | On the profile page click the edit profile button, make the changes and submit                                                | Profile will be edited                                                                             |
| To see all of your posts      | Navigate to the profile page and all the details and posts will be displayed.                                                 | All the user's profile details will be displayed.                                                  |
| To search for a specific user | input the user's username in the search bar on the navigation bar                                                             | You will be directed to the user with a matching username. click on the user to see their details. |
| To view other all posts       | Navigate to the home page to view posts from the users you follow                                                             | All posts will be displayed                                                                        |
| To log out                    | click the profile icon and then the logout link                                                                               | You will be logged out                                                                             |


## Setup/Installation Requirements
* Ensure you have Installed Python3.6
* Clone the Instagram Repository
* Create and Activate your virtual environment - `python3.6 -m venv --without-pip virtual` && `source virtual/bin/activate`
* Install dependencies - `pip install -r requirements.txt`
* Create a Database - `psql` then `CREATE DATABASE database name`
* Run Migrations - `python3.6 manage.py makemigrations database name` then `python3.6 manage.py migrate`
* Run the App - `python3.6 manage.py runserver`
* Application should open on `localhost:8000` 

## Known Bugs
The comment, follow and like functionalities are not functioning properly yet.

## Technologies Used
* Python 3.6
* Bootstrap
* Heroku
* HTML
* CSS
* Django

## Support and contact details
For more information, questions, or help using the program, get in touch with me on +254 726 047102 or email: kimita.wanjiku@gmail.com.

### License
MIT
Copyright (c) 2019 **Elizabeth Wanjiku Kimita**
  