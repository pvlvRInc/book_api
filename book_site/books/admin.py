from django.contrib import admin
from django.utils.safestring import mark_safe

from books.models import Books, Artists, Companies, Series, Genres, Tags, Commentary, UserBookRating, Quote, UserProfile


@admin.register(Books)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'cover_mini', 'created_at', 'publish_year', 'book_series', 'price', 'rating', 'downloads', 'type', 'status')
    readonly_fields = ('rating', 'downloads', 'created_at')
    list_filter = ('type', 'status')
    search_fields = ('title',)

    def cover_mini(self, obj):
        if obj.cover:
            return mark_safe(f'<img src="{obj.cover.url}" width="75">')

    cover_mini.short_description = 'Обложка'


@admin.register(Artists)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'email', 'created_at', 'type')
    readonly_fields = ('created_at', )
    list_filter = ('type', )
    search_fields = ('fullname', 'email')

    def fullname(self, obj):
        return str(obj)

    fullname.short_description = 'Полное имя'

@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ('book', 'ip', 'user', 'parent', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('book', 'user')
    # todo filter by anonymous users

admin.site.register(Companies)
admin.site.register(Series)
admin.site.register(Genres)
admin.site.register(Tags)


admin.site.register(UserBookRating)
admin.site.register(Quote)
admin.site.register(UserProfile)
