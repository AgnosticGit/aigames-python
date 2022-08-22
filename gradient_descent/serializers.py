from rest_framework import serializers

from gradient_descent.models import GradientDescent2D
from perceptron.models import Perceptron


class GradientDescent2DSerializer(serializers.ModelSerializer):
    class Meta:
        model = GradientDescent2D
        fields = ['initial_point_x', 'points_list_x', 'math_function', 'delta']
