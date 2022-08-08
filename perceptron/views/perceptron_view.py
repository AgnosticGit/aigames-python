from perceptron.models import Perceptron
from perceptron.serializers import PerceptronSerializer
from django.http import JsonResponse


def load_perceptron(request):
    perceptron_id = request.session.get('perceptron_id')

    if perceptron_id == None:
        new_perceptron = create_perceptron()
        request.session['perceptron_id'] = new_perceptron.id
        serialized = PerceptronSerializer(new_perceptron)

        return JsonResponse(serialized.data, safe=False)

    old_perceptron = Perceptron.objects.get(pk=perceptron_id)
    serialized = PerceptronSerializer(old_perceptron)

    return JsonResponse(serialized.data, safe=False)


def create_perceptron():
    new_perceptron = Perceptron()
    new_perceptron.save()
    return new_perceptron


