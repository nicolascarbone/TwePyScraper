# System level dependencies
Elasticsearch >=5.0,<6.0

# Install packages
pip install -r requirements.txt

# Build the index
python manage.py search_index --rebuild -f

# Run server
python manage.py runserver

# Run celery worker
celery -A tweetpyscraper worker -l info

# Stack

Django
Elastic Search
Django Rest Framework
Celery

# Considerations
Profiles are indexed using Elastic Search due to the size of the table can 
potencially grow, we need to respond as soon as possible to the user request

# Flow

http://localhost:8000/api/profiles/?query=<profile query>

If there isn't any result for the entered criteria, then a Processing Request will be created
i.e Ritchie Kotzen
if there isn't any profile that matches that criteria, a record will be stored for it in the 
Processing Request model

http://localhost:8000/api/run-task/processing-requests/

It will run a scraper task with the processing request keywords
i.e It will search for profiles that matches Ritchie Kotzen 

http://localhost:8000/api/run-task/scrape/

This task scrapes for an specific keyword passed in as parameter and it will pdate the index after the operation has finished

# Missing things
Write tests for views and tasks

Due to the system level requeriments, it may be better to create a docker container to hold the project

Versioning
Due that I'm using django, versioning will go through git tags
I won't use setup.py for that purpose