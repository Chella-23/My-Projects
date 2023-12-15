from django.shortcuts import render
from formapp.forms import StudentForm

# Create your views here.
def studentinputview(request):
    form=StudentForm()
    my_dict={'form':form}
    return render(request, 'formapp/base.html',{'form':form})
