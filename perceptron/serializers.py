from rest_framework import serializers
from perceptron.models import Perceptron

class PerceptronSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perceptron
        fields = ['id', 'w0', 'w1', 'input1', 'input2', 'epoches', 'learning_rate']