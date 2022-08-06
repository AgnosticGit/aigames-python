from django.http import HttpResponse
import uuid


def init_session(request):
    if request.session.get('uuid') == None:
        request.session['uuid'] = uuid.uuid4().hex

    return HttpResponse(status=204)
