from django.shortcuts import render
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
# def index(request):
#     context = {
#         "variable1":"One boy has having only mathaa.",
#         "variable2":"He don't have brain"
#     }
#     return render(request, 'index.html', context)
#     #return HttpResponse("this is home page")

def home(request):
    return render(request, 'base.html')

def index(request):
    # messages.success(request, "This is the test messages..")
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')
    #return HttpResponse("this is about page")

def services(request):
    return render(request, 'services.html')
    #return HttpResponse("this is services page")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your contact details has been sent!')
    return render(request, 'contact.html')






# def Contact(request):
#     if request.method == 'POST':
#         form = Contact(name=request.POST.get('name'), email=request.POST.get('email'), phone=request.POST.get('phone'), desc=request.POST.get('desc'), instance=Contact)
#         if form.is_valid():
#             form.save()
#             return HttpResponse("Exito!")
#         else:
#             form = Contact(instance=Contact)
#     else:
#         form = Contact()
#     return render(request, 'contact.html', {'form': form})


