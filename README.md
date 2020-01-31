# LMS
In this app there are multiple libraries. In each library there are multiple librarians and books. So basically a member can borrow a book from the library only if he is a member.

###Functionalities and assumptions:

Book is issued by the librarian and then has to be returned within a due date of 7 days.
If at all he doesn't return the book on or before the due date he is going to pay the fine as assigned by the library standards.
I have implemented the concept of #####post_save so that as soon the book is returned and the book is shown available for the upcoming booking members.
A member can borrow only limited books from the library.
To run this in your system:

Clone this repo in your system:

git clone https://github.com/SaneeyaIqbal/Library-Management-System.git
Get inside the repo, type this is terminal:

cd library
Create a virtual environment inside the repo:

python3 -m venv .library
After that activate the virtual environment by typing:

source .library/bin/activate
Next step is to install all the dependencies into your virtual environment:

pip3 install 
Django==3.0.1
django-jsonfield==1.4.0
Next get into the project directory by typing:

cd lms
Type 3 commands in order before for the project to run:

python3 manage.py makemigrations
python3 manage.py migrate
Now to access the admin page before running the server create a superuser:

python3 manage.py createsuperuser
fill the details :
username: <ur choice>
email: <optional>
password: <password>
confirm password: <confirm the password>
After filling all these to run the project:

python3 manage.py runserver
This is just the admin page functionality project.

I hope this project was bit beneficial for you references.
