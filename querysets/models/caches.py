from django.db import models

class CacheUser(models.Model):
    email = models.EmailField(max_length=20)
    password = models.CharField(max_length=500)
    
    class Meta:
        db_table = 'cache_users'