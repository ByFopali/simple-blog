from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'article'

    def __str__(self):
        return self.title
