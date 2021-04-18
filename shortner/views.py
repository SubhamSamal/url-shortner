from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from .models import urlShortner

# Create your views here.
def urlRedirect(request, output=None, *args, **kwargs):
    urlShortnerObj = get_object_or_404(urlShortner, output=output)
    return HttpResponseRedirect(urlShortnerObj.url)