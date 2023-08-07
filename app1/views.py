from django.shortcuts import render

# Create your views here.
def condition(request):
    d={'s':'kalyani'}
    return render(request,'hai.html',context=d)