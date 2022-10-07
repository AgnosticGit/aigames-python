from django.urls import path

from gradient_descent.views import create_or_load_gradient_descent, set_math_expression, set_point_x, descent, set_delta

urlpatterns = [
    path('', create_or_load_gradient_descent),
    path('math_expression', set_math_expression),
    path('point_x', set_point_x),
    path('descent', descent),
    path('delta', set_delta)
]
