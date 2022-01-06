from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import (CustomUser, Expertise, TeamMember,
                     CreativeDesign, MyselfModel, MyProject,
                     Service
                     )


class UserAdmin1(BaseUserAdmin):
    # form = UserChangeForm
    fieldsets = (
        ('User', {'fields': ('email',)}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('user_info'), {'fields': ('native_name', 'phone_no')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ['email', 'first_name', 'last_name', 'is_staff', "native_name", "phone_no"]
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)


class ExpertAdmin(admin.ModelAdmin):
    list_display = ['skill_title', 'skill_level', 'college_learnt', 'skill_mentor']


class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'thought', ]


class MyselfAdmin(admin.ModelAdmin):
    list_display = ['full_name',
                    'course_doing',
                    'side_hobby',
                    'school_abbr',
                    'email_address',
                    'phone_num']


class MyProjectAdmin(admin.ModelAdmin):
    list_display = ['project_title', 'project_tw_link', 'project_iG_link']


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['service_name', ]


admin.site.register(CustomUser, UserAdmin1)
admin.site.register(Expertise, ExpertAdmin)
admin.site.register(TeamMember, TeamMemberAdmin)
admin.site.register(CreativeDesign)
admin.site.register(MyselfModel, MyselfAdmin)
admin.site.register(MyProject, MyProjectAdmin)
admin.site.register(Service, ServiceAdmin)
