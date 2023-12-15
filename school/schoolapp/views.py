from django.shortcuts import render
from schoolapp.forms import studentinputform

# Create your views here.
def studentinputview(request):
    form=studentinputform()
    my_dict={'form':form}
    if request.method=='POST':
        form=studentinputform(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'schoolapp/base.html',{'form':form})