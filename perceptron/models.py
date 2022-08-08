from django.db import models


class Perceptron(models.Model):
    w0 = models.FloatField(default=0.5)
    w1 = models.FloatField(default=0.7)

    input1 = models.IntegerField(null=True)
    input2 = models.IntegerField(null=True)

    epoches = models.IntegerField(default=1)
    learning_rate = models.IntegerField(default=0.1)
