from django.db import models


class Perceptron(models.Model):
    w0 = models.FloatField(default=0.1)
    w1 = models.FloatField(default=0.2)

    input1 = models.IntegerField(default=0)
    input2 = models.IntegerField(default=0)

    epoches = models.IntegerField(default=1)
    learning_rate = models.FloatField(default=0.1)

    output = models.IntegerField(null=True)
