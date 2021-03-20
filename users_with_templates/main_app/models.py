from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=75)
    email = models.CharField(max_length=100)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return f"User | {self.name} | {self.email} | {self.age}"