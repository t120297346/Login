from django.db import models
from collections import namedtuple

from django.db import connection
# Create your models here.
class User(models.Model):
    
    name = models.CharField(max_length = 128, unique = True, verbose_name = 'user')
    password = models.CharField(max_length = 256, verbose_name = 'password')
    email = models.EmailField(unique = True, verbose_name = 'email')
    c_time = models.DateTimeField(auto_now = True, verbose_name = 'create time')
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-c_time']
        verbose_name = 'user'
        verbose_name_plural = 'users'
        db_table = "login"
        app_label = "login"
        
def fun_raw_sql_query(**kwargs):
    name = kwargs.get('name')
    
    if name:
        result = User.object.raw('SELECT * FROM user WHERE name = %s', [name])
    else:
        result = User.object.raw('SELECT * FROM user')
    
    return result
    