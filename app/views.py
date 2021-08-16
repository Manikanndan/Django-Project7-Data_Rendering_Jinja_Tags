from django.shortcuts import render

# Create your views here.
def fun_app(request):
    return render(request,'first.html',context={'name':'Manikanndan','class':'Django','Timings':'12:45 PM'})