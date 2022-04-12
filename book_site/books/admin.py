from django.contrib import admin

from books.models import Books, Artists, Companies, Series, Genres, Tags, Commentary, UserBookRating, Quote, UserProfile


@admin.register(Books)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'cover', 'created_at', 'publish_year', 'price', 'rating', 'downloads', 'type', 'status')
    readonly_fields = ('rating', 'downloads', 'created_at')
    list_filter = ('type', 'status')
    search_fields = ('title',)



admin.site.register(Artists)
admin.site.register(Companies)
admin.site.register(Series)
admin.site.register(Genres)
admin.site.register(Tags)
admin.site.register(Commentary)
admin.site.register(UserBookRating)
admin.site.register(Quote)
admin.site.register(UserProfile)
