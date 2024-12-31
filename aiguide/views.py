from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from .models import StudentProfile, JobRole, JobRoleQuestion, JobRoleResponse
from django.contrib.auth.decorators import login_required

# View to list all available job roles for the student's stream
def inde(request):
    return render(request,'inde.html')

def tenth(request):
    return render(request,'tenth.html')

'''
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
    return render(request, 'career_guidance/recommend_job_roles.html', context)'''


