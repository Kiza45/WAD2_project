from django.contrib import admin
from hashtagtube.models import Category, Page
from hashtagtube.models import UserProfile

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

class PageAdmin(admin.ModelAdmin):

    list_display = ('thumbnail', 'title', 'category', 'author' )

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)

