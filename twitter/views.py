from django.shortcuts import render_to_response
from twitter.models import Twit
def index(request):
    print request.GET
    if 'q' in request.GET:
        v = Twit()
        v.text = request.GET['q']
        v.save()

    twits=Twit.objects.all()
    return render_to_response("twitter/index.html",{'twits':twits})
# Create your views here.
