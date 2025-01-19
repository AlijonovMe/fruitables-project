from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *

admin.site.site_header = "Fruitables"


@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name')
    list_display_links = ('id', 'username')


class CategoryInline(admin.TabularInline):
    model = Category
    prepopulated_fields = {'slug': ('name',)}
    extra = 0


@admin.register(Departament)
class DepartamentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name')
    prepopulated_fields = {'slug': ('name',)}

    inlines = [
        CategoryInline
    ]

    def get_fieldsets(self, request, obj=None):
        field = [("Bo'lim", {'fields': ['name', 'slug']})]
        return field


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0
    min_num = 1
    validate_min = True


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'currency', 'price', 'discount', 'quantity', 'quality', 'weight', 'category', 'get_image')
    list_display_links = ('id', 'name')
    prepopulated_fields = {'slug': ('name',)}

    inlines = [ProductImageInline]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "category":
            if Category.objects.all().exists():
                kwargs['empty_label'] = 'Tanlang'
            else:
                kwargs['empty_label'] = "Mavjud emas"
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def formfield_for_choice_field(self, db_field, request, **kwargs):
        if db_field.name == "weight" or db_field.name == "currency":
            kwargs['choices'] = db_field.get_choices(
                include_blank=True,
                blank_choice=[("", "Tanlang")]
            )
        return super().formfield_for_choice_field(db_field, request, **kwargs)

    def get_fieldsets(self, request, obj=None):
        fields = [field.name for field in Product._meta.fields if field.name != 'id']
        return [("Mahsulot", {'fields': fields})]

    def get_image(self, product):
        images = product.images.all()
        if images.exists():
            return mark_safe(f'<img src="{images.first().image.url}" width="50px">')
        return ''

    get_image.short_description = 'Surati'
