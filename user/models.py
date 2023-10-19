from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import PermissionsMixin


class UserManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self,email, password, **extra_fields):
        if not email:
            raise ValueError()

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must have is_staff=True.'
            )
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must have is_superuser=True.'
            )

        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractUser, PermissionsMixin):
    class SportSection(models.TextChoices):
        TAEKWONDO = 'T', 'Тхэквондо'
        JUDO = 'J', 'Дзюдо'
        BOXING = 'B', 'Бокс'
        SAMBO = 'S', 'Самбо'
        KARATE = 'K', 'Карате'
        MMA = 'M', 'ММА'
        FREESTYLE_WRESTLING = 'FW', 'Вольная борьба'
        GRAPPLING = 'G', 'Грэпплинг'

    class JobTitle(models.TextChoices):
        PUPIL = 'P', 'Ученик'
        COACH = 'C', 'Тренер'

    patronymic = models.CharField(max_length=20)
    sport_section = models.CharField(max_length=2,
                                     choices=SportSection.choices)
    position = models.CharField(max_length=2, choices=JobTitle.choices)

    username = models.CharField(
        max_length=100,
        error_messages={"unique": ("Такой пользователь уже существует")},
        null=True,
        blank=True
    )
    email = models.EmailField('email adress', unique=True)

    is_active = models.BooleanField(default=False)

    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []











