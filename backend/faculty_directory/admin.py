from django.contrib import admin
from .models import contact_herosection, Contact

@admin.register(contact_herosection)
class ContactHeroSectionAdmin(admin.ModelAdmin):
    search_fields = ('title', 'uni_name')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_filter = ('category', 'is_active')
    search_fields = ('name', 'email', 'phone', 'office', 'location')
