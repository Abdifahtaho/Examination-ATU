from django import forms
from .models import Course, Semester, Student, Faculty, Batch, ExamResult

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['code', 'name', 'credit_hours']




class SemesterForm(forms.ModelForm):
    class Meta:
        model = Semester
        fields = ['name', 'start_date', 'end_date', 'courses']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['firstname', 'last_name', 'student_id', 'enrollment_year', 'faculty', 'batches', 'semesters']
        widgets = {
            'batches': forms.CheckboxSelectMultiple(),
            'semesters': forms.CheckboxSelectMultiple(),
        }


class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ['name']

class BatchForm(forms.ModelForm):
    class Meta:
        model = Batch
        fields = ['name', 'year']


class ExamResultForm(forms.ModelForm):
    class Meta:
        model = ExamResult
        fields = ['student', 'course', 'semester', 'score']
# Repeat for other models...
