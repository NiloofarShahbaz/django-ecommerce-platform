from django.db import models
from django.utils.translation import ugettext_lazy as _


class Rating:
    VERY_BAD = '1'
    BAD = '2'
    MEDIUM = '3'
    GOOD = '4'
    VERY_GOOD = '5'

    @staticmethod
    def get_choices():
        return (
            (Rating.VERY_BAD, _('خیلی بد')),
            (Rating.BAD, _('بد')),
            (Rating.MEDIUM, _('متوسط')),
            (Rating.GOOD, _('خوب')),
            (Rating.VERY_GOOD, _('خیلی خوب'))
        )


class Store(models.Model):
    name = models.CharField(max_length=500, verbose_name=_('نام'), unique=True)
    slug = models.SlugField(unique=True, editable=False)
    logo = models.ImageField(verbose_name=_('لوگو'), upload_to='products/store/logo', null=True, blank=True)
    # TODO : cover could be gif or video :D
    cover_image = models.ImageField(verbose_name=_('تصویر کاور'), upload_to='products/store/cover')
    # TODO : add emojies to text editor
    description = models.TextField(verbose_name=_('توضیحات'), blank=True, null=True)
    policy = models.TextField(verbose_name=_('قوانین و مقررات'), blank=True, null=True)
    creation_date = models.DateTimeField(verbose_name=_('تاریخ ایجاد'), auto_now_add=True)

    # TODO : total_rate
    # TODO : total buyers

    def __str__(self):
        return self.name

    def get_slug(self):
        slug = self.name.replace(' ', '-')
        return slug

    def save(self, *args, **kwargs):
        self.slug = self.get_slug()
        super(Store, self).save(*args, **kwargs)


class Category(models.Model):
    name = models.CharField(max_length=500, verbose_name=_('نام'), unique=True)
    slug = models.SlugField(unique=True, editable=False)
    description = models.TextField(verbose_name=_('توضیحات'), blank=True, null=True)
    image = models.ImageField(verbose_name=_('تصویر'), upload_to='products/category/image')
    order = models.IntegerField(verbose_name=_('ترتیب'), blank=True, null=True)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return self.name

    def get_slug(self):
        slug = self.name.replace(' ', '-')
        return slug

    def save(self, *args, **kwargs):
        self.slug = self.get_slug()
        super(Category, self).save(*args, **kwargs)


class SubCategory(models.Model):
    name = models.CharField(max_length=500, verbose_name=_('نام'), unique=True)
    description = models.TextField(verbose_name=_('توضیحات'), blank=True, null=True)
    image = models.ImageField(verbose_name=_('تصویر'), upload_to='products/category/image')
    slug = models.SlugField(unique=True, editable=False)
    order = models.IntegerField(verbose_name=_('ترتیب'), blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_('دسته بندی'))

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return self.name

    def get_slug(self):
        slug = self.name.replace(' ', '-')
        return slug

    def save(self, *args, **kwargs):
        self.slug = self.get_slug()
        super(SubCategory, self).save(*args, **kwargs)


class Product(models.Model):
    name = models.CharField(max_length=1000, verbose_name=_('نام'))
    slug = models.SlugField(unique=True, editable=False)
    description = models.TextField(verbose_name=_('توضیحات'), blank=True, null=True)
    overview = models.TextField(verbose_name=_('توضیحات'), blank=True, null=True)
    price = models.IntegerField(verbose_name=_('قیمت'))
    # TODO : discount price
    quantity = models.IntegerField(verbose_name=_('تعداد'))
    order = models.IntegerField(verbose_name=_('ترتیب'), blank=True, null=True)
    number_of_buyers = models.IntegerField(verbose_name=_('تعداد خریداران'), default=0)
    rate = models.IntegerField(verbose_name=_('امتیاز'), blank=True, null=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.PROTECT, verbose_name=_('زیر دسته'))
    store = models.ForeignKey(Store, on_delete=models.CASCADE, verbose_name=_('فروشگاه'))

    # TODO: color and weight

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return self.name

    def get_unique_slug(self):
        slug = self.name.replace(' ', '-')
        unique_slug = slug
        num = 1
        while Product.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()
        super(Product, self).save(*args, **kwargs)


class ProductImage(models.Model):
    photo = models.ImageField(verbose_name=_('تصویر'), upload_to='products/category/image')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_('محصول'))

    def __str__(self):
        return self.product.name + " " + "IMAGE"
