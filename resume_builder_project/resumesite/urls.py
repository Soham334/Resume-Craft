# resumesite/urls.py

from django.urls import path, include # <-- Added 'include' for API routing
from . import views
from django.views.generic import TemplateView 
from django.contrib.auth import views as auth_views
# --- NEW IMPORTS FOR DRF ---
from rest_framework.routers import DefaultRouter

# Initialize DRF Router
router = DefaultRouter()
# Register the ModelViewSet we created in views.py
router.register(r'resumes', views.ResumeViewSet, basename='resume-api')

urlpatterns = [
    path('', views.react_demo_view, name='react_demo'),
    path('api/', include(router.urls)),
    path('resume/create/', views.create_resume, name='resume_create'),
    
    # -----------------------------------------------
    # EXISTING DJANGO CRUD & AUTH VIEWS (UNCHANGED)
    # -----------------------------------------------
    # C (Create) - Mapped to the base path within the inclusion ('/')
    
    # AUTHENTICATION
    path('register/', views.register, name='register'),
    
    # R (Read/Detail)
    path('resume/<int:resume_id>/', views.resume_detail, name='resume_detail'), 

    # U (Update/Edit)
    path('resume/<int:resume_id>/edit/', views.edit_resume, name='resume_edit'), 
    
    # D (Delete)
    path('resume/<int:resume_id>/delete/', views.delete_resume, name='resume_delete'), 

    # CBV (Class-Based View for Experiment 3)
    path('resume-cbv/<int:pk>/', views.ResumeDetailView.as_view(), name='resume_detail_cbv'), 
    #logout
path(
    'logout/',
    auth_views.LogoutView.as_view(
        template_name='registration/logged_out.html'
    ),
    name='logout'
),]