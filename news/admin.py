from django.contrib import admin
from .models import Editor,Article,tags

class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal =('tags',)


    
admin.site.register(Editor)
admin.site.register(Article)
admin.site.register(tags)


# Register your models here.
# . dot - Matches any single character.
# \d - Matches any single digit.
# [A-Z] - Matches all characters between A-Z uppercase.
# [a-z] - Matches all characters between a-z lowercase.
# [A-Za-z] - Matches all characters between a-z case Insensitive.
# + - Matches one or more of previous expression ie.\d+.
# [n/]+ - Matches one or more characters not including a forward slash
# ? - Matches zero or one of previous expression ie. \d?.
# * - Matches Zero or more of previous expression ie. \d*.
# {1-3} - Matches between one and three digits inclusive of previous expression ie \d{1,6}.