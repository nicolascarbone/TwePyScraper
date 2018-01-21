from __future__ import absolute_import, unicode_literals

import tweepy

from django.conf import settings
from django.core.management import call_command

from celery import task

from profiles.models import Profile

from processing_requests.models import ProcessingRequest
from processing_requests.documents import ProcessingRequestDocument

@task
def processing_requests():
    requests = ProcessingRequestDocument.search().filter('match', processed=False)
    processed = []
    for request in requests:
        processed.append(request.id)
        scrape.delay(request.keyword)
        # Save record so signals are fired, this is needed 
        # to keep our index consistent
        record = ProcessingRequest.objects.get(id=request.id)
        record.processed = True
        record.save()

    # This is what I'd expect to do, but signals are not fired because .update does 
    # not call to .save, so the index remains out of date
    # ProcessingRequest.objects.filter(id__in=processed).update(processed=True)

@task
def rebuild_index():
    call_command('search_index', '--rebuild', '-f')

@task
def scrape(query):
    profiles = settings.TWITTER_API.search_users(q=query, per_page=10, show_user=True)

    bulk = []
    for profile in profiles:
        formatted = {
            'name': profile['name'],
            'short_description': profile['description'],
            'popularity_index': profile['followers_count'],
            'image': profile['profile_image_url']
        }
        bulk.append(Profile(**formatted))

    Profile.objects.bulk_create(bulk)

    # Rebuild index to be able to search for this new data
    rebuild_index()

    return query