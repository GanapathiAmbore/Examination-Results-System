from django.shortcuts import render
from resultsapp.models import Halticket,Student
from django.contrib import messages

def home(request):
    if request.method=='POST':
        number=request.POST.get('number')
        if number:
            result=Student.objects.filter(htno_id=str(number))
            if result:
                return render(request, 'home.html', {'results': result})
            else:
                messages.error(request,'No Results found for {}'.format(number))
    else:
        pass
    return render(request,'home.html')


