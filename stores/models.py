from django.db import models
from accounts.models import Profile
from django.utils.translation import ugettext_lazy as _


class ShippingMethod(models.Model):
    name = models.CharField(max_length=500, verbose_name=_('نام'))
    icon = models.ImageField(upload_to='products/shipping_method', verbose_name=_('تصویر'))


class Store(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=500, verbose_name=_('نام فروشگاه'), unique=True)
    slug = models.SlugField(unique=True, editable=False)
    logo = models.ImageField(verbose_name=_('لوگوی فروشگاه'), upload_to='products/store/logo', null=True, blank=True)
    city = models.CharField(max_length=500, verbose_name=_('شهر'))
    # TODO : cover could be gif or video :D
    cover_image = models.ImageField(verbose_name=_('تصویر کاور'), upload_to='products/store/cover', null=True,
                                    blank=True)
    # TODO : add emojies to text editor
    description = models.TextField(verbose_name=_('توضیحات'), blank=True, null=True)
    creation_date = models.DateTimeField(verbose_name=_('تاریخ ایجاد'), auto_now_add=True)

    # TODO : total_rate
    # TODO : total buyers
    class Meta:
        verbose_name = _('فروشگاه')
        verbose_name_plural = _('فروشگاه ها')

    def __str__(self):
        return self.name

    def get_slug(self):
        slug = self.name.replace(' ', '-')
        return slug

    def save(self, *args, **kwargs):
        self.slug = self.get_slug()
        super(Store, self).save(*args, **kwargs)


class Shipping(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, verbose_name=_('فروشگاه'))
    shipping_method = models.OneToOneField(ShippingMethod, on_delete=models.CASCADE, verbose_name=_('شیوه ارسال'))
    price_store_city = models.CharField(max_length=7, default='0')
    price_other = models.CharField(max_length=7, default='0')


class Policy(models.Model):
    store = models.OneToOneField(Store, on_delete=models.CASCADE)

    return_policy = models.BooleanField(choices=((True, _('امکان پس گرفتن کالا وجود دارد')),
                                                 (False, _('امکان پس گرفتن کالا وجود ندارد'))), default=True)
    return_policy_description = models.CharField(max_length=500, blank=True, null=True)

    exchange_policy = models.BooleanField(choices=((True, _('امکان تعویض کالا وجود دارد')),
                                                   (False, _('امکان تعویض کالا وجود ندارد'))), default=True)
    exchange_policy_description = models.CharField(max_length=500, blank=True, null=True)

    cancellation_policy = models.BooleanField(choices=((True, _('امکان لغو سفارش وجود دارد')),
                                                       (False, _('امکان لغو سفارش وجود ندارد'))), default=True)
    cancellation_policy_description = models.CharField(max_length=500, blank=True, null=True)
    further_description = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.store.name + 'POLICIES'
