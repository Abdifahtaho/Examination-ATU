from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Batch, Course, Student
from .forms import CourseForm
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.db.models import Avg
from .models import Semester
from .forms import SemesterForm
from .models import Student
from .forms import StudentForm
from .models import Faculty
from .forms import FacultyForm
from .models import Batch
from .forms import BatchForm
from .models import ExamResult
from .forms import ExamResultForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

@login_required(login_url="/accounts/login/")
def home(request):
    return render(request, 'examination/home.html')


class CourseListView(ListView):
    model = Course
    template_name = 'examination/course_list.html'  # Corrected here
    context_object_name = 'courses'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Course.objects.filter(name__icontains=query)
        return Course.objects.all()

    

class CourseCreateView(CreateView):
    model = Course
    form_class = CourseForm
    template_name = 'examination/course_form.html'  # Corrected here
    success_url = reverse_lazy('course_list')

class CourseUpdateView(UpdateView):
    model = Course
    form_class = CourseForm
    template_name = 'examination/course_form.html'  # Corrected here
    success_url = reverse_lazy('course_list')

class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'examination/course_confirm_delete.html'  # Corrected here
    success_url = reverse_lazy('course_list')



class BatchDetailView(DetailView):
    model = Batch
    template_name = 'batches/batch_detail.html'  # Corrected here

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['students'] = self.object.students.all()
        return context
    
#    semsters
class SemesterListView(ListView):
    model = Semester
    template_name = 'semesters/semester_list.html'
    context_object_name = 'semesters'

class SemesterCreateView(CreateView):
    model = Semester
    form_class = SemesterForm
    template_name = 'semesters/semester_form.html'
    success_url = reverse_lazy('semester_list')

class SemesterUpdateView(UpdateView):
    model = Semester
    form_class = SemesterForm
    template_name = 'semesters/semester_form.html'
    success_url = reverse_lazy('semester_list')

class SemesterDeleteView(DeleteView):
    model = Semester
    template_name = 'semesters/semester_confirm_delete.html'
    success_url = reverse_lazy('semester_list')


# student

class StudentListView(ListView):
    model = Student
    template_name = 'students/student_list.html'
    context_object_name = 'students'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Student.objects.filter(firstname__icontains=query) | \
                   Student.objects.filter(last_name__icontains=query) | \
                   Student.objects.filter(student_id__icontains=query)
        return super().get_queryset()

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/student_form.html'
    success_url = reverse_lazy('student_list')

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/student_form.html'
    success_url = reverse_lazy('student_list')

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'students/student_confirm_delete.html'
    success_url = reverse_lazy('student_list')



# faculty

class FacultyListView(ListView):
    model = Faculty
    template_name = 'faculty/faculty_list.html'
    context_object_name = 'faculties'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        department_filter = self.request.GET.get('department')
        
        if query:
            queryset = queryset.filter(name__icontains=query)
        if department_filter:
            queryset = queryset.filter(department__icontains=department_filter)
        
        return queryset

class FacultyCreateView(CreateView):
    model = Faculty
    form_class = FacultyForm
    template_name = 'faculty/faculty_form.html'
    success_url = reverse_lazy('faculty_list')

class FacultyUpdateView(UpdateView):
    model = Faculty
    form_class = FacultyForm
    template_name = 'faculty/faculty_form.html'
    success_url = reverse_lazy('faculty_list')

class FacultyDeleteView(DeleteView):
    model = Faculty
    template_name = 'faculty/faculty_confirm_delete.html'
    success_url = reverse_lazy('faculty_list')


# batch.........

class BatchListView(ListView):
    model = Batch
    template_name = 'batches/batch_list.html'
    context_object_name = 'batches'

class BatchCreateView(CreateView):
    model = Batch
    form_class = BatchForm
    template_name = 'batches/batch_form.html'
    success_url = reverse_lazy('batch_list')

class BatchUpdateView(UpdateView):
    model = Batch
    form_class = BatchForm
    template_name = 'batches/batch_form.html'
    success_url = reverse_lazy('batch_list')

class BatchDeleteView(DeleteView):
    model = Batch
    template_name = 'batches/batch_confirm_delete.html'
    success_url = reverse_lazy('batch_list')

# Exam result..........

class ExamResultListView(ListView):
    model = ExamResult
    template_name = 'exam_results/exam_result_list.html'
    context_object_name = 'exam_results'

class ExamResultCreateView(CreateView):
    model = ExamResult
    form_class = ExamResultForm
    template_name = 'exam_results/exam_result_form.html'
    success_url = reverse_lazy('exam_result_list')

class ExamResultUpdateView(UpdateView):
    model = ExamResult
    form_class = ExamResultForm
    template_name = 'exam_results/exam_result_form.html'
    success_url = reverse_lazy('exam_result_list')

class ExamResultDeleteView(DeleteView):
    model = ExamResult
    template_name = 'exam_results/exam_result_confirm_delete.html'
    success_url = reverse_lazy('exam_result_list')




# Gpa calcualtion ..........  

def calculate_gpa_points(score):
    if 90 <= score <= 100:
        return 4.0  # A
    elif 75 <= score < 90:
        return 3.0  # B
    elif 60 <= score < 75:
        return 2.0  # C
    else:
        return 1.0  # D

def generate_transcript(request, student_id):
    student = Student.objects.get(pk=student_id)
    exam_results = student.exam_results.select_related('course', 'semester')
    
    # Initialize storage for semester information
    semesters = {}
    total_credits = 0
    total_points = 0
    
    # Process each exam result
    for result in exam_results:
        semester = result.semester
        
        # Initialize the semester data if not already done
        if semester not in semesters:
            semesters[semester] = {
                'courses': [],
                'credits': 0,
                'points': 0,
                'sgpa': 0
            }
        
        credits = result.course.credit_hours
        points = calculate_gpa_points(result.score) * credits  # Calculate points based on GPA points
        
        # Determine the grade based on the score
        grade = ''
        if 90 <= result.score <= 100:
            grade = 'A'
        elif 75 <= result.score < 90:
            grade = 'B'
        elif 60 <= result.score < 75:
            grade = 'C'
        else:
            grade = 'D'  # D or lower
        
        # Add the grade to the result object for display in the template
        result.grade = grade
        
        # Update semester data
        semesters[semester]['courses'].append(result)
        semesters[semester]['credits'] += credits
        semesters[semester]['points'] += points
        
        # Update overall totals
        total_credits += credits
        total_points += points
    
    # Calculate SGPA for each semester
    for semester in semesters:
        if semesters[semester]['credits'] > 0:
            semesters[semester]['sgpa'] = semesters[semester]['points'] / semesters[semester]['credits']
    
    # Calculate OGPA
    ogpa = total_points / total_credits if total_credits > 0 else 0

    context = {
        'student': student,
        'semesters': semesters,
        'ogpa': ogpa,
    }
    return render(request, 'students/transcript.html', context)
















# login and logout......

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to login page after registration
                
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            # Redirect to 'next' if it exists, otherwise home
            return redirect(request.POST.get('next', 'home'))
    else:
        form = AuthenticationForm()
    return render(request, "registration/login.html", {"form": form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')  # Redirect to home after logout
    return redirect('login')