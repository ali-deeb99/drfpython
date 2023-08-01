from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Student(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username


class Company(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    company_name=models.CharField(max_length=128)

    def __str__(self):
        return self.user.username

class Teacher(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    decription=models.TextField(blank=False)
    # education=models.TextField(blank=False)
    # teaching_experience=models.TextField(blank=False)
    # teaching_philosophy=models.TextField(blank=False)
    # technical_skills=models.TextField(blank=False)
    # cv=models.FileField(blank=False)

    def __str__(self):
        return self.user.username

class ApplicationForm(models.Model):
    entity_name=models.CharField(max_length=100,unique=True)
    contact_person_name=models.CharField(max_length=100)
    contact_person_email=models.EmailField(unique=True)
    contact_person_phone_number=models.CharField(max_length=100,unique=True)
    brief_decription_of_the_entity=models.TextField()
    website_url=models.URLField(unique=True)
    type_of_courses_pathes_plan_to_create=models.TextField()
    target_audience_for_courses_paths=models.TextField()
    Proposed_course_name=models.CharField(max_length=100)
    brief_description_of_the_course=models.TextField()
    estimated_number_of_course_programes_plan_to_create=models.IntegerField(blank=True,null=True)
    estimated_timeline_for_course_program_creation=models.DateField()
    content_delivery_format=models.TextField()
    any_existing_courses_programes_they_have_created_before=models.TextField(blank=True)
    any_reviews=models.TextField(blank=True)
    any_additional_information=models.TextField(blank=True)




class Path(models.Model):
    Choices=(('1','Beginner'),('2','Intermidiate'),('3','Advansed'))
    path_name=models.CharField(max_length=255)
    description=models.TextField()
    requirements=models.TextField()
    rating=models.DecimalField(max_digits=6,decimal_places=2)
    level=models.CharField(max_length=20,choices = Choices,
default = '1')
    teacher_username=models.ForeignKey(Teacher,on_delete=models.RESTRICT)

    def __str__(self):
        return self.path_name

class Course(models.Model):
    Choices=(('1','Beginner'),('2','Intermidiate'),('3','Advansed'))
    course_name=models.CharField(max_length=255)
    description=models.TextField()
    requirements=models.TextField()
    rating=models.DecimalField(max_digits=1,decimal_places=1)
    level=models.CharField(max_length=20,choices=Choices,default='1')
    teacher_username=models.ForeignKey(Teacher,on_delete=models.RESTRICT)

    def __str__(self):
        return self.course_name

class Section(models.Model):
    name_of_the_section=models.CharField(max_length=128)
    number_of_videos=models.IntegerField()
    time_of_videos=models.IntegerField()
    number_of_readings=models.IntegerField()
    time_of_readings=models.IntegerField()
    rating=models.DecimalField(max_digits=1,decimal_places=1)
    number_of_quizes=models.IntegerField()
    number_of_assignments=models.IntegerField()
    teacher_username=models.ForeignKey(Teacher,on_delete=models.RESTRICT)

    def __str__(self):
        return self.name_of_the_section


class Content(models.Model):
    Choices=(('1','Reading'),('2','Video'),('3','Quiz'),('4','Assignment'))
    content_name=models.CharField(max_length=128)
    content_time=models.IntegerField()
    content_type=models.CharField(max_length=20,choices=Choices)
    teacher_username=models.ForeignKey(Teacher,on_delete=models.RESTRICT)
    
    def __str__(self):
        return self.content_name


class ReadingContent(models.Model):
    content_name=models.OneToOneField(Content,on_delete=models.CASCADE)
    reading=models.TextField()

    def __str__(self):
        return self.content_name.content_name
    

class SectionContent(models.Model):
    section_name=models.ForeignKey(Section,on_delete=models.CASCADE)
    content_name=models.ForeignKey(Content,on_delete=models.CASCADE)
    order_of_content=models.IntegerField()
    class Meta:
        unique_together=('section_name','content_name')

    def __str__(self):
        return self.section_name.name_of_the_section + self.content_name.content_name


class Tag(models.Model):
    tag_name=models.CharField(max_length=128)

    def __str__(self):
        return self.tag_name


class TagSection(models.Model):
    section_name=models.ForeignKey(Section,on_delete=models.CASCADE)
    tage_name=models.ForeignKey(Tag,on_delete=models.RESTRICT)
    class Meta:
       unique_together=('section_name','tage_name') 

    def __str__(self):
        return self.section_name.name_of_the_section + self.tage_name.tag_name


class CourseSection(models.Model):
    course_name=models.ForeignKey(Course,on_delete=models.CASCADE)
    section_name=models.ForeignKey(Section,on_delete=models.CASCADE)
    order_of_section=models.IntegerField()
    class Meta:
        unique_together=('course_name','section_name')

    def __str__(self):
        return self.course_name.course_name + self.section_name.name_of_the_section
        

class PathCourse(models.Model):
    path_name=models.ForeignKey(Path,on_delete=models.CASCADE)
    course_name=models.ForeignKey(Course,on_delete=models.CASCADE)
    order_of_course=models.IntegerField()
    class Meta:
        unique_together=('path_name','course_name')

    def __str__(self):
        return self.path_name.path_name + self.course_name.course_name

class TeacherCourse(models.Model):
    teacher_username=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    course_name=models.ForeignKey(Course,on_delete=models.CASCADE)
    class Meta:
        unique_together=('teacher_username','course_name')

    def __str__(self):
        return self.teacher_username.user.username + self.course_name.course_name



class Test(models.Model):
    x=models.IntegerField()
    y=models.IntegerField(blank=True)
    # def __str__(self):
    #     return self.x


class Blog(models.Model):
    title=models.CharField(max_length=255)
    content=models.TextField()
    added_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False,null=False,blank=False)    
    slug = models.SlugField(null=True,blank=True)

    def __str__(self):
        return self.title
    class Meta:
        #verbose_name='My Blog'
        verbose_name_plural='My Blogs'


class Obada(models.Model):
    name=models.CharField(max_length=255)





