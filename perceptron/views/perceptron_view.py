import json
from perceptron.models import Perceptron
from perceptron.serializers import PerceptronSerializer
from django.http import JsonResponse


def load_perceptron(request):
    perceptrons = Perceptron.objects.all()
    serialized = PerceptronSerializer(perceptrons, many=True)

    return JsonResponse(serialized.data, safe=False)
