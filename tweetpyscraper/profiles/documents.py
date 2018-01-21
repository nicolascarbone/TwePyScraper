from django_elasticsearch_dsl import DocType, Index

from .models import Profile

# Name of the Elasticsearch index
profile = Index('profiles')

profile.settings(
    number_of_shards=1,
    number_of_replicas=0
)


@profile.doc_type
class ProfileDocument(DocType):
    """ Document definition for Profile model index """

    class Meta:
        model = Profile
        # Fields to index using elastic search
        fields = [
            'name',
            'image',
            'short_description',
            'popularity_index',
        ]
