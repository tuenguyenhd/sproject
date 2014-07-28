from django.db import models


class Contact(models.Model):    
        
    name = models.CharField(
        max_length=255,
    )
    password = models.CharField(
        max_length=255,
    )
    phone_number = models.CharField(
        max_length=100,
    )
    price = models.IntegerField(default=0)            
    birth = models.IntegerField(default=0)    
    region = models.CharField(
        max_length=255,
    )
    description = models.CharField(
        max_length=255,
    )    
    last_review_time = models.DateTimeField(null=True)    
    rate = models.IntegerField(default=0)    
    work_name = models.CharField(
        max_length=255,
    )    
    face = models.IntegerField(default=0)    
    v1 = models.IntegerField(default=0)    
    v2 = models.IntegerField(default=0)    
    v3 = models.IntegerField(default=0)    
    service = models.IntegerField(default=0)            
    
    def __str__(self):

        return ' '.join([
            self.name,
            self.password,
        ])
