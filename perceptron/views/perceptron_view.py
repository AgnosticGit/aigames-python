import numpy as np
from perceptron.artificial_perceptron import ArtificialPerceptron
from perceptron.models import Perceptron
from perceptron.serializers import PerceptronSerializer
from django.http import JsonResponse
from users.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view


def load_perceptron(request):
    ip = request.META.get("REMOTE_ADDR")
    user = User.objects.filter(ip=ip).first()

    perceptron_id = user.perceptron_id

    if perceptron_id is None:
        new_perceptron = create_perceptron()
        user.perceptron_id = new_perceptron.id
        user.save()

        serialized = PerceptronSerializer(new_perceptron)

        return JsonResponse({'data': serialized.data}, safe=False)

    old_perceptron = Perceptron.objects.get(pk=perceptron_id)
    old_serialized = PerceptronSerializer(old_perceptron)

    return JsonResponse({'data': old_serialized.data}, safe=False)


def create_perceptron():
    new_perceptron = Perceptron()
    new_perceptron.save()

    return new_perceptron


@csrf_exempt
@api_view(['POST'])
def try_perceptron(request):
    ip = request.META.get("REMOTE_ADDR")
    user = User.objects.filter(ip=ip).first()
    perceptron_id = user.perceptron_id
    perceptron_data = request.data

    perceptron = Perceptron.objects.get(pk=perceptron_id)

    perceptron.input1 = perceptron_data['input1']
    perceptron.input2 = perceptron_data['input2']
    perceptron.save()

    serialized = PerceptronSerializer(perceptron)
    data = serialized.data

    artificial_perceptron = ArtificialPerceptron(weights=np.array([data['w0'], data['w1']]),
                                                 epoches=data['epoches'],
                                                 learning_rate=0.1,
                                                 inputs=np.array(
                                                     [data['input1'], data['input2']]),
                                                 targets=np.array([0, 0, 1]))
    data['output'] = artificial_perceptron.request()

    return JsonResponse({'data': data})


@csrf_exempt
@api_view(['POST'])
def train_perceptron(request):
    ip = request.META.get("REMOTE_ADDR")
    user = User.objects.filter(ip=ip).first()
    perceptron_id = user.perceptron_id
    perceptron_data = request.data

    artificial_perceptron = ArtificialPerceptron(weights=np.array([perceptron_data['w0'], perceptron_data['w1']]),
                                                 epoches=perceptron_data['epoches'],
                                                 learning_rate=perceptron_data['learning_rate'],
                                                 inputs=np.array(
                                                     [perceptron_data['input1'], perceptron_data['input2']]),
                                                 targets=np.array([0, 1, 1, 1]))
    artificial_perceptron.train(inputs=np.array([
        [0, 0],
        [1, 0],
        [1, 1],
        [0, 1]]))

    perceptron = Perceptron.objects.get(pk=perceptron_id)
    perceptron.input1 = perceptron_data['input1']
    perceptron.input2 = perceptron_data['input2']
    perceptron.learning_rate = perceptron_data['learning_rate']
    perceptron.epoches = perceptron_data['epoches']
    perceptron.w0 = round(artificial_perceptron.weights[0], 2)
    perceptron.w1 = round(artificial_perceptron.weights[1], 2)
    perceptron.save()

    serialized = PerceptronSerializer(perceptron)

    return JsonResponse({'data': serialized.data})


@csrf_exempt
@api_view(['POST'])
def reset_perceptron(request):
    ip = request.META.get("REMOTE_ADDR")
    user = User.objects.filter(ip=ip).first()
    perceptron_id = user.perceptron_id
    perceptron = Perceptron.objects.get(pk=perceptron_id)

    initial_perceptron = Perceptron()

    perceptron.input1 = initial_perceptron.input1
    perceptron.input2 = initial_perceptron.input2
    perceptron.epoches = initial_perceptron.epoches
    perceptron.learning_rate = initial_perceptron.learning_rate
    perceptron.w0 = initial_perceptron.w0
    perceptron.w1 = initial_perceptron.w1
    perceptron.output = initial_perceptron.output
    perceptron.save()

    serialized = PerceptronSerializer(perceptron)
    data = serialized.data

    return JsonResponse({'data': data})
