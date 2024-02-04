from django.contrib import admin

from .models import Coin, Author, Post


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'last_name', 'birthday']
    ordering = ['name', '-birthday']
    list_filter = ['name', 'birthday']
    search_fields = ['name']
    search_help_text = 'Serch by name'

    readonly_fields = ['birthday']

    fieldsets = [
        (
            'Author',
            {
                'classes': ['wide'],
                'fields': ['name', 'last_name'],
            },
        ),
        (
            'Details',
            {
                'classes': ['collapse'],
                'description': 'Biography',
                'fields': ['birthday', 'bio'],
            },
        ),
        (
            'Other info',
            {
                'description': 'Contact info',
                'fields': ['email'],
            }
        ),
    ]


class PostAdmin(admin.ModelAdmin):

    @admin.action(description='Reset all authors posts')
    def reset_content(modeladmin, request, queryset):
        queryset.update(content='')

    list_display = ['title', 'content', 'author']
    ordering = ['title', 'author']
    list_filter = ['title', 'author']
    search_fields = ['title']
    search_help_text = 'Serch by author'
    actions = [reset_content]

    readonly_fields = ['is_published']

    fieldsets = [
        (
            'Post',
            {
                'classes': ['wide'],
                'fields': ['title', 'content'],
            },
        ),
        (
            'Details',
            {
                'classes': ['collapse'],
                'description': 'Autor',
                'fields': ['author'],
            },
        ),
        (
            'Other info',
            {
                'description': 'Other info',
                'fields': ['is_published', 'views'],
            }
        ),
    ]




admin.site.register(Coin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Post, PostAdmin)

