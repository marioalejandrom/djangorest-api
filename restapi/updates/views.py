from django.http import JsonResponse
from django.views.generic import View
from restapi.mixins import JsonResponseMixin


def json_example_view(request):
    """
    Jason Example GET HttpResponse
    :param request:
    :return: Example dict as Json
    """
    data = {
        "count": 100,
        "content": "This is content"
    }
    return JsonResponse(data)


class JsonCBV(View):
    def get(self, request, *args, **kwargs):
        data = {
            "count": 1000,
            "content": "This is content"
        }
        return JsonResponse(data)


class JsonCBV2(JsonResponseMixin, View):
    def get(self, request, *args, **kwargs):
        data = {
            "count": 100,
            "content": "This is content"
        }
        return self.render_to_json_response(data)
