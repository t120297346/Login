from django.db import models
from collections import namedtuple

from django.db import connection
# Create your models here.
class User(models.Model):
    
    name = models.CharField(max_length = 128, unique = True, verbose_name = 'user')
    password = models.CharField(max_length = 256, verbose_name = 'password')
    email = models.EmailField(unique = True, verbose_name = 'email')
    c_time = models.DateTimeField(auto_now = True, verbose_name = 'create time')
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "login"
        app_label = "login"

        
def fun_raw_sql_query(**kwargs):
    name = kwargs.get('name')
    
    if name:
        result = User.objects.raw('SELECT * FROM login WHERE name = %s', [name])
    else:
        result = User.objects.raw('SELECT * FROM login')
    return result

def namedtuplefetchall(cursor):
    # Return all rows from a cursor as a nametuple
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

def fun_sql_cursor_update(**kwargs):
    name = kwargs.get('name')
    pk = kwargs.get('pk')
    '''
    Note that if you want to include literal percent signs in the query, 
    you have to double them in the case you are passing parameters:
    '''
    with connection.cursor() as cursor:
        cursor.execute("UPDATE login SET name = %s WHERE id = %s", [name, pk])
        cursor.execute("SELECT * FROM login WHERE id = %s", [pk])
        result = namedtuplefetchall(cursor)
    result = [
        {
            'id': r.id,
            'name': r.name,
            'password': r.password,
            'email': r.email,
        }
        for r in result
    ]
    
    return result
    
    