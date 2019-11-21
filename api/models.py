from django.db import models

# Create your models here.
class Question(models.Model):
    body = models.CharField(blank=False, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at', 'body']

    # def __str__(self):
    #     return '%s' % (self.body)