from django.contrib import admin
from .models import Network_security_links, Help_for_addicts_links, To_contact_us, ContactInformation, Partners


class Help_for_addicts_links_admin(admin.ModelAdmin):
    class Media:
        js = ('jsmainpage/Help_for_addicts.js',)


class Network_security_links_admin(admin.ModelAdmin):
    class Media:
        js = ('jsmainpage/Network_security.js',)


class ContactInformation_admin(admin.ModelAdmin):
    class Media:
        js = ('jsmainpage/ContactInformation.js',)

    exclude = ['flag']


class Partners_admin(admin.ModelAdmin):
    list_display = ['link', 'get_img']


admin.site.register(Help_for_addicts_links, Help_for_addicts_links_admin)
admin.site.register(Network_security_links, Network_security_links_admin)
admin.site.register(To_contact_us)
admin.site.register(ContactInformation, ContactInformation_admin)
admin.site.register(Partners, Partners_admin)
# Register your models here.
