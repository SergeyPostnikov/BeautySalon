from django.contrib import admin
from django.shortcuts import reverse
from django.utils.html import format_html

from .models import Salon
from .models import Profession
from .models import Master
from .models import Service
from .models import Client
from .models import Review
from .models import Order


@admin.register(Salon)
class SalonAdmin(admin.ModelAdmin):
    search_fields = [
        'name',
        'address'
    ]
    list_display = [
        'name',
        'address',
        'working_time_from',
        'working_time_to'
    ]

    def get_image_preview(self, obj):
        if not obj.image:
            return 'выберите картинку'
        return format_html('<img src="{url}" style="max-height: 200px;"/>', url=obj.image.url)
    get_image_preview.short_description = 'превью'


@admin.register(Profession)
class ProfessionAdmin(admin.ModelAdmin):
    list_display = [
        'name',
    ]


@admin.register(Master)
class MasterAdmin(admin.ModelAdmin):
    search_fields = [
        'fullname',
        'profession'
    ]
    list_display = [
        'fullname',
        'profession',
        'work_duration'
    ]
    readonly_fields = [
        'get_image_preview',
    ]

    def get_image_preview(self, obj):
        if not obj.photo:
            return 'выберите картинку'
        return format_html('<img src="{url}" style="max-height: 200px;"/>', url=obj.photo.url)
    get_image_preview.short_description = 'превью'


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    search_fields = [
        'name'
    ]
    list_display = [
        'name',
        'description',
        'price'
    ]

    def get_image_preview(self, obj):
        if not obj.image:
            return 'выберите картинку'
        return format_html('<img src="{url}" style="max-height: 200px;"/>', url=obj.image.url)
    get_image_preview.short_description = 'превью'


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    search_fields = [
        'name',
        'phone'
    ]
    list_display = [
        'name',
        'phone'
    ]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    search_fields = [
        'salon'
    ]
    list_display = [
        'name',
        'text',
        'date',
        'salon'
    ]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    search_fields = [
        'client'
    ]
    list_display = [
        'client',
        'service',
        'date',
        'time'
    ]
