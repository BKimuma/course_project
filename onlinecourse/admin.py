from django.contrib import admin
# <HINT> Import any new Models here
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission

# <HINT> Register QuestionInline and ChoiceInline classes here


class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5


# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'course']
    search_fields = ['title', 'course']
    
    def lesson_number(self, obj):
        return obj.id
    
    lesson_number.short_description = 'Lesson Number'

class LearnerAdmin(admin.ModelAdmin):
    list_display = ['user']


admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner, LearnerAdmin)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Submission)
