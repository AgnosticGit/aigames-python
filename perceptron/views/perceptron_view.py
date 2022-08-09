from perceptron.artificial_perceptron import ArtificialPerceptron
from perceptron.models import Perceptron
from perceptron.serializers import PerceptronSerializer
from django.http import JsonResponse
from users.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
import numpy as np


def load_perceptron(request):
    ip = request.META.get("REMOTE_ADDR")
    user = User.objects.filter(ip=ip).first()

    if user is None:
        create_user(ip)

    user = User.objects.filter(ip=ip).first()

    perceptron_id = user.perceptron_id

    if perceptron_id == None:
        new_perceptron = create_perceptron()
        user.perceptron_id = new_perceptron.id
        user.save()

        serialized = PerceptronSerializer(new_perceptron)

        return JsonResponse({'data': serialized.data}, safe=False)

    old_perceptron = Perceptron.objects.get(pk=perceptron_id)
    old_serialized = PerceptronSerializer(old_perceptron)

    return JsonResponse({'data': old_serialized.data}, safe=False)


def create_user(ip):
    new_user = User()
    new_user.ip = ip
    new_user.save()


def create_perceptron():
    new_perceptron = Perceptron()
    new_perceptron.save()

    return new_perceptron


@csrf_exempt
@api_view(['POST'])
def try_perceptron(request):
    perceptron = PerceptronSerializer(data=request.data)
    ArtificialPerceptron(epoches=1, learning_rate=0.1,
                         inputs=np.array([0, 0]), targets=np.array([0, 0, 1]))
    return JsonResponse({})
