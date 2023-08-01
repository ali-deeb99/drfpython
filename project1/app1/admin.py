from django.contrib import admin
from .models import Student,Company,Teacher,Path,Course,Section,Content,ReadingContent,SectionContent,Tag,TagSection,CourseSection,PathCourse,TeacherCourse,Test,Blog,Obada,ApplicationForm
# Register your models here.




class TestAdmin(admin.ModelAdmin):
      def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(id=request.user.id)

class CourseAdmin(admin.ModelAdmin):
     def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(teacher_username__user=request.user)
      

class BlogAdmin(admin.ModelAdmin):
      list_display =    ('title','added_date','updated_date','is_published')
      list_per_page=25
      search_fields=['is_published','title']
      list_filter=['is_published']
      date_hierarchy = 'updated_date'


admin.site.register(Blog,BlogAdmin)
admin.site.register(Test,TestAdmin)
admin.site.register(Course,CourseAdmin)
admin.site.register([Student,Company,Teacher,Path,Section,Content,ReadingContent,SectionContent,Tag,TagSection,CourseSection,PathCourse,TeacherCourse,Obada,ApplicationForm])
