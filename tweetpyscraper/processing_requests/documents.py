from django_elasticsearch_dsl import DocType, Index

from .models import ProcessingRequest

# Name of the Elasticsearch index
procesing_requests = Index('processing_requests')

procesing_requests.settings(
    number_of_shards=1,
    number_of_replicas=0
)


@procesing_requests.doc_type
class ProcessingRequestDocument(DocType):
    """ Document definition for procesing_requests model index """

    class Meta:
        model = ProcessingRequest
        # Fields to index using elastic search
        fields = [
            'id',
            'keyword',
            'processed'
        ]
