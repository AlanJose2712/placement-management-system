from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('placement-login/', views.placement_login, name='placement_login'),
    path('student-login/', views.student_login, name='student_login'),
    path('alumni-login/', views.alumni_login, name='alumni_login'),
    path('alumni-signup/', views.alumni_signup, name='alumni_signup'),
    path('student_signup/', views.student_signup, name='student_signup'),
    
    # Dashboard URLs
    path('alumni-dashboard/', views.alumni_dashboard, name='alumni_dashboard'),
    path('placement-dashboard/', views.placement_dashboard, name='placement_dashboard'),
    path('student-dashboard/', views.student_dashboard, name='student_dashboard'),
    path('student_forgot/', views.student_forgot, name='student_forgot'),
    path('student_password/', views.student_password, name='student_password'),

    # Placement officer pages
    path('pl_placement_details/', views.pl_placement_details, name='pl_placement_details'),
    path('pl_student_profile/', views.pl_student_profile, name='pl_student_profile'),
    path('pl_applied_students/', views.pl_applied_students, name='pl_applied_students'),
    path('pl_alumni/', views.pl_alumni, name='pl_alumni'),
    path('pl_edit_student/<str:student_id>/', views.pl_edit_student, name='pl_edit_student'),
    path('pl_edit_alumni/<str:alumni_id>/', views.pl_edit_alumni, name='pl_edit_alumni'),
    path('addcompany', views.addcompany, name='addcompany'),
    path('update_application_status/<int:application_id>/<str:status>/', views.update_application_status, name='update_application_status'),

    # student pages
    path('stplacement_details/', views.stplacement_details, name='stplacement_details'),
    path('placement_apply/<int:placement_id>/', views.placement_apply, name='placement_apply'),
    path('st_alumni/', views.st_alumni, name='st_alumni'),
    path('stapplication_details/', views.stapplication_details, name='stapplication_details'),
    path('stnotification/', views.stnotification, name='stnotification'),
    # alumni pages
    path('al_student_profile/', views.al_student_profile, name='al_student_profile'),
    path('alapplied_students/', views.alapplied_students, name='alapplied_students'),

    # Logout URL
    path('logout/', views.user_logout, name='logout'),
]
# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)