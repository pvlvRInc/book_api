from django.contrib import admin

from books.models import Books, Artists, Companies, Series, Genres, Tags, Commentary, UserBookRating, Quote, UserProfile


class BookAdmin(admin.ModelAdmin):
    pass



admin.site.register(Books, BookAdmin)
admin.site.register(Artists)
admin.site.register(Companies)
admin.site.register(Series)
admin.site.register(Genres)
admin.site.register(Tags)
admin.site.register(Commentary)
admin.site.register(UserBookRating)
admin.site.register(Quote)
admin.site.register(UserProfile)
