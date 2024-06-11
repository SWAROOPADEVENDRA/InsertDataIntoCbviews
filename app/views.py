from typing import Any
from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
from django.views.generic import TemplateView,FormView

from app.forms import *

class InsertdataByTV(TemplateView):
    template_name='InsertdataByTV.html'

    def get_context_data(self, **kwargs):
        EVDO=super().get_context_data(**kwargs)
        #EVDO['name']='Anusha'
        #EVDO['age']=4
        EVDO['EDVO']=VillageForm()
        return EVDO
    
    def post(self,request):
        VDDO=VillageForm(request.POST)
        if VDDO.is_valid():
            VDDO.save()
            return HttpResponse('InsertdataByTV is done')
        else:
            return HttpResponse('InsertdataByTV is done')
        
class DataInsertByFV(FormView):
    template_name='DataInsertByFV.html'
    form_class=VillageForm

    def form_valid(self, form):
        form.save()
        return HttpResponse('DataInsertByFV is done')
    
