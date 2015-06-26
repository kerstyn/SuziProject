from django.db import models
from django.utils import timezone


# question or statement posed by user
class Question(models.Model):
    author = models.ForeignKey('auth.User')
    question = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.question