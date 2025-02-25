from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from .models import StudentProfile, JobRole, JobRoleQuestion, JobRoleResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def inde(request):
    return render(request,'index.html')

'''def signup(request):
    return render(request,'signup.html')'''


def signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        mobile_number = request.POST.get('mobile_number')
        password = request.POST.get('password')

        # Check if the user already exists
        if User.objects.filter(username=email).exists():
            messages.error(request, "Email already registered!")
            return render(request, 'signup.html')

        # Create new user
        user = User.objects.create_user(username=email, email=email, password=password, first_name=first_name, last_name=last_name)
        user.save()
        messages.success(request, "Account created successfully! Please log in.")
        return redirect('login')  # Redirect to the Login page after sign-up

    return render(request, 'signup.html')



# Path to your custom login template
class CustomLoginView(LoginView):
    template_name = 'login.html'  
    
'''
# View to list all available job roles for the student's stream
@login_required
def job_roles_list(request):
    student_profile = get_object_or_404(StudentProfile, user=request.user)
    job_roles = JobRole.objects.filter(stream__in=[student_profile.stream, 'all'])
    context = {
        'student_profile': student_profile,
        'job_roles': job_roles,
    }
    return render(request, 'career_guidance/job_roles_list.html', context)

# View to display questions for a specific job role
@login_required
def job_role_questions(request, job_role_id):
    job_role = get_object_or_404(JobRole, id=job_role_id)
    questions = job_role.questions.all()
    context = {
        'job_role': job_role,
        'questions': questions,
    }
    return render(request, 'career_guidance/job_role_questions.html', context)


# View to handle the submission of responses for a specific job role
@login_required
def submit_responses(request, job_role_id):
    if request.method == 'POST':
        job_role = get_object_or_404(JobRole, id=job_role_id)
        student_profile = get_object_or_404(StudentProfile, user=request.user)

        # Save responses
        for question_id, score in request.POST.items():
            if question_id.startswith('question_'):
                question_id = int(question_id.split('_')[1])
                question = get_object_or_404(JobRoleQuestion, id=question_id)
                JobRoleResponse.objects.update_or_create(
                    student=student_profile,
                    question=question,
                    defaults={'score': int(score)},
                )
        return HttpResponseRedirect(reverse('career_guidance:job_roles_list'))


# View to recommend job roles based on responses
@login_required
def recommend_job_roles(request):
    student_profile = get_object_or_404(StudentProfile, user=request.user)
    job_roles = JobRole.objects.filter(stream__in=[student_profile.stream, 'all'])
    job_role_scores = {}

    for job_role in job_roles:
        questions = job_role.questions.all()
        total_score = 0
        max_possible_score = 0

        for question in questions:
            response = JobRoleResponse.objects.filter(student=student_profile, question=question).first()
            if response:
                total_score += response.score
            max_possible_score += question.max_score

        if max_possible_score > 0:
            percentage_score = (total_score / max_possible_score) * 100
            job_role_scores[job_role] = percentage_score

    # Sort job roles by percentage score in descending order
    sorted_job_roles = sorted(job_role_scores.items(), key=lambda x: x[1], reverse=True)
    context = {
        'student_profile': student_profile,
        'sorted_job_roles': sorted_job_roles,
    }
    return render(request, 'career_guidance/recommend_job_roles.html', context)

'''
