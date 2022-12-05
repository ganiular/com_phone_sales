from django.db import models

# Create your models here.
class Member(models.Model):
    last_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    other_name = models.CharField(max_length=20, default='')
    reg_number = models.CharField(max_length=16)

    def __str__(self) -> str:
        return self.first_name
