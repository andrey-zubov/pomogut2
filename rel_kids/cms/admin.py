from django.contrib import admin
from .models import Block, Category, Map, Relation_forarticle, FAQ, Link, Encyclopedia_of_knowledge, Connect_with_us, Counter_children
from feincms.admin import tree_editor
#from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django_ymap.admin import YmapAdmin


class BlockAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    fields = ["title", "slug", "picture", "text", "name_button", "categories", "pages"]
    list_display = ['title', 'name_button', 'text']

    class Media:
        js = ('js/ForBlock.js',)


admin.site.register(Block, BlockAdmin)


class CategoryAdmin(tree_editor.TreeEditor):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'get_img']
    list_filter = ['parent']

    class Media:
        js = ('js/ForCategory.js',)


admin.site.register(Category, CategoryAdmin)


class MapAdmin(YmapAdmin, admin.ModelAdmin):
    list_filter = ('title',)
    list_display = ('title', 'description')


admin.site.register(Map, MapAdmin)


class Relation_forarticle_Admin(admin.ModelAdmin):
    class Media:
        js = ('js/ForRelation_forarticle.js',)


admin.site.register(Relation_forarticle, Relation_forarticle_Admin)

admin.site.register(FAQ)
admin.site.register(Link)
admin.site.register(Encyclopedia_of_knowledge)
admin.site.register(Connect_with_us)
