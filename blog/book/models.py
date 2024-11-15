from django.db import models

# Create your models here.
class Membership(models.Model):
    member_name= models.CharField(max_length=50)
    membership_type=  models.CharField(max_length=50)
    join_date= models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.join_date