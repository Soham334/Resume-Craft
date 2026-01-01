from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView
from django.urls import reverse
from django.contrib.auth.decorators import login_required 
from django.http import HttpResponse 
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm 
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import logout
from django.shortcuts import render
from .models import Resume
from .forms import ResumeForm
from .serializers import ResumeSerializer 

User = get_user_model() 
@login_required 
def create_resume(request, resume_id=None):
    """Handles creating (no resume_id) or editing (with resume_id) a resume, 
    restricted to the owner."""
    
    if resume_id:
        resume_instance = get_object_or_404(Resume, id=resume_id, user=request.user)
    else:
        resume_instance = None

    if request.method == "POST":
        form = ResumeForm(request.POST, instance=resume_instance)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.user = request.user 
            resume.save()
            return redirect(reverse('resume_detail', kwargs={'resume_id': resume.id}))
    else:
        form = ResumeForm(instance=resume_instance)
        
    return render(request, 'resumesite/resume_form.html', {
        'form': form,
        'resume_id': resume_id,
        'is_edit': resume_id is not None
    })
edit_resume = create_resume

@login_required
def resume_detail(request, resume_id):
    """Fetches the resume (owned by the user) and prepares lists for the template."""
    
    resume = get_object_or_404(Resume, id=resume_id, user=request.user)
    skills_list = [s.strip() for s in resume.skills.split(',') if s.strip()]
    languages_list = [l.strip() for l in resume.languages.split(',') if l.strip()]
    achievements_list = [a.strip() for a in resume.achievements.split(',') if a.strip()]

    return render(request, 'resumesite/resume_detail.html', {
        'resume': resume,
        'skills_list': skills_list,
        'languages_list': languages_list,
        'achievements_list': achievements_list,
    })


@login_required
def delete_resume(request, resume_id):
    """Handles the DELETE operation, restricted to the owner."""
    
    # ... (Your existing delete_resume logic remains here) ...
    resume = get_object_or_404(Resume, id=resume_id, user=request.user)
    
    if request.method == 'POST':
        resume.delete()
        return redirect('resume_create') 
        
    return HttpResponse(f"""
        <div class="form-container" style="text-align: center;">
            <h2>Confirm Deletion</h2>
            <p>Are you sure you want to permanently delete the resume for <strong>{resume.full_name}</strong>?</p>
            <form method='POST' action=''>
                {request.user.get_csrf_token()}
                <button type='submit' style='background-color: red; color: white; padding: 10px; border: none; cursor: pointer;'>
                    Yes, Delete
                </button>
            </form>
            <p style='margin-top: 15px;'><a href='{reverse('resume_detail', kwargs={'resume_id': resume.id})}'>No, Go Back</a></p>
        </div>
    """)


# -----------------------------------------------------------
# 4. REGISTRATION
# -----------------------------------------------------------
def register(request):
    """Handles user registration using Django's built-in UserCreationForm."""
    
    # ... (Your existing register logic remains here) ...
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') 
    else:
        form = UserCreationForm()
        
    return render(request, 'registration/register.html', {'form': form})


# -----------------------------------------------------------
# 5. READ (R) - Class-Based View 
# -----------------------------------------------------------
class ResumeDetailView(DetailView):
    """Alternative method for the Detail View, using CBV."""
    # ... (Your existing ResumeDetailView logic remains here) ...
    model = Resume
    template_name = 'resumesite/resume_detail.html'
    context_object_name = 'resume'
    
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Resume.objects.filter(user=self.request.user)
        return Resume.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        resume = context.get('resume')
        
        if resume:
            context['skills_list'] = [s.strip() for s in resume.skills.split(',') if s.strip()]
            context['languages_list'] = [l.strip() for l in resume.languages.split(',') if l.strip()]
            context['achievements_list'] = [a.strip() for a in resume.achievements.split(',') if a.strip()]
        
        return context

# ===========================================================
#        NEW: REACT AND DRF INTEGRATION VIEWS
# ===========================================================

# -----------------------------------------------------------
# 6. REACT FRONTEND ENTRY POINT
# -----------------------------------------------------------
def react_demo_view(request):
    """Renders the HTML file that loads the compiled React bundle."""
    return render(request, 'resumesite/react_demo.html')


class ResumeViewSet(viewsets.ModelViewSet):
    """
    Provides full CRUD operations for Resumes via API.
    Only allows access to resumes owned by the authenticated user.
    """
    serializer_class = ResumeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # 1. Filter the queryset to only include resumes belonging to the current user
        return Resume.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # 2. Automatically set the user field when a new resume is created
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        # 3. Ensure the user cannot change ownership during an update
        serializer.save(user=self.request.user)
        
#LOGOUT   
def custom_logout(request):
    logout(request)
    return render(request, 'registration/logged_out.html')