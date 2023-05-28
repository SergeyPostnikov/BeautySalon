from django.contrib import admin
from django.shortcuts import reverse
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from .models import Salon
from .models import Profession
from .models import Master
from .models import CategoryService
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
    fields = [
        'name',
        'address',
        'working_time_from',
        'working_time_to',
        'image',
        'preview'
    ]
    readonly_fields = [
        "preview"
    ]

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="max-height: 200px;">')


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
    fields = [
        'fullname',
        'profession',
        'work_duration',
        'photo',
        'preview'
    ]
    readonly_fields = [
        "preview"
    ]

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.photo.url}" style="max-height: 200px;">')


@admin.register(CategoryService)
class CategoryServiceAdmin(admin.ModelAdmin):
    list_display = [
        'name',
    ]


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    search_fields = [
        'name'
    ]
    fields = [
        'name',
        'description',
        'price',
        'master',
        'image',
        'preview'
    ]
    readonly_fields = [
        "preview"
    ]

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="max-height: 200px;">')


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
