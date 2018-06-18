


from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer


class JsonApiResponse(HttpResponse):

    def __init__(self, data, **kwargs):
        kwargs.setdefault('content_type', 'application/json')
        content = JSONRenderer().render(data)
        super(JsonApiResponse, self).__init__(content=content, **kwargs)