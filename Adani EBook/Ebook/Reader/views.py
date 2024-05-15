from django.shortcuts import render,redirect
from django.views.generic import View
from Reader.models import CustomUser
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .serializers import AddBookSerializer
from rest_framework.generics import ListAPIView 
from .models import AddBook
# Create your views here.


###Here is Login Page Code  this is Frist Page 
def book(request):
        
       # return render(request, "book.html",{'ebook':'static/alice.epub'})
       return render(request, "book.html",{'ebook':'static/ABEX TECHNICAL FACILITATION GRO - Poojan Soni.epub'})


        


def home(request):
         return render(request, "index.html")


# def login(request):
#          return render(request,"login.html")




class RegisterView(View):
    """
    create class for registration
    """
    template_name = "register.html"
    def get(self, request):

        return render(request, self.template_name)
    
    def post(self, request):
        full_name = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

     
        if CustomUser.objects.filter(email=email).exists():
             messages.error(request, "You have entered email all ready exists.")
             return render(request, self.template_name)
        else:
            user_obj = CustomUser.objects.create(
                full_name=full_name, email=email
            )
            user_obj.set_password(password)
            user_obj.save()
            messages.success(request, "Registration successfully.")
            return render(request, self.template_name)



class LoginView(View):
    """
    create class for login
    """

    template_name = "login.html"

    def get(self, request):
        if request.user.is_authenticated:
              return render(request, self.template_name)
        return render(request, self.template_name)

    def post(self, request):
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(email=email, password=password)
        print(user, "user")
        if user is not None:
            login(request, user)
            messages.success(request, "Login successfully.")
            return redirect("book")
            
            
        messages.error(request, "You have entered an invalid email or password")
        return render(request, self.template_name)
    



class AddBookListview(ListAPIView):
     queryset = AddBook.objects.all()
     serializer_class = AddBookSerializer
    




