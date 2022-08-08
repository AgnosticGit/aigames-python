from perceptron.models import Perceptron
from perceptron.serializers import PerceptronSerializer
from django.http import JsonResponse
from users.models import User


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
