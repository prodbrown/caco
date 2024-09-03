from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import EmailValidator, RegexValidator

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    USER_TYPE_CHOICES = [
        ('local', 'Local'),
        ('staff', 'Staff'),
        ('admin', 'Admin'),
    ]
    
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    PHONE_NUMBER_REGEX = r'^\+?1?\d{9,15}$'  # Example regex for international phone numbers

    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, blank=True, null=True)
    surname = models.CharField(max_length=30)
    nida_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(unique=True, validators=[EmailValidator()])
    phone_number_1 = models.CharField(
        max_length=10, 
        unique=True, 
        validators=[RegexValidator(regex=PHONE_NUMBER_REGEX, message="Enter a valid phone number.")]
    )
    phone_number_2 = models.CharField(
        max_length=16, 
        blank=True, 
        null=True, 
        unique=True, 
        validators=[RegexValidator(regex=PHONE_NUMBER_REGEX, message="Enter a valid phone number.")]
    )
    passport_image = models.ImageField(upload_to='passport_images/', blank=True, null=True, default='passport_images/profile.png')
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='local')
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'surname', 'gender', 'phone_number_1']

    def __str__(self):
        return self.email


