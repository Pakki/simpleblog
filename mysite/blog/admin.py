from django.contrib import admin
from .models import Category, Tag, Post, ViewsCount
from ckeditor_uploader.widgets import CKEditorUploadingWidget
#from ckeditor.widgets import CKEditorWidget
from django import forms


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug',)
    prepopulated_fields = {"slug": ("title",)}
    list_display_links = ('id', 'title',)


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug',)
    prepopulated_fields = {"slug": ("title",)}
    list_display_links = ('id', 'title',)


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    
    class Meta:
        model = Post
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ('id', 'title', 'slug', 'created_at', 'category',)
    prepopulated_fields = {"slug": ("title",)}
    list_display_links = ('id', 'title',)


class ViewsCountAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(ViewsCount, ViewsCountAdmin)

