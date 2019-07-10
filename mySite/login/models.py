from django.db import models

# Create your models here.
class User(models.Model):
     
    gender = (
        ('male', 'male'),
        ('female', 'female'),
    )

    name = models.CharField(max_length = 100, unique = True, verbose_name = '用戶名')
    password = models.CharField(max_length = 256, verbose_name = 'password')
    email = models.EmailField(unique = True, verbose_name = 'email')
    sex = models.CharField(choices = gender, max_length = 32, default = 'mail', verbose_name = 'gender')
    c_time = models.DateTimeField(auto_now_add = True, verbose_name = 'create time')
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-c_time'] #反向時間排序
        verbose_name = 'username'
        verbose_name_plural = 'usernames'