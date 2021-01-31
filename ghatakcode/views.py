from django.shortcuts import render


from visitnepal2020.views import log
from .models import Destination,DjangoBitmap,Pdxdataformats


# Create your views here.
class defo:
    def index(self,request):
        res = Destination.objects.all()
        name=log.sendname()
        return render(request, 'index.html',{'result':res,'name':name})
demo=defo()
