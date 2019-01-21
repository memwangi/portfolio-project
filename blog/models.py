from django.db import models

class Blog(models.Model):
    post_image = models.ImageField(upload_to='images/')
    post = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=150)

