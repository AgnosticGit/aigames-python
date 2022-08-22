from django.db import models


class User(models.Model):
    ip = models.TextField()
    perceptron_id = models.IntegerField(null=True)
    gradient_descent_2d_id = models.IntegerField(null=True)

    @staticmethod
    def get_request_user(request):
        ip = request.META.get("REMOTE_ADDR")
        return User.objects.filter(ip=ip).first()

    def __str__(self):
        return self.ip
