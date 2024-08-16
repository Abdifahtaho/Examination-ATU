from django.urls import path
from .views import CourseListView, CourseCreateView, CourseUpdateView, CourseDeleteView,home,generate_transcript,BatchDetailView,SemesterListView, SemesterCreateView, SemesterUpdateView, SemesterDeleteView
from .views import StudentListView, StudentCreateView, StudentUpdateView, StudentDeleteView
from .views import FacultyListView, FacultyCreateView, FacultyUpdateView, FacultyDeleteView
from .views import BatchListView, BatchCreateView, BatchUpdateView, BatchDeleteView
from .views import ExamResultListView, ExamResultCreateView, ExamResultUpdateView, ExamResultDeleteView,register
from django.contrib.auth import views as auth_views
from .views import login_view, logout_view, register,generate_transcript

urlpatterns = [
    path('home', home, name='home'),
    path('students/<int:student_id>/transcript/', generate_transcript, name='generate_transcript'),
    path('courses/', CourseListView.as_view(), name='course_list'),
    path('courses/create/', CourseCreateView.as_view(), name='course_create'),
    path('courses/<int:pk>/update/', CourseUpdateView.as_view(), name='course_update'),
    path('courses/<int:pk>/delete/', CourseDeleteView.as_view(), name='course_delete'),
    path('batches/<int:pk>/', BatchDetailView.as_view(), name='batch_detail'),
#    semester
    path('semesters/', SemesterListView.as_view(), name='semester_list'),
    path('semesters/create/', SemesterCreateView.as_view(), name='semester_create'),
    path('semesters/<int:pk>/update/', SemesterUpdateView.as_view(), name='semester_update'),
    path('semesters/<int:pk>/delete/', SemesterDeleteView.as_view(), name='semester_delete'),

    # Students
    path('students/', StudentListView.as_view(), name='student_list'),
    path('students/create/', StudentCreateView.as_view(), name='student_create'),
    path('students/<int:pk>/update/', StudentUpdateView.as_view(), name='student_update'),
    path('students/<int:pk>/delete/', StudentDeleteView.as_view(), name='student_delete'),

    # faculty
    path('faculties/', FacultyListView.as_view(), name='faculty_list'),
    path('faculties/create/', FacultyCreateView.as_view(), name='faculty_create'),
    path('faculties/<int:pk>/update/', FacultyUpdateView.as_view(), name='faculty_update'),
    path('faculties/<int:pk>/delete/', FacultyDeleteView.as_view(), name='faculty_delete'),
    
    # batch.......
    path('batches/', BatchListView.as_view(), name='batch_list'),
    path('batches/create/', BatchCreateView.as_view(), name='batch_create'),
    path('batches/<int:pk>/update/', BatchUpdateView.as_view(), name='batch_update'),
    path('batches/<int:pk>/delete/', BatchDeleteView.as_view(), name='batch_delete'),

    # exam_result............
    path('exam_results/', ExamResultListView.as_view(), name='exam_result_list'),
    path('exam_results/create/', ExamResultCreateView.as_view(), name='exam_result_create'),
    path('exam_results/<int:pk>/update/', ExamResultUpdateView.as_view(), name='exam_result_update'),
    path('exam_results/<int:pk>/delete/', ExamResultDeleteView.as_view(), name='exam_result_delete'),
    path('register/', register, name='register'),
    path('', login_view, name='login'),
    path('accounts/logout/', logout_view, name='logout'),
    path('students/<int:student_id>/transcript/', generate_transcript, name='generate_transcript'),

]
