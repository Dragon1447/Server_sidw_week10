from django.shortcuts import render , redirect
import json
from django.http import HttpResponse
from .models import *
from django.views import View
from django.http import JsonResponse
from .forms import EmployeeForm, ProjectForm, ProjectDetailForm

# Create your views here.

class IndexView(View):

    def get(self, request):
        employee_list = Employee.objects.order_by("id")
        num  = Employee.objects.count()
        context = {
            "employee_list" : employee_list,
            "num" : num       
                   }
        return render(request, "employee.html", context)
    
class PositionView(View):
    def get(self, request):
        position_list = Position.objects.order_by("id")
        context = {
            "position_list" : position_list, 
                   }
        return render(request, "position.html", context)
    
    
class PojectView(View):
    def get(self, request):
        project_list = Project.objects.order_by("id")
        context = {
            "project_list" : project_list
                   }
        return render(request, "project.html", context)
    def delete(self, request, id):
        project = Project.objects.get(pk=id)
        project.delete()
        return JsonResponse({'foo':'bar'}, status=200)
    
    
    
    # def post (self, request, project_id):
    #     project = Project.objects.get(pk=project_id).delete()
    #     return render("project", "project_detail.html")
    
class PojectdetailView(View):
    def get (self, request, project_id):
        project = Project.objects.get(pk=project_id)
        form = ProjectDetailForm(instance=project)
        context = {
            "staff": project.staff.all(),
            "project" : project,
            "start_date" : project.start_date.strftime("%Y-%m-%d"),
            "due_date" : project.due_date.strftime("%Y-%m-%d"),
            "form" : form
                   }
        return render(request, "project_detail.html", context)
    
    def post(self, request, project_id):
        project = Project.objects.get(pk=project_id)
        # for updating article instance set instance=article
        form = ProjectDetailForm(request.POST, instance=project)
        context = {
            "project" : project,
            "start_date" : project.start_date.strftime("%Y-%m-%d"),
            "due_date" : project.due_date.strftime("%Y-%m-%d"),
            "form" : form
                   }

        # save if valid                                       
        if form.is_valid():                                                                      
            form.save()                                                                          
            return redirect("projectdetail", project_id)

        return render(request, "project_detail.html", context)
    
    
    def put(self, request, project_id, emp_id):
        try:
            
            project = Project.objects.get(id=project_id)
            employee = Employee.objects.get(id=emp_id)

            # Add employee to project
            project.staff.add(employee)
            return JsonResponse({'message': 'Employee added successfully'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
        
    def delete(self, request, project_id, emp_id):
        try: 
            project = Project.objects.get(id=project_id)
            employee = Employee.objects.get(id=emp_id)
            project.staff.remove(employee)
            return JsonResponse({"message": "Project deleted successfully."}, status=200)
        except Project.DoesNotExist:
            return JsonResponse({"error": "Project not found."}, status=404)
        
    from django.shortcuts import render, redirect

class EmployeeForm_us(View):
    def get(self, request):
        form = EmployeeForm()
        return render(request, "employee_form.html", {"form": form})
    
    def post(self, request):
        # bind data to form
        form = EmployeeForm(request.POST)
        # validate data in the form
        if form.is_valid():
            form.save()
            return redirect("employee")
    
        return render(request, "employee_form.html", {"form": form})

class ProjectForm_us(View):
    def get(self, request):
        form = ProjectForm()
        return render(request, "project_form.html", {"form": form})
    
    def post(self, request):
        # bind data to form
        form = ProjectForm(request.POST)
        # validate data in the form
        if form.is_valid():
            form.save()
            return redirect("project")
    
        return render(request, "project_form.html", {"form": form})
    