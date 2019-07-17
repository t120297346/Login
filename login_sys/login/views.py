from django.shortcuts import render, get_object_or_404
from login.models import User
from login.serializers import UserSerializer
from login.models import fun_raw_sql_query, fun_sql_cursor_update

from rest_framework import viewsets, status
from rest_framework.decorators import list_route, detail_route
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser
# Create your views here.

class LoginViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    #parser_classes = (JSONParser,) # 限定接收JSON
    
    @list_route(methods = ['get'])
    def raw_sql_query(self, request):
        name = request.query_params.get('name', None)
        user = fun_raw_sql_query(name = name)
        serializer = UserSerializer(user, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    @detail_route(methods = ['put'])
    def sql_cursor_update(self, request, pk = None):
        name = request.data.get('name', None)
        if name:
            user = fun_sql_cursor_update(name = name, pk = pk)
            return Response(user, status = status.HTTP_200_OK)
    
    @detail_route(methods = ['get'])
    def detail(self, request, pk = None):
        user = get_object_or_404(User, pk = pk)
        result = {
            'name': user.name,
            'password': user.password,
            'email': user.email,
            'c_time': user.c_time,
        }
        return Response(result, status = status.HTTP_200_OK)
    
    @list_route(methods = ['get'])
    def all_user(self, request):
        user = User.objects.values_list('name', flat = True)
        return Response(user, status = status.HTTP_200_OK)        
        
        