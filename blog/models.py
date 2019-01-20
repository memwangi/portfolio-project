from django.db import models

class Blog(models.Model):
    author = models.TextField(max_length=50,null=False)
    post = models.TextField(null=False)
    date_posted = models.TimeField(auto_now_add=True)

