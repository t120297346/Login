from django.shortcuts import render
from login.models import User
from login.serializers import UserSerializer
from login.models import fun_raw_sql_query

from rest_framework import viewsets, status
from rest_framework.decorators import list_route
from rest_framework.response import Response
# Create your views here.

class LoginViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    @list_route(methods = ['get'])
    def raw_sql_query(self, request):
        name = request.query_params.get('name', None)
        user = fun_raw_sql_query(name = name)
        serializer = UserSerializer(user, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)
        
        