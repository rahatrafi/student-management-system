from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm
from django.contrib import messages
from django.views import View

# CBV for Student List
class StudentListView(View):
    def get(self, request):
        students_list = Student.objects.all()
        paginator = Paginator(students_list, 10)  # Show 5 students per page
        page_number = request.GET.get('page')
        students = paginator.get_page(page_number)
        return render(request, 'students/student_list.html', {'students': students})

# CBV for Student Create
class StudentCreateView(View):
    def get(self, request):
        form = StudentForm()
        return render(request, 'students/student_form.html', {'form': form})

    def post(self, request):
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Student added successfully!")
            return redirect('student_list')
        return render(request, 'students/student_form.html', {'form': form})

# CBV for Student Update
class StudentUpdateView(View):
    def get(self, request, id):
        student = get_object_or_404(Student, id=id)
        form = StudentForm(instance=student)
        return render(request, 'students/student_form.html', {'form': form})

    def post(self, request, id):
        student = get_object_or_404(Student, id=id)
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Student updated successfully!")
            return redirect('student_list')
        return render(request, 'students/student_form.html', {'form': form})

# CBV for Student Delete
class StudentDeleteView(View):
    def get(self, request, id):
        student = get_object_or_404(Student, id=id)
        return render(request, 'students/student_confirm_delete.html', {'student': student})

    def post(self, request, id):
        student = get_object_or_404(Student, id=id)
        student.delete()
        messages.success(request, "Student deleted successfully!")
        return redirect('student_list')
