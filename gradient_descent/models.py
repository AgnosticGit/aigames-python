from django.db import models


class GradientDescent2D(models.Model):
    initial_point_x = models.FloatField(null=True)
    points_list_x = models.TextField(null=True)

    math_function = models.CharField(max_length=20, null=True)
    delta = models.FloatField(default=0.1)
