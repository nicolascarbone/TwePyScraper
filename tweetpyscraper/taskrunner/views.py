import json

from rest_framework import viewsets
from rest_framework.response import Response

from .tasks import processing_requests, scrape, rebuild_index
from .models import TaskRunner


class TaskRunnerViewSet(viewsets.ModelViewSet):
    queryset = TaskRunner.objects.all()

    def rebuild_index(self, request):
        rebuild_index.delay()
        return Response('Task ran succesfully')

    def processing_requests(self, request):
        processing_requests.delay()
        return Response('Task ran succesfully')

    def scrape(self, request):
        query = request.POST.get('query')
        if query is not None:
            scrape.delay(query)
        return Response('Task ran succesfully')