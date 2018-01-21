import json

from rest_framework import viewsets
from rest_framework.response import Response

from processing_requests.models import ProcessingRequest

from .models import Profile 
from .serializers import ProfileSerializer


class ProfilesViewSet(viewsets.ModelViewSet):
    """ ViewSet for Twitter Profiles """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def list(self, request):
        """ Search for profiles using passed in arguments if needed """
        query = request.GET.get('query', None)

        if query is not None:
            search = Profile.search_index(query)
                            
        serializer = self.get_serializer(search, many=True)

        # Search did not get any result, create a processing request
        if not serializer.data:
            ProcessingRequest.create_processing_requests(query)

        return Response(serializer.data or 'Processing Request')