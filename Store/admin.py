from django.contrib import admin
from .models import *


class WaschmaschineAdmin(admin.ModelAdmin):
    search_fields = ['name', 'model', 'fassung', 'preis',]
    list_display = ['name', 'fassung', 'model']


class SpuelmaschineAdmin(admin.ModelAdmin):
    search_fields = ['name', 'model', 'breite', 'art']
    list_display = ["name", "breite", 'art', 'model']


class BackofenAdmin(admin.ModelAdmin):
    search_fields = ['name', 'model']
    list_display = ['name', 'model']


class BackofenHerdAdmin(admin.ModelAdmin):
    search_fields = ['name', 'model']
    list_display = ['name', 'model', 'iduktion']


class KuehlschrankAdmin(admin.ModelAdmin):
    search_fields = ['name', 'model', 'type']
    list_display = ['name', 'type', 'model']


class VerkaufenAdmin(admin.ModelAdmin):
    search_fields = ['product']


# Register your models here.
admin.site.register(Waschmaschine, WaschmaschineAdmin)
admin.site.register(Spuelmaschine, SpuelmaschineAdmin)
admin.site.register(Backofen, BackofenAdmin)
admin.site.register(BackofenHerd, BackofenHerdAdmin)
admin.site.register(Kuehlschrank, KuehlschrankAdmin)
admin.site.register(Verkaufen, VerkaufenAdmin)
