from django.contrib import admin
from nested_admin import NestedStackedInline, NestedModelAdmin
from index.models import *
# Register your models here.
'''
admin.site.register(Journal)
admin.site.register(Volume)
admin.site.register(Issue)
admin.site.register(Article)

class VolumeInline(admin.TabularInline):
    model = Volume   

class IssueInline(admin.StackedInline):
    model = Issue

class ArticleInline(admin.StackedInline):
    model = Article

class JournalsAdmin(admin.ModelAdmin):
    inlines = [VolumeInline, IssueInline, ArticleInline]
'''

class ArticleInline(NestedStackedInline):
    model = Article
    extra = 1
    fk_name = 'volume'

class IndexingInline(NestedStackedInline):
    model = Indexing
    extra = 1
    fk_name = 'journal'

class ImpactFactorInline(NestedStackedInline):
    model = ImpactFactor
    extra = 1
    fk_name = 'journal'

class VolumeInline(NestedStackedInline):
    model = Volume
    extra = 1
    fk_name = 'journal'
    inlines = [ArticleInline,]

class EditorInline(NestedStackedInline):
    model = Editor
    extra = 1
    fk_name = 'journal'

class JournalAdmin(NestedModelAdmin):
    list_display = ('journal_name', 'journal_url', 'subject', 'language', 'origin_country')
    model = Journal
    inlines = [IndexingInline, ImpactFactorInline, EditorInline,VolumeInline]




class JournalFeeAdmin(admin.ModelAdmin):
    list_display = ('journal', 'usd', 'inr',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()  

class TestimonyAdmin(admin.ModelAdmin):
    list_display = ('testimony', 'testimony_name', 'testimony_desg')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()  

class TopEditorAdmin(admin.ModelAdmin):
    list_display = ('editor_name', 'designation')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()  

class TopReviewerAdmin(admin.ModelAdmin):
    list_display = ('reviewer_name', 'designation')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()  

class FeaturedArticleAdmin(admin.ModelAdmin):
    list_display = ('article_name', 'author', 'publish_date')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = () 

class AuthorOfTheMonthAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'author_desg', 'last_updated',)
    readonly_fields = ('last_updated',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = () 

class GlobalIndexingAdmin(admin.ModelAdmin):
    list_display = ('index_name', 'index_picture', 'index_url',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Journal, JournalAdmin)
admin.site.register(TopEditor, TopEditorAdmin)
admin.site.register(FeaturedArticle, FeaturedArticleAdmin)
admin.site.register(JournalFee, JournalFeeAdmin)
admin.site.register(AuthorOfTheMonth, AuthorOfTheMonthAdmin)
admin.site.register(GlobalIndexing, GlobalIndexingAdmin)

