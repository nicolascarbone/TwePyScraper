from rest_framework import viewsets
from rest_framework.response import Response

from taskrunner.tasks import scrape

from .models import Scrape


class ScraperViewSet(viewsets.ModelViewSet):
    """Scrape user profiles.

    Here you can run the scrape with an specific criteria search
    and not though a processing request    
    """
    queryset = Scrape.objects.all()

    def scrape(self, request):
        query = request.POST.get('query')
        if query is not None:
            scrape.delay(query)

        return Response('running scraper with query = {}'.format(query))