from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.dispatch import receiver
from django.db.models.signals import post_save


class RoleChoices:
    BUYER = 'BU'
    BOTH = 'BO'

    @staticmethod
    def get_choices():
        return (
            (RoleChoices.BUYER, _('خریدار')),
            (RoleChoices.BOTH, _('هر دو')),
        )


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(verbose_name=_('نقش'), choices=RoleChoices.get_choices(), max_length=2)
    tel = models.CharField(verbose_name=_('شماره تلفن همراه'), blank=True, null=True, max_length=11)
    address = models.CharField(verbose_name=_('آدرس'), max_length=500, blank=True, null=True)
    avatar = models.ImageField(verbose_name=_('عکس پروفایل'), blank=True, null=True, upload_to='accounts/avatars/')
    # TODO: account_balance?

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()