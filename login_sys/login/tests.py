from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIClient

from login.models import User as Users
# Create your tests here.
class UserViewTestCase(APITestCase):
    url_reverse = reverse('api:user-list')
    url = '/api/login/'
    url_detail = '/api/login/{}/'
    url_detail_route_reverse = reverse('api:user-detail', kwargs = {"pk" : 1})
    url_detail_route = '/api/login/{}/detail/'
    url_list_route = '/api/login/all_user/'
    
    def setUp(self):
        print('setUp')
        
        self.cilent = APIClient()
        User.objects.create_user(username = 'test_user', password = 'password123')
        
        self.cilent.login(username = 'test_user', password = 'password123')
        
        self.request_data = {
            'name': 'b05611018',
            'password': 'm9031314',
            'email': 't120297346@gmail.com',
        }
        self.user = Users.objects.create(user = 'user_test', password = 'password_test', email = 'email_test')
    
    def test_api_music_create(self):
        print('test_api_music_create')
        self.response = self.cilent.post(
                self.urls,
                self.request_data,
                format = "json",
            )
    