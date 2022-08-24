from django.urls import path

from gradient_descent.views import create_or_load_gradient_descent, set_math_expression

urlpatterns = [
    path('', create_or_load_gradient_descent),
    path('math_expression', set_math_expression)
]
