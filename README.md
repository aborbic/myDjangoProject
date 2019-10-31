# myDjangoProject
This is a web application I plan to deploy that helps colleagues from my student organization stay in touch. It features an announcements page, a home page, a page to upload pictures that we take over the years and finally a page for potential members to schedule interviews with the active chapter.

## Prerequisites
* [Python](https://www.python.org/downloads/release/python-374/)
* [Pip](https://pip.pypa.io/en/stable/installing/)
* [Django](https://www.djangoproject.com/download/)
* [Pillow](https://pillow.readthedocs.io/en/stable/installation.html)

## Installing
```
python get-pip.py
pip install Django
pip install Pillow
```
## Initialize your database.
* python manage.py syncdb
* python manage.py migrate

## Setup 
* Git clone <repository-url>
* Open in your IDE of choice

To use admin page, you need to register. In command line type:
* python ./manage.py createsuperuser
* enter email
* enter desired username
* enter desired password

## Running
* python manage.py runserver

## Useful Links
* [Django_Help](https://docs.djangoproject.com/en/2.2/)

## Contributing
If you want to contriute, submit a pull request please. 

## Versioning 
Current Version is 1.0.0

## Authors
Christian Aborbie - Main author and contributor
See also the list of contributors who participated in this project.

## License 
This project is licensed under the MIT License - see the LICENSE.md file for details
