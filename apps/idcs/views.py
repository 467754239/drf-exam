
# 标准模块
import json

# 自定义模块
from .models import Idc
from .serializers import IdcSerializer
from apps.utils import JsonApiResponse

# 第三方package
from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse, JsonResponse
from django.core import serializers

from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, mixins


# Create your views here.

####################### 函数视图(1) ######################################

def idc_list(request, *args, **kwargs):

    if request.method == "GET":
        queryset = Idc.objects.all()
        s = IdcSerializer(queryset, many=True)
        # content = JSONRenderer().render(s.data)
        # return HttpResponse(content, content_type="application/json")
        return JsonApiResponse(s.data)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        s = IdcSerializer(data=data)
        if s.is_valid():
            s.save()
            # content = JSONRenderer().render(s.data)
            # return HttpResponse(content, content_type="application/json")
            return JsonApiResponse(s.data)
        return HttpResponse("Raise a unknow except.")


def idc_detail(request, pk, *args, **kwargs):

    try:
        obj = Idc.objects.get(pk=pk)
    except Idc.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        s = IdcSerializer(obj)
        return JsonApiResponse(s.data)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        s = IdcSerializer(obj, data=data)  # 全部字段修改
        # s = IdcSerializer(Idc, data={'name': u'idc3'}, partial=True)  # 部分字段修改
        if s.is_valid():
            s.save()
            return JsonApiResponse(s.data)
        else:
            return JsonApiResponse(s.errors, status=400)

    elif request.method == "DELETE":
        obj.delete()
        return HttpResponse("", status=204)


####################### 装饰器 函数视图(2) ######################################

@api_view(['GET', 'POST'])
def idc_list_v2(request, format=None, *args, **kwargs):

    if request.method == "GET":
        queryset = Idc.objects.all()
        s = IdcSerializer(queryset, many=True)
        return JsonApiResponse(s.data)

    elif request.method == "POST":
        s = IdcSerializer(data=request.data)
        if s.is_valid():
            s.save()
            return JsonApiResponse(s.data, status=status.HTTP_201_CREATED)
        return JsonApiResponse(s.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def idc_detail_v2(request, pk, format=None, *args, **kwargs):

    try:
        obj = Idc.objects.get(pk=pk)
    except Idc.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        s = IdcSerializer(obj)
        return Response(s.data, status=status.HTTP_200_OK)

    elif request.method == "PUT":
        s = IdcSerializer(obj, data=request.data)  # 全部字段修改
        # s = IdcSerializer(Idc, data={'name': u'idc3'}, partial=True)  # 部分字段修改
        if s.is_valid():
            s.save()
            return Response(s.data)
        else:
            return Response(s.errors, status=status.HTTP_404_NOT_FOUND)

    elif request.method == "DELETE":
        obj.delete()
        return HttpResponse("", status=status.HTTP_204_NO_CONTENT)


####################### 类视图(3) ######################################

class IdcList(APIView):

    def get(self, request, format=None):
        queryset = Idc.objects.all()
        s = IdcSerializer(queryset, many=True)
        return Response(s.data)

    def post(self, request, format=None):
        s = IdcSerializer(data=request.data)
        if s.is_valid():
            s.save()
            return JsonApiResponse(s.data, status=status.HTTP_201_CREATED)
        return JsonApiResponse(s.data, status=status.HTTP_400_BAD_REQUEST)

class IdcDetail(APIView):

    def get_object(self, pk):
        try:
            return Idc.objects.get(pk=pk)
        except Idc.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        obj = self.get_object(pk)
        s = IdcSerializer(obj)
        return Response(s.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        obj = self.get_object(pk)
        s = IdcSerializer(obj, data=request.data)  # 全部字段修改
        # s = IdcSerializer(Idc, data={'name': u'idc3'}, partial=True)  # 部分字段修改
        if s.is_valid():
            s.save()
            return Response(s.data)
        else:
            return Response(s.errors, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        obj = self.get_object(pk)
        obj.delete()
        return HttpResponse("", status=status.HTTP_204_NO_CONTENT)


####################### 混合视图(4) ######################################

class IdcListV4(GenericAPIView,
                mixins.ListModelMixin,
                mixins.CreateModelMixin):
    queryset = Idc.objects.all()
    serializer_class = IdcSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class IdcDetailV4(GenericAPIView,
                mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin):
    queryset = Idc.objects.all()
    serializer_class = IdcSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


####################### 混合视图(5) ######################################
class IdcListV5(ListCreateAPIView):
    queryset = Idc.objects.all()
    serializer_class = IdcSerializer


class IdcDetailV5(RetrieveUpdateDestroyAPIView):
    queryset = Idc.objects.all()
    serializer_class = IdcSerializer

####################### 视图集(6) ######################################

class IdcListViewset(GenericViewSet,
                mixins.ListModelMixin,
                mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,
                mixins.CreateModelMixin):
    queryset = Idc.objects.all()
    serializer_class = IdcSerializer

####################### 视图集(7) ######################################
class IdcListViewsetV7(ModelViewSet):
    queryset = Idc.objects.all()
    serializer_class = IdcSerializer
