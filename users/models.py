from django.db import models

class User(models.Model):
    ip = models.TextField()
    perceptron_id = models.IntegerField(null=True)

    def __str__(self):
        return self.ip