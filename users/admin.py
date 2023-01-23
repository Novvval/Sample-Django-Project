from functools import partial

from django.contrib import admin
from django.forms import MediaDefiningClass
from django.urls import reverse
from django.utils.html import format_html
from pytz import unicode

from distribution_chain.models import ChainLink, Product
from users.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.

admin.site.register(User, BaseUserAdmin)


class UserAdmin(BaseUserAdmin):
    list_display = ("username", "email", "first_name", "last_name", "is_active")
    search_fields = ("username", "email", "first_name", "last_name")
    readonly_fields = ("last_login", "date_joined")
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal info",
         {"fields": ("is_active", "is_staff", "is_superuser")}),
        ("Important dates",
         {"fields": ("date_joined", "last_login")}
         )
    )


def linkify(field_name):
    """Превращает поле объекта в ссылку"""

    def _linkify(obj):
        linked_obj = getattr(obj, field_name)
        if linked_obj is None:
            return '-'
        app_label = linked_obj._meta.app_label
        model_name = linked_obj._meta.model_name
        view_name = f'admin:{app_label}_{model_name}_change'
        link_url = reverse(view_name, args=[linked_obj.pk])
        return format_html('<a href="{}">{}</a>', link_url, linked_obj)

    _linkify.short_description = field_name
    return _linkify


@admin.action(description='Убрать задолженность')
def remove_owed(modeladmin, request, queryset):
    queryset.update(owed=0.00)


class SupplierInline(admin.StackedInline):
    model = ChainLink


class ProductInline(admin.StackedInline):
    model = Product


class ChainLinkAdmin(admin.ModelAdmin):
    list_display = ("name", "level", "email", "country", "city", "street", "street_number"
                    , "owed", linkify(field_name="supplier"), "created")
    list_filter = ("country", "city")
    actions = [remove_owed]


admin.site.register(ChainLink, ChainLinkAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "model", "release_date")
    search_fields = ("name", "model", "release_date")


admin.site.register(Product, ProductAdmin)
