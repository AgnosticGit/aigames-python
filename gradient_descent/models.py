from sympy import symbols, sympify, diff, lambdify
from django.db import models


class GradientDescent2D(models.Model):
    point_x = models.FloatField(null=True)
    point_y = models.FloatField(null=True)

    points = models.JSONField(null=False, default=dict)

    math_expression = models.CharField(max_length=20, null=True)
    delta = models.FloatField(default=0.1)

    def fill_points_list(self, points: int):
        exp = sympify(self.math_expression)
        x = symbols('x')

        new_points = {'points_x': [], 'points_y': []}

        for number in range(-points, points + 1):
            result = exp.subs(x, number)
            new_points['points_y'].append(float(result))
            new_points['points_x'].append(float(number))

        self.points = new_points

    def fill_point_y_by_expression(self):
        if self.point_x is not None:
            exp = sympify(self.math_expression)
            x = symbols('x')
            result = exp.subs(x, self.point_x)
            self.point_y = float(result)

    def get_gradient(self):
        exp = sympify(self.math_expression)
        x = symbols('x')
        derivative_exp = diff(exp, x)
        f = lambdify(x, derivative_exp)
        gradient = f(self.point_x)

        return gradient
