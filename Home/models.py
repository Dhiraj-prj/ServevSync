
from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.conf import settings
from django.conf.urls.static import static

class UserProfile(models.Model):
    ROLE_CHOICES = (
        ('hirer', 'Hirer'),
        ('houseworker', 'Houseworker'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.role}"

    role = models.CharField(max_length=15, choices=ROLE_CHOICES, null=True, blank=True)

    class Service(models.Model):
        name = models.CharField(max_length=100, unique=True)

        def __str__(self):
            return self.name

class Profile(models.Model):
    ROLE_CHOICES = [
        ('owner', 'House Owner'),
        ('maid', 'Maid'),
    ]

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.role}"

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('houseowner', 'House Owner'),
        ('houseworker', 'House Worker'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='houseowner')

    # Explicitly set related_name for user_permissions to avoid conflicts
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_groups',  # Custom related_name
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions',  # Custom related_name
        blank=True,
    )

    def __str__(self):
        return self.username




class Service(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    service_name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.service_name




class HouseworkerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='houseworker_profile')
    name = models.CharField(max_length=100)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='houseworkers')
    contact = models.CharField(max_length=50)
    bio = models.TextField(blank=True)
    rating = models.FloatField(default=0.0)

    photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)

    def __str__(self):
        return self.name

class HouseworkerProfile(models.Model):
    SERVICE_CHOICES = [
        ('CLEANING SERVICES', 'Cleaning Services'),
        ('BABYSITTING', 'Babysitting'),
        ('COOKING ASSISTANCE', 'Cooking Assistance'),
        ('GARDENING SERVICES', 'Gardening Services'),
        ('ELDER CARE', 'Elder Care'),
        ('HOME MAINTENANCE', 'Home Maintenance'),
        ('LAUNDRY SERVICES', 'Laundry Services'),
        ('CUSTOM HOME SERVICES', 'Custom Home Services'),
        ('PLUMBING', 'Plumbing'),
        ('ELECTRICIAN', 'Electrician'),
    ]

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="houseworker_profile",
        blank=True,
        null=True
    )
    name = models.CharField(max_length=100)
    service = models.CharField(max_length=100, choices=SERVICE_CHOICES)
    contact = models.CharField(max_length=50)
    bio = models.TextField(blank=True)
    rating = models.FloatField(default=0.0)
    photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)

    def __str__(self):
        return self.name



from django.db import models

class UniqueServiceModel(models.Model):
    service_name = models.CharField(max_length=255)

    def __str__(self):
        return self.service_name

class UniqueProfileModel(models.Model):
    full_name = models.CharField(max_length=255)
    selected_service = models.ForeignKey(UniqueServiceModel, on_delete=models.CASCADE)
    contact_info = models.CharField(max_length=15)
    biography = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.full_name
