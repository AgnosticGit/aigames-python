from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from gradient_descent.models import GradientDescent2D
from users.models import User
from django.http import JsonResponse
from gradient_descent.serializers import GradientDescent2DSerializer


@csrf_exempt
@api_view(['GET'])
def create_or_load_gradient_descent(request):
    user = User.get_request_user(request)

    if user.gradient_descent_2d_id is None:
        gradient_descent = create_gradient_descent(user)
        serialized_gradient_descent = GradientDescent2DSerializer(gradient_descent)
        return JsonResponse({'data': serialized_gradient_descent})
    else:
        gradient_descent = load_gradient_descent(user)
        serialized_gradient_descent = GradientDescent2DSerializer(gradient_descent)
        return JsonResponse({'data': serialized_gradient_descent.data}, safe=False)


def create_gradient_descent(user):
    gradient_descent = GradientDescent2D()
    gradient_descent.save()

    user.gradient_descent_2d_id = gradient_descent.id
    user.save()

    return gradient_descent


def load_gradient_descent(user):
    gradient_descent_id = user.gradient_descent_2d_id
    gradient_descent = GradientDescent2D.objects.get(id=gradient_descent_id)
    return gradient_descent


@csrf_exempt
@api_view(['POST'])
def set_math_expression(request):
    user = User.get_request_user(request)

    gradient_descent = load_gradient_descent(user)
    gradient_descent.math_expression = request.data['math_expression']

    gradient_descent.fill_points_list(points=100)
    gradient_descent.save()

    serialized_gradient_descent = GradientDescent2DSerializer(gradient_descent)
    return JsonResponse({'data': serialized_gradient_descent.data}, safe=False)
