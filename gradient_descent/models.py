from django.db import models

from gradient_descent.numeric_string_parser import NumericStringParser


class GradientDescent2D(models.Model):
    initial_point_x = models.FloatField(null=True)
    points = models.JSONField(null=False, default=dict)

    math_expression = models.CharField(max_length=20, null=True)
    delta = models.FloatField(default=0.1)

    def fill_points_list(self, points: int):
        nsp = NumericStringParser()

        new_points = {'points_x': [], 'points_y': []}

        for x in range(-points, points + 1):
            math_expression = nsp.replace_x(self.math_expression, x)
            print(math_expression)
            function_result = nsp.eval(math_expression)
            new_points['points_y'].append(function_result)
            new_points['points_x'].append(x)

        self.points = new_points
