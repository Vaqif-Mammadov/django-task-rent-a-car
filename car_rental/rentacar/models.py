from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Car(models.Model):
    model = models.CharField(max_length=100)

    def __str__(self):
        return self.model

class Owner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    car = models.OneToOneField(Car, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    def clean(self):
        if Owner.objects.filter(user=self.user).exists():
            raise ValidationError(_('Bu şəxsin artıq bir avtomobili var və ikinci avtomobili ala bilməz.'))

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

class RentACar(models.Model):
    name = models.CharField(max_length=100)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return self.name




