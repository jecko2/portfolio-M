from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from datetime import date


class CustomUser(AbstractUser):
    username = models.CharField(max_length=50, blank=True, null=True, unique=True)
    email = models.EmailField(_('email address'), unique=True)
    native_name = models.CharField(max_length=5)
    phone_no = models.CharField(max_length=10)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return "{}".format(self.email)


class CreativeDesign(models.Model):
    creative_design = models.TextField()

    def __str__(self):
        return self.creative_design[:70]


class Expertise(models.Model):
    skill_title = models.CharField(max_length=100, )
    skill_level = models.IntegerField(default=0)
    college_learnt = models.CharField(max_length=100, null=True, blank=True)
    skill_mentor = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.skill_title}"


class TeamMember(models.Model):
    profile_pic = models.ImageField(upload_to='media/images/', null=True, blank=True)
    full_name = models.CharField(max_length=100)
    thought = models.TextField()
    email_address = models.EmailField(max_length=255, )

    def __str__(self):
        return self.full_name and self.thought[:20]


class MyselfModel(models.Model):
    profile_pic = models.ImageField(upload_to='media/images/', default='me1.jpg')
    home_img = models.ImageField(upload_to='media/images/')
    full_name = models.CharField(max_length=100, default="Jeckonia Onyango")
    course_doing = models.CharField(max_length=100)
    side_hobby = models.CharField(max_length=100)
    marquee_text_home = models.TextField(default="")
    marquee_text_proj = models.TextField(default="")
    marquee_text_serv = models.TextField(default="")
    school = models.CharField(max_length=100)
    school_link = models.URLField(default='https://www.jkuat.ac.ke')
    school_abbr = models.CharField(max_length=100)
    personal_stat = models.TextField()
    personal_cv = models.FileField(upload_to='media/cvs/', null=True, blank=True)
    address = models.CharField(max_length=100)
    email_address = models.EmailField(max_length=255)
    phone_num = models.IntegerField(default=254745547755, )

    def __str__(self):
        return self.full_name


class MyProject(models.Model):
    PROJ_CATEGORY = (
        ('WEB DEVELOPMENT', 'Web Development'),
        ('HACKING', 'Hacking'),
        ('PROGRAMMING', 'Programing'),
        ('UI/UX', 'Design'),
    )
    project_title = models.CharField(max_length=100)
    project_category = models.CharField(max_length=100, choices=PROJ_CATEGORY)
    project_desc = models.TextField()
    project_image = models.ImageField(upload_to='media/projects/', null=True, blank=True)
    project_tw_link = models.URLField(default='https://twitter.com/PQuinka', null=True, blank=True)
    project_iG_link = models.URLField(default='https://www.instagram.com/pafiquinka/', null=True, blank=True)

    def __str__(self):
        return self.project_title


class Service(models.Model):
    service_icon_name = models.CharField(max_length=100)
    service_name = models.CharField(max_length=100)
    service_desc = models.TextField()

    def __str__(self):
        return self.service_name
