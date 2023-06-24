from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *


class Welcome(APIView):
    def get(self, request):
        name = Name.objects.all()
        name_serialize = NameSerializer(name, many=True)
        return Response(name_serialize.data)


class NameId(APIView):
    def get(self, request, id):
        name = Name.objects.get(id=id)
        name_serialize = NameSerializer(name)
        return Response(name_serialize.data)
