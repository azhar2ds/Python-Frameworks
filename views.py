from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import *
from django.template import RequestContext
#from django.core.urlresolvers import reverse
def add(request):
    if request.method == 'POST':
        form = Output(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            input1 = cd['input1']
            input2 = cd['input2']
            output = input1 + input2
            return render(request,'output.html', {'form':form, 'input1': input1, 'input2':input2, 'output':output}, )
    else:
            form = Output()
            return render(request, 'add.html', {'form': form},)