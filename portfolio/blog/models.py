from django.db import models

class ContactMeTable(models.Model):
    name = models.CharField(max_length = 20)
    email = models.EmailField()
    info = models.TextField(max_length = 500)


