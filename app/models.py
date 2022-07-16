from django.db import models
from django.contrib.auth.models import User, auth

# Create your models here.
class Todo(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, unique=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["complete"]

    def __str__(self):
        return self.title
