from django.db import models



class Profile(models.Model):
    """"""
    name = models.CharField(max_length=100)
    image = models.URLField(max_length=100)
    popularity_index = models.IntegerField(default=0)
    short_description = models.CharField(max_length=255)

    @classmethod
    def search_index(cls, query):
        """ Search for query in index.
        
        Return Document for request query search
        Query is a string, can be splitted into several keywords
        """
        from .documents import ProfileDocument

        keywords = [keyword.lower() for keyword in query.split(' ')]
        search = ProfileDocument.search().query('terms', name=keywords) \
                .query('terms', short_description=keywords)

        return search
