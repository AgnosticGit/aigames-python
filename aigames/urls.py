from django.contrib import admin
from django.urls import path, include

from aigames.views.session_view import init_session

urlpatterns = [
    path('__debug__/', include('debug_toolbar.urls')),
    path('admin/', admin.site.urls),
    path('session/', init_session),
    path('perceptron/', include('perceptron.urls')),
    path('gradient_descent_2d/', include('gradient_descent.urls'))
]
