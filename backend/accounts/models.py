from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.templatetags.static import static

class UserManager(BaseUserManager):

    def create_user(self, email, username, password=None,
                    is_active=True, is_staff=False, is_admin=False):
        user = self.model(
            email=self.normalize_email(email),
            username=username
        )
        user.set_password(password)
        user.is_active = is_active
        user.is_staff = is_staff
        user.is_admin = is_admin
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, username, password=None):
        user = self.create_user(
            email, username, password=password, is_staff=True)
        return user

    def create_superuser(self, email, username, password=None, subscribed=True):
        user = self.create_user(email, username, password=password,
                                is_staff=True, is_admin=True)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address',
                              max_length=255, unique=True)
    username = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True, null=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.username

    def get_shortname(self):
        return self.username

    def get_fullname(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_lable):
        return True

    def get_absolute_url(self):
        # return reverse('accounts:profile',kwargs={'user_slug':self.slug})
        return reverse('/')


class UserProfile(models.Model):
    user = models.OneToOneField(
        'User', on_delete=models.CASCADE,
                related_name='profile',verbose_name=_('User'))
    avatar = models.ImageField(_('avatar'),
                               null=True,blank=True,
                               upload_to='avatarss')
    description = models.TextField(_('description'),null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user + ' profile'
    
    def get_avatar(self):
        try:
            image = self.avatar.url
        except:
            image = static('images/user.png')
        return image
