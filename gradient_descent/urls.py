from django.urls import path

from gradient_descent.views import create_or_load_gradient_descent

urlpatterns = [
    path('', create_or_load_gradient_descent),
]
