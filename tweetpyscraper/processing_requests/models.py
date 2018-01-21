from django.db import models


class ProcessingRequest(models.Model):
    """ Model to save user processing requests """
    keyword = models.CharField(max_length=255)
    processed = models.BooleanField(default=False)

    @classmethod
    def create_processing_requests(cls, query):
        
        # Importing here to avoid circular dependency
        from .documents import ProcessingRequestDocument

        search = ProcessingRequestDocument.search().filter('match', keyword=query)
        # If there isn't any PR for this keyword the add it
        if  search.count() == 0:
            cls.objects.create(keyword=query)