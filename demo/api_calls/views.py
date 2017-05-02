from django.http import HttpResponse
from .models import ApiCall


def demo_api(request):
    count = ApiCall.objects.all().count()
    ApiCall(num=count).save()
    return HttpResponse(str(count))
