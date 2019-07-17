from django.utils.timezone import now
from rest_framework import serializers
from login.models import User

class UserSerializer(serializers.ModelSerializer):
    
    day_since_created = serializers.SerializerMethodField()
    #SerializerMethodField(method_name=''), if no included this defaults to get_<field_name>
    
    class Meta:
        model = User
        #fields = '__all__'
        fields =['id', 'name', 'password', 'email', 'c_time', 'created', 'day_since_created']
    
    def get_day_since_created(self, obj):
        return (now() - obj.created).days
        
class UserSerializerV1(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'password', 'email')