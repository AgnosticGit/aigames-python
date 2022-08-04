import json
from perceptron.serializers import DrinkSerializer
from .models import Perceptron
from django.http import JsonResponse


def load_perceptron(request):
    perceptrons = Perceptron.objects.all()
    serialized = DrinkSerializer(perceptrons, many=True)
    
    return JsonResponse(serialized.data, content_type="application/json", safe=False)
