from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import forms
# Create your views here.
def index(request):
     return render(request,'formapp/index.html')

def form_name_view(request):
    form=forms.formname()
    print("hi")
    if request.method == 'POST':
        print("Hello")
        form=forms.formname(request.POST)

        if form.is_valid():
            print("testing")
            print("validation success")
            print("NAME:  "+ form.cleaned_data['name'])
            print("EMAIL:  "+ form.cleaned_data['email'])
            print("COMMENTS:  "+ form.cleaned_data['comments'])
    return render(request,'formapp/formbasics.html',{'form' : form})
