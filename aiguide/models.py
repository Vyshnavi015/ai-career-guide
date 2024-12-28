from django.contrib.auth.models import User
from django.db import models

class StudentProfile(models.Model):
    STREAM_CHOICES = [
        ('science', 'Science'),
        ('commerce', 'Commerce'),
        ('arts', 'Arts'),
        ('vocational', 'Vocational Studies'),
        ('undecided', 'Undecided'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    grade = models.IntegerField(choices=[(10, '10th Grade'), (12, '12th Grade')])
    stream = models.CharField(max_length=20, choices=STREAM_CHOICES, default='undecided')
    interests = models.TextField(help_text="Describe hobbies or activities the student enjoys.")
    career_goal = models.CharField(max_length=255, null=True, blank=True, help_text="Optional future career goal.")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.stream}"


class JobRole(models.Model):
    STREAM_CHOICES = [
        ('science', 'Science'),
        ('commerce', 'Commerce'),
        ('arts', 'Arts'),
        ('vocational', 'Vocational Studies'),
        ('all', 'All Streams'),
    ]

    name = models.CharField(max_length=100)
    stream = models.CharField(max_length=20, choices=STREAM_CHOICES)
    description = models.TextField(help_text="Brief description of the job or course.")
    eligibility = models.TextField(help_text="Eligibility criteria for this role.")
    duration = models.CharField(max_length=50, help_text="Duration of the course or preparation time.")
    skills_needed = models.TextField(help_text="Skills needed to excel in this career.")
    career_opportunities = models.TextField(help_text="Potential job roles after pursuing this career.")
    avg_salary = models.CharField(max_length=50, help_text="Average salary range for this career.")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class JobRoleQuestion(models.Model):
    job_role = models.ForeignKey(JobRole, on_delete=models.CASCADE, related_name='questions')
    question_text = models.CharField(max_length=255)
    max_score = models.IntegerField(help_text="Maximum score for this question.")

    def __str__(self):
        return f"Question for {self.job_role.name}: {self.question_text}"
    
class JobRoleResponse(models.Model):
        student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
        question = models.ForeignKey(JobRoleQuestion, on_delete=models.CASCADE)
        score = models.IntegerField(help_text="Score given by the student.")

        def __str__(self):
            return f"{self.student.user.username} - {self.question.job_role.name}: {self.score}"

