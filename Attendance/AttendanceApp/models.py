from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from .manager import UserManager

class StudentsCustomUser(AbstractBaseUser, PermissionsMixin):
    roll_no = models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True)
    student_name = models.CharField(max_length=50)
    dob = models.DateField()
    branch = models.CharField(max_length=50)
    year = models.IntegerField()
    number = models.CharField(max_length=10, unique=True)
    # user_img = models.ImageField(upload_to="profile")
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    # otp = models.CharField(max_length=4)

    USERNAME_FIELD = 'roll_no'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def __str__(self):
        return self.roll_no

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

class subOtp(models.Model):
    otp = models.CharField(max_length=6)
    londitude = models.CharField(max_length=30)
    langitude = models.CharField(max_length=30)
    

class cseData(models.Model):
    roll_no = models.CharField(max_length=10)
    student_name = models.CharField(max_length=20)
    branch = models.CharField(max_length=50)
    year = models.IntegerField(max_length=1)
    section = models.CharField(max_length=5)
    # otp = models.IntegerField(max_length=6)
    # location = models.CharField(max_length=16)
    subCode = models.CharField(max_length=10)

class itData(models.Model):
    roll_no = models.CharField(max_length=10)
    student_name = models.CharField(max_length=20)
    branch = models.CharField(max_length=50)
    year = models.IntegerField(max_length=1)
    section = models.CharField(max_length=5)
    # otp = models.IntegerField(max_length=6)
    # location = models.CharField(max_length=16)
    subCode = models.CharField(max_length=10)

class eceData(models.Model):
    roll_no = models.CharField(max_length=10)
    student_name = models.CharField(max_length=20)
    branch = models.CharField(max_length=50)
    year = models.IntegerField(max_length=1)
    section = models.CharField(max_length=5)
    # otp = models.IntegerField(max_length=6)
    # location = models.CharField(max_length=16)
    subCode = models.CharField(max_length=10)

