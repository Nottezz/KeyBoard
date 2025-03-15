from django.contrib import admin

from .models import Category, KeyBoard, Specification

admin.register(Specification)
admin.register(Category)


@admin.register(KeyBoard)
class KeyBoardAdmin(admin.ModelAdmin):
    fields = [
        "name",
        "slug",
        "photo",
        "description",
        "is_published",
        "category",
        "price",
        "counter",
        "specifications",
        "equipments",
        "created_at",
        "updated_at",
    ]
    readonly_fields = [
        "created_at",
        "updated_at",
    ]
    prepopulated_fields = {"slug": ("name",)}
    list_display = [
        "name",
        "category",
        "is_published",
        "counter",
        "created_at",
        "updated_at",
    ]
    list_display_links = [
        "name",
    ]
    search_fields = ["name", "category"]
    save_on_top = True


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )
    list_display_links = (
        "id",
        "name",
    )
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Specification)
class SpecificationAdmin(admin.ModelAdmin):
    fields = [
        "name",
        "key_material",
        "size",
        "number_of_keys",
        "os_compatibility",
        "backlight",
        "connection_interface",
        "weight",
        "country_of_manufacture",
        "brand",
    ]
    list_display = ["name", "brand"]
    search_fields = ["name", "brand"]
