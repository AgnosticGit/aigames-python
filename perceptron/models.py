from django.db import models


class Perceptron(models.Model):
    w0 = models.FloatField()
    w1 = models.FloatField()

    input1 = models.IntegerField()
    input2 = models.IntegerField()

    epoches = models.IntegerField()
    learning_rate = models.IntegerField()

