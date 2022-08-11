from django.urls import path

from perceptron.views.perceptron_view import load_perceptron, reset_perceptron, train_perceptron, try_perceptron


urlpatterns = [
    path('', load_perceptron),
    path('try', try_perceptron),
    path('train', train_perceptron),
    path('reset', reset_perceptron)
]
