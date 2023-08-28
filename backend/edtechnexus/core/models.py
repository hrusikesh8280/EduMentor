from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=50)
    parent_department = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    major = models.CharField(max_length=50)
    email = models.EmailField()
    contact_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Instructor(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    department = models.CharField(max_length=50)
    email = models.EmailField()
    contact_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Course(models.Model):
    course_code = models.CharField(max_length=20)
    course_name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)  # Use ForeignKey to Department
    credits = models.IntegerField()
    description = models.TextField()
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)

    def __str__(self):
        return self.course_name

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

class Assignment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField()

    def __str__(self):
        return self.title

class Submission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    submission_date = models.DateField()
    status = models.CharField(max_length=20)
    remarks = models.TextField()


class Announcement(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    publish_date = models.DateField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE, blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title
