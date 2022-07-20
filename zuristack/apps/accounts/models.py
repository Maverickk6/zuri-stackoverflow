from enum import unique
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import AbstractUser
# Create your models here.
from . import utils

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)

    slug = models.SlugField(blank=True, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        ordering = ["email"]
        verbose_name = "User"

    def __str__(self):
        return self.email

    # creating a default slug/username for users

    def generate_random_slug(self):
        random_slug = slugify(self.first_name + self.last_name +
                              utils.generate_random_id())
        while CustomUser.objects.filter(slug=random_slug).exists():
            random_slug = slugify(self.first_name + self.last_name +
                                  utils.generate_random_id())
        return random_slug

    def save(self, *args, **kwargs):
        # perform some logic
        # check for a slug. if not exists, create one

        if not self.slug:

            self.slug = self.generate_random_slug()

            # then finally save

        super().save(*args, **kwargs)
