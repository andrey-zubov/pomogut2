from django.db import models
from feincms.module.medialibrary.fields import MediaFile, MediaFileForeignKey
from os.path import join
from django.conf import settings
from django.utils.html import format_html


class Network_security_links(models.Model):
    class Meta:
        db_table = 'Безопасность в сети'
        verbose_name = 'Ссылки для "Безопасность в сети"'
        verbose_name_plural = 'Ссылки для "Безопасность в сети"'

    url = models.URLField(verbose_name='Ссылка')
    title = models.CharField(max_length=25, verbose_name='название ссылки')
    mediafile = MediaFileForeignKey(MediaFile, related_name='+',
                                    null=True, on_delete=models.SET_NULL,
                                    verbose_name='Картинка')

    def __str__(self):
        return self.title

    @property
    def get_img(self):
        return join(settings.MEDIA_URL, str(self.mediafile.file))


class Help_for_addicts_links(models.Model):
    class Meta:
        db_table = 'Помощь наркозависимым'
        verbose_name = 'Сcылки для "Помощь наркозависимым"'
        verbose_name_plural = 'Сcылки для "Помощь наркозависимым"'

    url = models.URLField(verbose_name='Ссылка')
    title = models.CharField(max_length=25, verbose_name='название ссылки')
    mediafile = MediaFileForeignKey(MediaFile, related_name='+',
                                    null=True, on_delete=models.SET_NULL,
                                    verbose_name='Картинка')

    def __str__(self):
        return self.title

    @property
    def get_img(self):
        return join(settings.MEDIA_URL, str(self.mediafile.file))


class To_contact_us(models.Model):
    class Meta:
        db_table = 'Связаться с нами'
        verbose_name = 'Связаться с нами'
        verbose_name_plural = 'Связаться с нами'

    email = models.EmailField()
    text = models.TextField()

    def __str__(self):
        return self.email


class ContactInformation(models.Model):
    class Meta():
        verbose_name = "Контактная информация на сайте"
        verbose_name_plural = "Контактная информация на сайте"

    phone = models.CharField(max_length=17, verbose_name="контактный телефон", null=True, blank=True)
    email = models.EmailField(verbose_name='Адрес электронной почты', null=True, blank=True)
    flag = models.BooleanField(verbose_name='отображать эту информацию', default=True)

    def __str__(self):
        return self.phone + '\n' + self.email


class Partners(models.Model):
    class Meta():
        verbose_name = "Партнер"
        verbose_name_plural = "Партнеры"

    mediafile = MediaFileForeignKey(MediaFile, related_name='+',
                                    null=True, on_delete=models.SET_NULL,
                                    verbose_name='Картинка')
    link = models.CharField(max_length=100, verbose_name='Ссылка')

    def __str__(self):
        return self.link

    @property
    def url_img(self):
        return join(settings.MEDIA_URL, str(self.mediafile.file))

    @property
    def get_img(self):
        return format_html(f"<img src='{self.url_img}' width='70px'>")
# Create your models here.
