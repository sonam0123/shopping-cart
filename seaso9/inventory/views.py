from django.http import HttpResponse ,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.shortcuts import render ,get_object_or_404
from django.core.urlresolvers import reverse ,reverse_lazy
from django.views.generic.edit import DeleteView # this is the generic view
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User



from .models import Product
from .serializers import ProductSerializer

from .forms import RegistrationForm


"""
Render content into json
"""
class JSONResponse(HttpResponse):

    """
    An HttpResponse that renders its content into JSON.
    """

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

"""
Display product list on api
"""
@csrf_exempt
def product_list(request):
    if request.method == 'GET':
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)

        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=200)
    return JSONResponse(serializer.errors, status=400)


"""
Display each product details
"""
@csrf_exempt
def product_details(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser.parse(request)
        serializer = ProductSerializer(product, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        Product.delete()
        return HttpResponse(status=204)

def home(request):
    # Render the HTML template.
    if request.method == 'GET':
        if request.user.is_authenticated:
            product = Product.objects.all()
        return render(request, "template.html")
    return render(request, "login.html")


def signup(request):
    # Render the HTML template.
    return render(request, "registration_form.html")

def login(request):
    # Render the HTML template.
    return render(request, "/customer/login.html")



def productDetails(request ,pk):
    # Render the HTML template.
    if request.method == 'GET':
        return render(request, "productDetails.html")

def Deals(request):
    # Render the HTML template.
    return render(request, "deal.html")

def Store(request):
    # Render the HTML template.
    return render(request, "store.html")

def contact(request):
    # Render the HTML template.
    return render(request, "contact.html")

def profile(request):
    # Render the HTML template.
    return render(request, "profile.html")

"""
user Registration
"""
def registration_form(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=username, firstname=name, email=email,password=   password)
            form.save()
            return render(request ,"success.html")
        else:
            return render(request,"registration_form.html", {"form":form})


    else:
        form = RegistrationForm()
        return render(request,"registration_form.html",{"form":form})

"""
def userList(request):
    if request.method == 'GET':
        #users = Registration.objects.all()
        #return render(request ,"users.html" ,{"users":users})
def updateuser(request, pk):
    #instance = get_object_or_404(Registration, pk=pk)
    if request.method == 'POST':

        form = UpdateuserForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            return render(request ,"success.html")
        else:
            return render(request,"update.html",{"form":form})

    else:
        form = UpdateuserForm(request.POST or None, instance=instance)
        return render(request,"update.html",{"form":form})
"""
def deleteuser(DeleteView):
    Model = Registration
    """
        if request.method == 'POST':
            user=Registration.objects.get(pk=pk)
            user.delete()
        return HttpResponseRedirect(reverse('inventory.views.userList'))
        """
    success_url = reverse_lazy('inventory.views.userList') # This is where this view will
                                            # redirect the user
    template_name = 'delete.html'

def login(request):

    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(username=username,password = password)

    if user is not None:
        if user.is_active:
            login(request ,user)
            return render(request ,"success.html")
        else:
            return render(request,"login.html")
            #return a disable account error message

    else:
        return render(request,"login.html")
             #return invalid error message

