from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm
from django.contrib import messages
from django.core.paginator import Paginator

# View to list all students
def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})

# View to add a new student
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Student added successfully!") 
            return redirect('student_list')
        else:
            messages.error(request, "Error! Please correct the form.") 
    else:
        form = StudentForm()
    return render(request, 'students/student_form.html', {'form': form})

# View to update student details
def student_update(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Student updated successfully!")  
            return redirect('student_list')
        else:
            messages.error(request, "Error! Please correct the form.")  
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/student_form.html', {'form': form})

# View to delete a student
def student_delete(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student.delete()
        messages.success(request, "Student deleted successfully!")  
        return redirect('student_list')
    return render(request, 'students/student_confirm_delete.html', {'student': student})
