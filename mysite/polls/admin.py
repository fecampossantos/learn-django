from django.contrib import admin

from .models import Choice, Question

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    # this organizes what will be shown in the header
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # this is for further organization on the page
    list_filter = ['pub_date'] ## filtering
    search_fields = ['question_text'] ## searching

admin.site.register(Question, QuestionAdmin)