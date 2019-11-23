annotate-world
==========

A simple Django app (not yet functional) to let users store information about cities and locations on a map of the world.

To run the backend make sure you have Django (2.x.x) and python (3.x.x) installed
and execute the follow command::

    $ sudo pip install -r requirements.txt

Followed by::

    $ python3 manage.py migrate

    $ python3 manage.py runserver

And open the following URL in your web browser:

 - http://127.0.0.1:8000/

To test out continent and country creation you can use:

 curl -X POST -d 'name=Asia&latitude_center=10.0&longitude_center=13.0' http://127.0.0.1:8000/createContinent

 followed by

 curl -X POST -d 'name=Japan&latitude_center=12.0&longitude_center=44.0&continent_id=1' http://127.0.0.1:8000/createCountry


To test the UI navigate to /frontend/ and run:

    $ npm install

    $ npm start

And open the following URL in your web browser:

 - http://127.0.0.1:3000/
