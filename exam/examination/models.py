from django.db import models

# Create your models here.
class Course(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    credit_hours = models.PositiveIntegerField()

    def __str__(self):
        return self.name
    
class Semester(models.Model):
    name = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    courses = models.ManyToManyField(Course, related_name='semesters')

    def __str__(self):
        return self.name
    

class Student(models.Model):
    firstname = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    student_id = models.CharField(max_length=20, unique=True)
    enrollment_year = models.IntegerField()
    faculty = models.ForeignKey('Faculty', on_delete=models.SET_NULL, null=True, related_name='students')
    batches = models.ManyToManyField('Batch', related_name='students')
    semesters = models.ManyToManyField(Semester, related_name='students')
    def __str__(self):
        return f"{self.firstname} {self.last_name}"
    
class Faculty(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Batch(models.Model):
    name = models.CharField(max_length=50)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.year}"
    

class ExamResult(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='exam_results')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.student} - {self.course}"


