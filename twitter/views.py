from django.shortcuts import render_to_response
from twitter.models import Twit
def index(request):

    twits=Twit.objects.all
    return render_to_response("twitter/index.html",{'twits':twits})
# Create your views here.
