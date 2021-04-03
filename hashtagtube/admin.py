from django.contrib import admin
from hashtagtube.models import Category, Page

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

class PageAdmin(admin.ModelAdmin):

    list_display = ('thumbnail', 'title', 'category', 'author' )

admin.site.register(Category)
admin.site.register(Page)
