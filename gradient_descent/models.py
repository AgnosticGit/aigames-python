from django.db import models

from gradient_descent.numeric_string_parser import NumericStringParser


class GradientDescent2D(models.Model):
    point_x = models.FloatField(null=True)
    point_y = models.FloatField(null=True)

    points = models.JSONField(null=False, default=dict)

    math_expression = models.CharField(max_length=20, null=True)
    delta = models.FloatField(default=0.1)

    def fill_points_list(self, points: int):
        nsp = NumericStringParser()

        new_points = {'points_x': [], 'points_y': []}

        for x in range(-points, points + 1):
            math_expression = nsp.replace_x(self.math_expression, x)
            function_result = nsp.eval(math_expression)
            new_points['points_y'].append(function_result)
            new_points['points_x'].append(x)

        self.points = new_points

    def fill_point_y_by_expression(self):
        if self.point_x is not None:
            nsp = NumericStringParser()
            math_expression = nsp.replace_x(self.math_expression, self.point_x)
            function_result = nsp.eval(math_expression)
            self.point_y = function_result
