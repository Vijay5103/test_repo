from django.db import models

# Create your models here.


from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from .manager import CustomUserManager


# Create your models here.


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    create custom user modal
    """
    full_name = models.CharField(max_length=500)
    email = models.EmailField(
        _("email address"),
        unique=True,
        error_messages={
            "unique": "This email address is already associated with another account."
        },
    )

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
   
  
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["full_name"]

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.full_name} - {self.email}"
 

def upload_Book_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return f"Upload_Book/{instance.id}/{filename}"



class AddBook(models.Model):
    id =  models.AutoField(primary_key=True)
    Book_Name = models.CharField(max_length=250)
    Book_Author =  models.CharField(max_length=250,null=True,blank=True)
    Book_Description =  models.CharField(max_length=1000,null=True,blank=True)
    Book_Category = models.CharField(max_length=1000,null=True,blank=True)
    Book_Coverpage = models.FileField(upload_to=upload_Book_path,null=True,blank=True)
    Book_Upload = models.FileField(upload_to=upload_Book_path,null=True,blank=True)
    Genratedate =models.DateTimeField(auto_now_add=True,null=True,blank=True)
    def __str__(self):
        return f"{self.id} - {self.Book_Name}"

    
