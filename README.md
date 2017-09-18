# photo_gallery
A simple Django photo gallery app
<hr>

## how to run the app
1. Unzip the file to a directory, let's call it /directory/

2. Open a console or a command line and type:

* cd /directory/photo_gallery-master (change directory into the project's root)

* $ python manage.py migrate (create your sqlite database schema)

* $ python manage.py createsuperuser (create a user for the admin site)

* $ python manage.py runserver 8090 (run the server on localhost:8090)

3. Visit http:\\localhost:8090\gallery to view the gallery

4. Visit http:\\localhost:8090\admin to add photos

<hr>

## video explanation for those who like to see how it's working

<a href="https://www.youtube.com/watch?v=nL426ABeFw0" 
target="_blank"><img src="http://img.youtube.com/vi/nL426ABeFw0/0.jpg" 
alt="Django photogallery app" width="240" height="180" border="10" /></a>