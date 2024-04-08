from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from django.utils.html import format_html
from config import local_settings

from dashboard_student.models import (SemesterRegistrationRequest,
                                      UnitSelectionRequest,
                                      AddRemoveRequest,
                                      EmploymentEducationRequest,
                                      RevisionRequest,
                                      EmergencyRemovalRequest,
                                      StudentDeleteSemesterRequest,
                                      EnrollmentRequest)
from dashboard_student.resource import (SemesterRegistrationRequestResource,
                                        UnitSelectionRequestResource,
                                        AddRemoveRequestResource,
                                        RevisionRequestResource,
                                        EmergencyRemovalRequestResource,
                                        StudentDeleteSemesterRequestResource,
                                        EnrollmentRequestResource,
                                        EmploymentEducationRequestResource)


class SemesterRegistrationRequestAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'student_link', 'semester_link', 'approval_status')
    list_filter = ('approval_status',)
    list_editable = ('approval_status',)
    ordering = ('id',)
    search_fields = ('student', 'semester')
    search_help_text = "Search in: Student, Semester"
    resource_class = SemesterRegistrationRequestResource
    list_display_links = ('id', 'student_link', 'semester_link')
    save_as = True
    list_per_page = 10
    list_max_show_all = 50

    def student_link(self, obj):
        student_id = obj.student.id
        student_url = f"http://127.0.0.1:8000/{local_settings.Admin}accounts/student/{student_id}/change/"

        return format_html('<a href="{}">{}</a>', student_url, obj.student)
    
    def semester_link(self, obj):
        semester_id = obj.semester.id
        semester_url = f"http://127.0.0.1:8000/{local_settings.Admin}education/semester/{semester_id}/change/"

        return format_html('<a href="{}">{}</a>', semester_url, obj.semester)
    
    student_link.short_description = "Student"
    semester_link.short_description = "Semester"

admin.site.register(SemesterRegistrationRequest, SemesterRegistrationRequestAdmin)


class UnitSelectionRequestAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'semester_registration_request_link', 'approval_status')
    list_filter = ('approval_status',)
    sortable_by = ('id',)
    list_editable = ('approval_status',)
    ordering = ('id',)
    resource_class = UnitSelectionRequestResource
    list_display_links = ('id', 'semester_registration_request_link')
    save_as = True
    list_per_page = 10
    list_max_show_all = 50

    def semester_registration_request_link(self, obj):
        semester_registration_request_id = obj.semester_registration_request.id
        semester_registration_request_url = f"http://127.0.0.1:8000/{local_settings.Admin}dashboard_student/\
        semesterregistrationrequest/{semester_registration_request_id}/change/"

        return format_html('<a href="{}">{}</a>', semester_registration_request_url,
                           obj.semester_registration_request)
    
    semester_registration_request_link.short_description = "Semester Registration Request"
    
admin.site.register(UnitSelectionRequest, UnitSelectionRequestAdmin)


class AddRemoveRequestAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'semester_registration_request_link', 'approval_status')
    list_filter = ('approval_status',)
    sortable_by = ('id',)
    list_editable = ('approval_status',)
    ordering = ('id',)
    resource_class = AddRemoveRequestResource
    list_display_links = ('id', 'semester_registration_request_link')
    save_as = True
    list_per_page = 10
    list_max_show_all = 50

    def semester_registration_request_link(self, obj):
        semester_registration_request_id = obj.semester_registration_request.id
        semester_registration_request_url = f"http://127.0.0.1:8000/{local_settings.Admin}dashboard_student/\
        semesterregistrationrequest/{semester_registration_request_id}/change/"

        return format_html('<a href="{}">{}</a>', semester_registration_request_url,
                           obj.semester_registration_request)
    
    semester_registration_request_link.short_description = "Semester Registration Request"

admin.site.register(AddRemoveRequest,AddRemoveRequestAdmin)


class RevisionRequestAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'student_link', 'student_course_link', 'teacher_approval_status',
                    'educational_assistant_approval_status')
    list_filter = ('teacher_approval_status',)
    sortable_by = ('student', 'course')
    list_editable = ('teacher_approval_status', 'educational_assistant_approval_status')
    ordering = ('created_at',)
    resource_class = RevisionRequestResource
    list_display_links = ('id', 'student_link', 'student_course_link')
    save_as = True
    list_per_page = 10
    list_max_show_all = 50

    def student_link(self, obj):
        student_id = obj.student.id
        student_url = f"http://127.0.0.1:8000/{local_settings.Admin}accounts/student/{student_id}/change/"

        return format_html('<a href="{}">{}</a>', student_url, obj.student)

    def student_course_link(self, obj):
        student_course_id = obj.course.id
        student_course_url = f"http://127.0.0.1:8000/{local_settings.Admin}education/studentcourse/\
        {student_course_id}/change/"

        return format_html('<a href="{}">{}</a>', student_course_url, obj.course)

    student_link.short_description = "Student"
    student_course_link.short_description = "Student Course"

admin.site.register(RevisionRequest, RevisionRequestAdmin)


class EmergencyRemovalRequestAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'student_link', 'student_course_link', 'approval_status',
                    'student_explanation', 'educational_assistant_explanation')
    list_filter = ('approval_status',)
    sortable_by = ('student', 'course')
    list_editable = ('approval_status',)
    ordering = ('created_at',)
    resource_class = EmergencyRemovalRequestResource
    list_display_links = ('id', 'student_link', 'student_course_link')
    search_fields = ('student_explanation',
                     'educational_assistant_explanation')
    search_help_text = "Search in: Student Explanation, Educational Assistant Explanation"
    save_as = True
    list_per_page = 10
    list_max_show_all = 50

    def student_link(self, obj):
        student_id = obj.student.id
        student_url = f"http://127.0.0.1:8000/{local_settings.Admin}accounts/student/{student_id}/change/"

        return format_html('<a href="{}">{}</a>', student_url, obj.student)

    def student_course_link(self, obj):
        student_course_id = obj.course.id
        student_course_url = f"http://127.0.0.1:8000/{local_settings.Admin}education/studentcourse/\
        {student_course_id}/change/"

        return format_html('<a href="{}">{}</a>', student_course_url, obj.course)

    student_link.short_description = "Student"
    student_course_link.short_description = "Student Course"

admin.site.register(EmergencyRemovalRequest, EmergencyRemovalRequestAdmin)


class StudentDeleteSemesterRequestAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'semester_registration_request_link', 'teacher_approval_status',
                    'educational_assistant_approval_status', 
                    'student_explanations', 'educational_assistant_explanation')
    list_filter = ('teacher_approval_status', 'educational_assistant_approval_status')
    list_editable = ('teacher_approval_status', 'educational_assistant_approval_status')
    ordering = ('created_at',)
    list_display_links = ('id', 'semester_registration_request_link')
    resource_class = StudentDeleteSemesterRequestResource
    search_fields = ('student_explanations',
                     'educational_assistant_explanation')
    search_help_text = "Search in: Student Explanation, Educational Assistant Explanation"
    save_as = True
    list_per_page = 10
    list_max_show_all = 50

    def semester_registration_request_link(self, obj):
        semester_registration_request_id = obj.semester_registration_request.id
        semester_registration_request_url = f"http://127.0.0.1:8000/{local_settings.Admin}dashboard_student/\
        semesterregistrationrequest/{semester_registration_request_id}/change/"

        return format_html('<a href="{}">{}</a>', semester_registration_request_url,
                           obj.semester_registration_request)
    
    semester_registration_request_link.short_description = "Semester Registration Request"

admin.site.register(StudentDeleteSemesterRequest,
                    StudentDeleteSemesterRequestAdmin)


class EnrollmentRequestAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'student_link', 'teacher_link', 'approval_status', 'reason_text')
    list_filter = ('approval_status',)
    sortable_by = ('student', 'teacher')
    list_editable = ('approval_status',)
    ordering = ('created_at',)
    list_display_links = ('id', 'student_link', 'teacher_link')
    resource_class = EnrollmentRequestResource
    search_fields = ('teacher', 'reason_text')
    search_help_text = "Search in: Teacher, Reason Text"
    save_as = True
    list_per_page = 10
    list_max_show_all = 50

    def student_link(self, obj):
        student_id = obj.student.id
        student_url = f"http://127.0.0.1:8000/{local_settings.Admin}accounts/student/{student_id}/change/"

        return format_html('<a href="{}">{}</a>', student_url, obj.student)
    
    def teacher_link(self, obj):
        teacher_id = obj.teacher.id
        teacher_url = f"http://127.0.0.1:8000/{local_settings.Admin}accounts/teacher/{teacher_id}/change/"

        return format_html('<a href="{}">{}</a>', teacher_url, obj.teacher)
    
    student_link.short_description = "Student"
    teacher_link.short_description = "Teacher"

admin.site.register(EnrollmentRequest, EnrollmentRequestAdmin)


class EmploymentEducationRequestAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'student_link', 'approval_status', 'need_for')
    list_filter = ('approval_status',)
    sortable_by = ('student',)
    list_editable = ('approval_status',)
    ordering = ('created_at',)
    list_display_links = ('id', 'student_link')
    resource_class = EmploymentEducationRequestResource
    search_fields = ('need_for',)
    search_help_text = "Search in: Reason Text"
    save_as = True
    list_per_page = 10
    list_max_show_all = 50

    def student_link(self, obj):
        student_id = obj.student.id
        student_url = f"http://127.0.0.1:8000/{local_settings.Admin}accounts/student/{student_id}/change/"

        return format_html('<a href="{}">{}</a>', student_url, obj.student)
    
    student_link.short_description = "Student"

admin.site.register(EmploymentEducationRequest, EmploymentEducationRequestAdmin)
