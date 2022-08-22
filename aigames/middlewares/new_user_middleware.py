from users.models import User


class NewUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        ip = request.META.get("REMOTE_ADDR")
        user = User.get_request_user(request=request)

        if user is None:
            self.__create_user(ip)

        response = self.get_response(request)

        return response

    @staticmethod
    def __create_user(ip):
        new_user = User()
        new_user.ip = ip
        new_user.save()
