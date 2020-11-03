from django.db import models
from django.utils.translation import ugettext_lazy as _
from feincms.module.page.models import Page
from mptt.models import MPTTModel, TreeForeignKey, TreeManyToManyField
from feincms.module.medialibrary.fields import MediaFileForeignKey, MediaFile
from mptt import register
from feincms import extensions
from django.conf import settings
from os.path import join
from django.utils.html import format_html
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from django_ymap.fields import YmapCoord
from django.template.loader import render_to_string
from re import findall


Page.register_extensions(
    'feincms.extensions.datepublisher',
)

Page.register_templates({
    'title': _('General Template'),
    'path': 'template1.html',
    'regions': (
        ('main', _('Main content area.')),
    ),
    })


class Search(models.Model):
    pages = models.ManyToManyField(Page)
    word = models.CharField(max_length=100)

    def __str__(self):
        return str([i.title for i in self.pages.all()])


class Category(MPTTModel):
    class Meta():
        db_table = 'category'
        verbose_name = 'Раздел-категория-тег'
        verbose_name_plural = 'Раздел-категория-тег'
        ordering = ('tree_id', 'level')

    class MPTTMeta:
        order_insertion_by = ['title']

    title = models.CharField(max_length=50, unique=False, verbose_name='Название')
    slug = models.SlugField(verbose_name="Слаг")
    flag = models.BooleanField(verbose_name="Стадия разработки", default=False, help_text="Страницы будут не доступны для пользователя")
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children',
                            verbose_name='Родитель')
    mediafile = MediaFileForeignKey(MediaFile, related_name='+',
                                    null=True, blank=True, on_delete=models.SET_NULL,
                                    verbose_name='Картинка')

    def __str__(self):
        return self.title

    @property
    def get_url(self):
        all_slugs = []
        id = self.id
        while self:
            all_slugs.append(str(self.slug))
            self = self.parent
        return '/'.join(all_slugs[::-1]) + '|' + str(id)

    @property
    def url_img(self):
        return join(settings.MEDIA_URL, str(self.mediafile.file))

    @property
    def get_img(self):
        if self.mediafile:
            return format_html(f"<img src='{self.url_img}' width='70px'>")
        return None


register(Category, order_insertion_oy=['title'])


class Block(models.Model):
    class Meta():
        verbose_name = 'Блок главной страницы'
        verbose_name_plural = 'Блоки главной страницы'

    title = models.CharField(max_length=100, verbose_name="Название блока")
    slug = models.SlugField(verbose_name="Слаг")
    name_button = models.CharField(max_length=100, verbose_name="Название кнопки")
    text = models.TextField(verbose_name="Текст")
    picture = MediaFileForeignKey(MediaFile,
                                  related_name='+',
                                  on_delete=models.SET_NULL,
                                  null=True,
                                  verbose_name="Картинка")
    categories = models.ManyToManyField(Category, verbose_name="Раздел-категория-тег")
    pages = models.ManyToManyField(Page, verbose_name="Статьи")

    def __str__(self):
        return self.title

    @property
    def get_img(self):
        return join(settings.MEDIA_URL, str(self.picture.file))


def name_category(object):
    if object.category:
        return ";".join([i.title for i in object.category.all()])


class Extension(extensions.Extension):
    ident = "category"

    def handle_model(self):
        self.model.add_to_class(
            'category',
            TreeManyToManyField(Category,
                                null=False,
                                blank=False,
                                related_name="%(app_label)s_%(class)s_category",
                                verbose_name='Раздел-категория-тег')
        )

        self.model.add_to_class(
            'mediafile',
            MediaFileForeignKey(MediaFile, on_delete=models.SET_NULL,
                                related_name='+',
                                null=True,
                                verbose_name='Картинка')
        )

        self.model.add_to_class('name_category', property(name_category))
        self.model.add_to_class('url_img', property(lambda x: join(settings.MEDIA_URL, str(x.mediafile.file))))
        self.model.add_to_class('stars', models.PositiveIntegerField(default=0))
        self.model.add_to_class('count_for_r', models.PositiveIntegerField(default=0))
        self.model.add_to_class('raiting', models.FloatField(default=0, verbose_name='Рейтинг'))

    def handle_modeladmin(self, modeladmin):
        modeladmin.extend_list("list_filter", ["category"])
        modeladmin.extend_list("list_display", ["name_category", "raiting"])
        modeladmin.add_extension_options(
            _("Category"),
            {"fields": ("category",), },
        )
        modeladmin.add_extension_options(
            _("image"),
            {"fields": ("mediafile",), },
        )


Page.register_extensions(Extension)


class Map(models.Model):
    class Meta():
        verbose_name = 'Точка'
        verbose_name_plural = 'Точки'

    title = models.CharField(max_length=200, verbose_name='Название точки')
    description = models.TextField(verbose_name='описание точки')
    address = YmapCoord(max_length=200, start_query=u'Минск', size_width=500, size_height=500)

    def __str__(self):
        return self.title


class Single_column(models.Model):
    class Meta:
        verbose_name = "Одноколоночный"
        abstract = True

    title = models.CharField(verbose_name='подпись Виджета', max_length=150)
    picture = MediaFileForeignKey(MediaFile,
                                  related_name='+',
                                  null=True,
                                  on_delete=models.SET_NULL,
                                  verbose_name="Картинка")
    under_img = models.CharField(max_length=150, verbose_name="подпись картинки", blank=True, null=True)
    text = models.TextField(verbose_name='основной текст', default='<p></p>',
                            help_text='''&ltp&gt &lt/p&gt-Тег для выделения
                             &lti&gt &lt/i&gt-курсив &ltb&gt &lt/b&gt-Жирный шрифт ''')

    title2 = models.CharField(max_length=150, verbose_name='заголовок пунктов', null=True, blank=True)
    point = models.TextField(verbose_name='пункты', default='<li></li>',
                             help_text='&ltli&gt &lt/li&gt -Тег для установки точки', null=True, blank=True)

    def render(self):
        return render_to_string('widget/single-column/widgets-page.html', {'widget':self,
                                                                           'text':mark_safe(self.text),
                                                                           'point':mark_safe(self.point)})

    @property
    def get_img(self):
        return join(settings.MEDIA_URL, str(self.picture.file))

    def save(self, **kwargs):############################################################################################
        super().save(**kwargs)
        content = self.title + " " + self.under_img + " " + self.text.replace('<p>', '').replace('</p>', '') + " "
        content += self.title2 + " " + self.point.replace('<li>', '').replace('</li>', '')
        content = " ".join(findall(r'[\w ]+', content))
        for w in content.lower().split():
            find_pages = Search.objects.filter(word = w)
            if find_pages:
                find_pages[0].pages.add(Page.objects.get(id=self.parent_id))
                find_pages[0].save()
            else:
                s = Search(word=w)
                s.save()
                s.pages.add(Page.objects.get(id=self.parent_id))
                s.save()



Page.create_content_type(Single_column)


class Raiting(models.Model):
    class Meta:
        verbose_name = "Рейтинг"
        abstract = True

    def render(self):
        page = Page.objects.get(raiting_set=self.id)
        return render_to_string('widget/raiting/widgets-page1.html', {'page_id':page.id})


Page.create_content_type(Raiting)


class Three_column(models.Model):
    class Meta:
        verbose_name = "Трехколоночный"
        abstract=True

    title = models.CharField(max_length=70, verbose_name='Название')

    picture1 = MediaFileForeignKey(MediaFile,
                                   related_name='+',
                                   null=True,
                                   blank=True,
                                   on_delete=models.SET_NULL,
                                   verbose_name="Картинка 1")
    key1 = models.CharField(max_length=70, verbose_name='Подпись 1', null=True, blank=True)

    picture2 = MediaFileForeignKey(MediaFile,
                                   related_name='+',
                                   null=True,
                                   blank=True,
                                   on_delete=models.SET_NULL,
                                   verbose_name="Картинка 2")
    key2 = models.CharField(max_length=70, verbose_name='Подпись 2', null=True, blank=True)

    picture3 = MediaFileForeignKey(MediaFile,
                                   related_name='+',
                                   null=True,
                                   blank=True,
                                   on_delete=models.SET_NULL,
                                   verbose_name="Картинка 3")
    key3 = models.CharField(max_length=70, verbose_name='Подпись 3', null=True, blank=True)

    picture4 = MediaFileForeignKey(MediaFile,
                                   related_name='+',
                                   null=True,
                                   blank=True,
                                   on_delete=models.SET_NULL,
                                   verbose_name="Картинка 4")
    key4 = models.CharField(max_length=70, verbose_name='Подпись 4', null=True, blank=True)

    picture5 = MediaFileForeignKey(MediaFile,
                                   related_name='+',
                                   null=True,
                                   blank=True,
                                   on_delete=models.SET_NULL,
                                   verbose_name="Картинка 5")
    key5 = models.CharField(max_length=70, verbose_name='Подпись 5', null=True, blank=True)

    picture6 = MediaFileForeignKey(MediaFile,
                                   related_name='+',
                                   null=True,
                                   blank=True,
                                   on_delete=models.SET_NULL,
                                   verbose_name="Картинка 6")
    key6 = models.CharField(max_length=70, verbose_name='Подпись 6', null=True, blank=True)

    picture7 = MediaFileForeignKey(MediaFile,
                                   related_name='+',
                                   null=True,
                                   blank=True,
                                   on_delete=models.SET_NULL,
                                   verbose_name="Картинка 7")
    key7 = models.CharField(max_length=70, verbose_name='Подпись 7', null=True, blank=True)

    @property
    def get_img(self):
        imgs= [join(settings.MEDIA_URL, str(i.file)) for i in [self.picture1, self.picture2, self.picture3, self.picture4, self.picture5, self.picture6, self.picture7] if i]
        return imgs

    def render(self):
        return render_to_string('widget/three-column/widgets-page.html', {'obj':self})

    def save(self, **kwargs):############################################################################################
        super().save(**kwargs)
        content = self.title + " "
        if self.key1:
            content += self.key1 + " "
        if self.key2:
            content += self.key2 + " "
        if self.key3:
            content += self.key3 + " "
        if self.key4:
            content += self.key4 + " "
        if self.key5:
            content += self.key5 + " "
        if self.key6:
            content += self.key6 + " "
        if self.key7:
            content += self.key7
        content = " ".join(findall(r'[\w ]+', content))
        for w in content.lower().split():
            find_pages = Search.objects.filter(word=w)
            if find_pages:
                find_pages[0].pages.add(Page.objects.get(id=self.parent_id))
                find_pages[0].save()
            else:
                s = Search(word=w)
                s.save()
                s.pages.add(Page.objects.get(id=self.parent_id))
                s.save()


Page.create_content_type(Three_column)


class Two_column(models.Model):
    class Meta:
        verbose_name = "Двухколоночный"
        abstract = True

    title = models.CharField(max_length=150, verbose_name='Название')
    picture1 = MediaFileForeignKey(MediaFile,
                                   related_name='+',
                                   null=True,
                                   on_delete=models.SET_NULL,
                                   verbose_name="Картинка 1")
    key1 = models.CharField(max_length=150, verbose_name='Подпись под картинкой 1', blank=True, null=True)
    text1 = models.TextField(verbose_name="Текст 1", max_length=600)

    picture2 = MediaFileForeignKey(MediaFile,
                                   related_name='+',
                                   null=True,
                                   on_delete=models.SET_NULL,
                                   verbose_name="Картинка 2")
    key2 = models.CharField(max_length=150, verbose_name='Подпись под картинкой 2', null=True, blank=True)
    text2 = models.TextField(verbose_name="Текст 2", max_length=600)

    @property
    def get_img(self):
        return join(settings.MEDIA_URL, str(self.picture1.file)), join(settings.MEDIA_URL, str(self.picture2.file))

    def render(self):
        return render_to_string('widget/two-column/widgets-page.html', {'two':self})

    def save(self, **kwargs):############################################################################################
        super().save(**kwargs)
        content = self.title + " " + self.key1 + " " + self.text1 + " " + self.key2 + " " + self.text2
        content = " ".join(findall(r'[\w ]+', content))
        for w in content.lower().split():
            find_pages = Search.objects.filter(word=w)
            if find_pages:
                find_pages[0].pages.add(Page.objects.get(id=self.parent_id))
                find_pages[0].save()
            else:
                s = Search(word=w)
                s.save()
                s.pages.add(Page.objects.get(id=self.parent_id))
                s.save()


Page.create_content_type(Two_column)


class Slider(models.Model):
    class Meta:
        verbose_name = "Слайдер для малышей"
        abstract = True

    title = models.CharField(max_length=150, verbose_name='название')

    picture1 = MediaFileForeignKey(MediaFile,
                                   related_name='+',
                                   null=True,
                                   blank=True,
                                   on_delete=models.SET_NULL,
                                   verbose_name="Картинка 1")
    key1 = models.CharField(max_length=70, verbose_name='Заголовок под картинкой', null=True, blank=True)
    for_picture1 = models.CharField(max_length=70, null=True, blank=True, verbose_name='подпись под картинкой 1')
    text1 = models.TextField(verbose_name='Текст 1', null=True, blank=True, max_length=500,
                             help_text="слайд счиается валидным если у него заполнены поля:\n Картинка, заголовок под картинкой и сам ткст - в противном случае этот слайд показан не будет")

    picture2 = MediaFileForeignKey(MediaFile,
                                   related_name='+',
                                   null=True,
                                   blank=True,
                                   on_delete=models.SET_NULL,
                                   verbose_name="Картинка 2")
    key2 = models.CharField(max_length=70, verbose_name='Заголовок под картинкой', null=True, blank=True)
    for_picture2 = models.CharField(max_length=70, null=True, blank=True, verbose_name='подпись под картинкой 2')
    text2 = models.TextField(verbose_name='Текст 2', null=True, blank=True, max_length=500,
                             help_text="слайд счиается валидным если у него заполнены поля:\n Картинка, заголовок под картинкой и сам ткст - в противном случае этот слайд показан не будет")

    picture3 = MediaFileForeignKey(MediaFile,
                                   related_name='+',
                                   null=True,
                                   blank=True,
                                   on_delete=models.SET_NULL,
                                   verbose_name="Картинка 3")
    key3 = models.CharField(max_length=70, verbose_name='Заголовок под картинкой', null=True, blank=True)
    for_picture3 = models.CharField(max_length=70, null=True, blank=True, verbose_name='подпись под картинкой 3')
    text3 = models.TextField(verbose_name='Текст 3', null=True, blank=True, max_length=500,
                             help_text="слайд счиается валидным если у него заполнены поля:\n Картинка, заголовок под картинкой и сам ткст - в противном случае этот слайд показан не будет")

    picture4 = MediaFileForeignKey(MediaFile,
                                   related_name='+',
                                   null=True,
                                   blank=True,
                                   on_delete=models.SET_NULL,
                                   verbose_name="Картинка 4")
    key4 = models.CharField(max_length=70, verbose_name='Заголовок под картинкой', null=True, blank=True)
    for_picture4 = models.CharField(max_length=70, null=True, blank=True, verbose_name='подпись под картинкой 4')
    text4 = models.TextField(verbose_name='Текст 4', null=True, blank=True, max_length=500,
                             help_text="слайд счиается валидным если у него заполнены поля:\n Картинка, заголовок под картинкой и сам ткст - в противном случае этот слайд показан не будет")

    picture5 = MediaFileForeignKey(MediaFile,
                                   related_name='+',
                                   null=True,
                                   blank=True,
                                   on_delete=models.SET_NULL,
                                   verbose_name="Картинка 5")
    key5 = models.CharField(max_length=70, verbose_name='Заголовок под картинкой', null=True, blank=True)
    for_picture5 = models.CharField(max_length=70, null=True, blank=True, verbose_name='подпись под картинкой 5')
    text5 = models.TextField(verbose_name='Текст 5', null=True, blank=True, max_length=500,
                             help_text="слайд счиается валидным если у него заполнены поля:\n Картинка, заголовок под картинкой и сам ткст - в противном случае этот слайд показан не будет")

    picture6 = MediaFileForeignKey(MediaFile,
                                   related_name='+',
                                   null=True,
                                   blank=True,
                                   on_delete=models.SET_NULL,
                                   verbose_name="Картинка 6")
    key6 = models.CharField(max_length=70, verbose_name='Заголовок под картинкой', null=True, blank=True)
    for_picture6 = models.CharField(max_length=70, null=True, blank=True, verbose_name='подпись под картинкой 6')
    text6 = models.TextField(verbose_name='Текст 6', null=True, blank=True, max_length=500,
                             help_text="слайд счиается валидным если у него заполнены поля:\n Картинка, заголовок под картинкой и сам ткст - в противном случае этот слайд показан не будет")

    picture7 = MediaFileForeignKey(MediaFile,
                                   related_name='+',
                                   null=True,
                                   blank=True,
                                   on_delete=models.SET_NULL,
                                   verbose_name="Картинка 7")
    key7 = models.CharField(max_length=70, verbose_name='Заголовок под картинкой', null=True, blank=True)
    for_picture7 = models.CharField(max_length=70, null=True, blank=True, verbose_name='подпись под картинкой 7')
    text7 = models.TextField(verbose_name='Текст 7', null=True, blank=True, max_length=500,
                             help_text="слайд счиается валидным если у него заполнены поля:\n Картинка, заголовок под картинкой и сам ткст - в противном случае этот слайд показан не будет")

    picture8 = MediaFileForeignKey(MediaFile,
                                   related_name='+',
                                   null=True,
                                   blank=True,
                                   on_delete=models.SET_NULL,
                                   verbose_name="Картинка 8")
    key8 = models.CharField(max_length=70, verbose_name='Заголовок под картинкой', null=True, blank=True)
    for_picture8 = models.CharField(max_length=70, null=True, blank=True, verbose_name='подпись под картинкой 8')
    text8 = models.TextField(verbose_name='Текст 8', null=True, blank=True, max_length=500,
                             help_text="слайд счиается валидным если у него заполнены поля:\n Картинка, заголовок под картинкой и сам ткст - в противном случае этот слайд показан не будет")

    picture9 = MediaFileForeignKey(MediaFile,
                                   related_name='+',
                                   null=True,
                                   blank=True,
                                   on_delete=models.SET_NULL,
                                   verbose_name="Картинка 9")
    key9 = models.CharField(max_length=70, verbose_name='Заголовок под картинкой', null=True, blank=True)
    for_picture9 = models.CharField(max_length=70, null=True, blank=True, verbose_name='подпись под картинкой 9')
    text9 = models.TextField(verbose_name='Текст 9', null=True, blank=True, max_length=500,
                             help_text="слайд счиается валидным если у него заполнены поля:\n Картинка, заголовок под картинкой и сам ткст - в противном случае этот слайд показан не будет")

    picture10 = MediaFileForeignKey(MediaFile,
                                    related_name='+',
                                    null=True,
                                    blank=True,
                                    on_delete=models.SET_NULL,
                                    verbose_name="Картинка 10")
    key10 = models.CharField(max_length=70, verbose_name='Заголовок под картинкой', null=True, blank=True)
    for_picture10 = models.CharField(max_length=70, null=True, blank=True, verbose_name='подпись под картинкой 10')
    text10 = models.TextField(verbose_name='Текст 10', null=True, blank=True, max_length=500,
                              help_text="слайд счиается валидным если у него заполнены поля:\n Картинка, заголовок под картинкой и сам ткст - в противном случае этот слайд показан не будет")

    @property
    def valid_slides(self):
        l = [i for i in[(self.picture1, self.for_picture1, self.key1, self.text1), (self.picture2, self.for_picture2, self.key2, self.text2), (self.picture3, self.for_picture3, self.key3, self.text3),
                        (self.picture4, self.for_picture4, self.key4, self.text4), (self.picture5, self.for_picture5, self.key5, self.text5), (self.picture6, self.for_picture6, self.key6, self.text6),
                        (self.picture7, self.for_picture7, self.key7, self.text7), (self.picture8, self.for_picture8, self.key8, self.text8), (self.picture9, self.for_picture9, self.key9, self.text9),
                        (self.picture10, self.for_picture10, self.key10, self.text10)] if i[0] and i[2] and i[3]]
        return l

    @property
    def get_img(self):
        l = self.valid_slides
        #imgs = [join(settings.MEDIA_URL, str(i[0].file)) for i in l]
        imgs = [(join(settings.MEDIA_URL, str(i[0].file)), i[1], i[2], i[3]) for i in l]
        return imgs

    def render(self):
        return render_to_string('widget/slider/widget-page.html', {'slider':self})

    def save(self, **kwargs):############################################################################################
        super().save(**kwargs)
        content = self.title + " "
        if self.text1:
            content += self.text1 + " "
        if self.text1:
            content += self.text2 + " "
        if self.text1:
            content += self.text3 + " "
        if self.text1:
            content += self.text4 + " "
        if self.text1:
            content += self.text5 + " "
        if self.text1:
            content += self.text6 + " "
        if self.text1:
            content += self.text7 + " "
        if self.text1:
            content += self.text8 + " "
        if self.text1:
            content += self.text9 + " "
        if self.text1:
            content += self.text10
        content = " ".join(findall(r'[\w ]+', content))
        for w in content.lower().split():
            find_pages = Search.objects.filter(word=w)
            if find_pages:
                find_pages[0].pages.add(Page.objects.get(id=self.parent_id))
                find_pages[0].save()
            else:
                s = Search(word=w)
                s.save()
                s.pages.add(Page.objects.get(id=self.parent_id))
                s.save()


Page.create_content_type(Slider)


class Relation_forarticle(models.Model):
    class Meta:
        verbose_name = "Группа статей"

    pages = models.ManyToManyField(Page, help_text='<b>можно выбрать до 4-х статей.</b><br>', verbose_name="Статьи", blank=False)
    tite = models.CharField(max_length=150, null=True, blank=True, verbose_name='название группы')

    def __str__(self):
        return self.tite if self.tite else "Имя не указано"


class Similar_article(models.Model):
    class Meta:
        verbose_name = "Похожие статьи"
        abstract=True

    title = models.CharField(max_length=150, verbose_name='Заголовок')
    rel = models.ForeignKey(Relation_forarticle, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='группа статей')

    def render(self):
        r = Relation_forarticle.objects.get(similar_article=self.id)
        pages = Page.objects.filter(relation_forarticle=r)
        return render_to_string('widget/similar-articles/widgets-page.html', {'pages':pages, 'title':self.title})


Page.create_content_type(Similar_article)


class Single_column_with_script(models.Model):
    class Meta:
        verbose_name = "Одноколоночный с Скриптом"
        abstract = True

    title = models.CharField(verbose_name='подпись Виджета', max_length=150)
    script = models.TextField(verbose_name='Script', help_text=" Всегда проверяйте скрипт на адекватность. Разработчик сайта не несет ответственность за вставленный скрипт.")
    text = models.TextField(verbose_name='основной текст', default='<p></p>',
                            help_text='''&ltp&gt &lt/p&gt-Тег для выделения
                             &lti&gt &lt/i&gt-курсив &ltb&gt &lt/b&gt-Жирный шрифт ''')

    title2 = models.CharField(max_length=150, verbose_name='заголовок пунктов', blank=True, null=True)
    point = models.TextField(verbose_name='пункты', default='<li></li>',
                             help_text='&ltli&gt &lt/li&gt -Тег для установки точки', null=True, blank=True)

    def render(self):
        return render_to_string('widget/single-column/widgets-page-with-script.html', {'widget':self,
                                                                                        'script':mark_safe(self.script),
                                                                                        'text':mark_safe(self.text),
                                                                                        'point':mark_safe(self.point)})

    def save(self, **kwargs):############################################################################################
        super().save(**kwargs)
        content = self.title + " " + self.text.replace('<p>', '').replace('</p>', '') + " "
        content += self.title2 + " " + self.point.replace('<li>', '').replace('</li>', '')
        content = " ".join(findall(r'[\w ]+', content))
        for w in content.lower().split():
            find_pages = Search.objects.filter(word=w)
            if find_pages:
                find_pages[0].pages.add(Page.objects.get(id=self.parent_id))
                find_pages[0].save()
            else:
                s = Search(word=w)
                s.save()
                s.pages.add(Page.objects.get(id=self.parent_id))
                s.save()


Page.create_content_type(Single_column_with_script)


class Single_column_with_map(models.Model):
    class Meta:
        verbose_name = "Одноколоночный с картой"
        abstract = True

    title = models.CharField(verbose_name='подпись Виджета', max_length=150)
    text = models.TextField(verbose_name='основной текст', default='<p></p>',
                            help_text='''&ltp&gt &lt/p&gt-Тег для выделения
                             &lti&gt &lt/i&gt-курсив &ltb&gt &lt/b&gt-Жирный шрифт''')

    title2 = models.CharField(max_length=150, verbose_name='заголовок пунктов', blank=True, null=True)
    point = models.TextField(verbose_name='пункты', default='<li></li>',
                             help_text='&ltli&gt &lt/li&gt -Тег для установки точки', null=True, blank=True)

    def render(self):
        return render_to_string('widget/single-column/widgets-page-with-map.html', {'widget':self,
                                                                                    'text':mark_safe(self.text),
                                                                                    'point':mark_safe(self.point)})

    def save(self, **kwargs):############################################################################################
        super().save(**kwargs)
        content = self.title + " " + self.text.replace('<p>', '').replace('</p>', '') + " "
        content += self.title2 + " " + self.point.replace('<li>', '').replace('</li>', '')
        content = " ".join(findall(r'[\w ]+', content))
        for w in content.lower().split():
            find_pages = Search.objects.filter(word=w)
            if find_pages:
                find_pages[0].pages.add(Page.objects.get(id=self.parent_id))
                find_pages[0].save()
            else:
                s = Search(word=w)
                s.save()
                s.pages.add(Page.objects.get(id=self.parent_id))
                s.save()


Page.create_content_type(Single_column_with_map)


class Widget_Form_connect_with_us(models.Model):
    class Meta:
        verbose_name = 'Форма обратной связи'
        abstract = True

    def render(self):
        return render_to_string('widget/Widget_Form_connect_with_us/widgets-page.html')


Page.create_content_type(Widget_Form_connect_with_us)


class FAQ(models.Model):
    class Meta:
        verbose_name = "FAQ"

    request = models.CharField(max_length=150, verbose_name='Часто задаваемый вопрос')
    response = models.TextField(verbose_name='Ответ:')

    def __str__(self):
        return self.request


class Encyclopedia_of_knowledge(models.Model):
    class Meta:
        verbose_name = "Энциклопедия знаний"
        verbose_name_plural = "Энциклопедия знаний"

    request = models.CharField(max_length=150, verbose_name='Часто задаваемый вопрос')
    response = models.TextField(verbose_name='Ответ:')

    def __str__(self):
        return self.request


class Link(models.Model):
    class Meta:
        verbose_name = "Ссылка"
        verbose_name_plural = "Ссылки"

    link = models.URLField(verbose_name='Ссылка')
    title = models.CharField(max_length=150, verbose_name='название')

    def __str__(self):
        return self.title


class Connect_with_us(models.Model):
    class Meta:
        verbose_name = 'Форма обратной связи'
        verbose_name_plural = 'Форма обратной связи'

    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    target_message = models.CharField(max_length=200)
    email = models.EmailField()
    text = models.TextField()

    def __str__(self):
        return self.email


class Counter_children(models.Model):
    class Meta:
        verbose_name = 'Счетчик'
        verbose_name_plural = 'Счетчик'

    couner1 = models.IntegerField(default=0)
    couner2 = models.IntegerField(default=0)
    couner3 = models.IntegerField(default=0)
    time = models.IntegerField(default=0)

    def __str__(self):
        return str(self.couner1) + str(self.couner2) + str(self.couner3)
