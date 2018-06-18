from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

# Create your views here.

@api_view(['GET'])
def api_root(request, format=None, *args, **kwargs):
    return Response({
        '/api/v1/idcs/' : reverse("idc_list", request=request, format=format)
    })