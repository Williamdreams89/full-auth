from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    """Overiding default user-creation utilities since login have been changed"""
    def create_user(self, email, username,first_name, last_name, department, password=None):
        """Create normal user utility"""
        if not email:
            raise ValueError("Email Must not be empty!!!")
        email = self.normalize_email(email)
        user = self.model(email=email,username=username,  first_name=first_name, last_name=last_name, department=department)
        user.set_password(password) #hashing password
        user.save(using=self._db)
        return user 


    def create_superuser(self, email, username,first_name, last_name, department, password):
        """Create Superusers utility"""
        user = self.create_user(email, username,first_name, last_name, department, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user 