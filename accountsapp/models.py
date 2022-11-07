from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager 



class User(AbstractBaseUser, PermissionsMixin):
    """Login with email configs and extra user attributes"""
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add = True)

    objects = UserManager()


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username","first_name", "last_name", "department"]

    @property
    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def __str__(self):
        return "{}-{}".format(self.full_name, self.email)

    class Meta:
        ordering= ["-department", "username"]
