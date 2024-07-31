from django.db.models.base import Model as Model
from django.db.models import Count
from .filters import StudentFilter
from django.views.generic import(
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView,
    DeleteView,
)
from django.views import View

from .models import Student, Company, PlacementActivity
from django.http import Http404
from .forms import (
	StudentForm,
	StudentReadOnlyForm,
	CompanyForm,
)
from django.urls import reverse_lazy
import os 
from django.contrib.auth.mixins import (
	LoginRequiredMixin, 
	UserPassesTestMixin,
)

from actions.models import Permission
from django.shortcuts import render 

# STUDENT

class BatchListView(LoginRequiredMixin,ListView):
	model = Student 
	template_name = 'batch_list.html'

	def get_queryset(self):
		queryset = Student.objects.values_list('batch', flat=True).distinct().order_by('batch').reverse()
		print(queryset)
		return queryset
	
class StudentListView(LoginRequiredMixin, ListView):
	model = Student 
	template_name = "student_list.html"

	def get_queryset(self):
		batch = self.kwargs.get('batch')
		branch=self.kwargs.get('branch')
		queryset = Student.objects.filter(batch = batch).filter(branch=branch).order_by('register_no')
		if queryset:
			return queryset
		else:
			raise Http404("No Students found for the specified batch.")

	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['batch'] = self.kwargs.get('batch')
		context['branch'] = self.kwargs.get('branch')
		return context
      
class StudentDetailView(LoginRequiredMixin, DetailView):
    model = Student 
    template_name = 'student_detail.html'

    def get_object(self):
        reg_no = self.kwargs.get("register_no")
        queryset = self.get_queryset().filter(register_no=reg_no)
        print(reg_no)
        if queryset.exists():
            return queryset.first()
        else:
            raise Http404("No Students found for the specified register_no.")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = StudentReadOnlyForm(instance=self.get_object())
        context['form'] = form 
        return context


class StudentCreateView(LoginRequiredMixin, UserPassesTestMixin ,CreateView):
	model = Student 
	template_name = 'student_create.html'
	form_class = StudentForm

	def get_success_url(self):
		return reverse_lazy('student_list', kwargs = {'batch' : self.object.batch})

	def test_func(self):
		current = Permission.objects.filter(staff = self.request.user)
		if current and current.first().status == 'A':
			return True
		return False

		



class StudentUpdateView(LoginRequiredMixin, UserPassesTestMixin , UpdateView):
	model = Student 
	template_name = "student_update.html"
	form_class = StudentForm
	def get_success_url(self):
		return reverse_lazy('student_list', kwargs = {'batch' : self.object.batch})
	
	def get_object(self):
		reg_no = self.kwargs.get("register_no")
		queryset = self.get_queryset().filter(register_no = reg_no)
		if queryset:
			return queryset.first()
		else:
			raise Http404("No Students found for the specified digital_id.")
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		object = self.get_object()
		context['object'] = object
		return context 
	
	# def form_valid(self, form):
	# 	new_image = form.cleaned_data.get('profile_image')
	# 	old_image = self.get_object().profile_image

	# 	if old_image and old_image != new_image:
	# 		os.remove(old_image.path)

	# 	new_file = form.cleaned_data.get("resume")
	# 	old_file = self.get_object().resume

	# 	if old_file and old_file != new_file:
	# 			os.remove(old_file.path)

	# 	return super().form_valid(form)
	
	def test_func(self):
		current = Permission.objects.filter(staff = self.request.user)
		if current and current.first().status == 'A':
			return True
		return False
	

class StudentDeleteView(LoginRequiredMixin, UserPassesTestMixin , DeleteView):
	model = Student 
	success_url = reverse_lazy('batch_list')
	template_name = 'student_delete.html'

	# def form_valid(self, form):
	# 	os.remove(self.get_object().profile_image.path)
	# 	os.remove(self.get_object().resume.path)
	# 	return super().form_valid(form)
	
	def get_object(self):
		reg_no = self.kwargs.get("register_no")
		queryset = self.get_queryset().filter(register_no = reg_no)
		if queryset:
			return queryset.first()
		else:
			raise Http404("No Students found for the specified digital_id.")
	
	def test_func(self):
		current = Permission.objects.filter(staff = self.request.user)
		if current and current.first().status == 'A':
			return True
		return False

# COMPANY

# views.py
class CompanyListView(LoginRequiredMixin, ListView):
    model = Student
    template_name = "company_list.html"
    context_object_name = 'company_list'
    filterset_class = StudentFilter

    def get_queryset(self):
        filterset = self.filterset_class(self.request.GET, queryset=Student.objects.all())
        filtered_students = filterset.qs

        # Apply CTC filters
        min_ctc = self.request.GET.get('min_ctc')
        max_ctc = self.request.GET.get('max_ctc')
        if min_ctc:
            filtered_students = filtered_students.filter(Cost_To_Company__gte=min_ctc)
        if max_ctc:
            filtered_students = filtered_students.filter(Cost_To_Company__lte=max_ctc)

        # Annotate with student count per company
        queryset = filtered_students.values('Company').annotate(student_count=Count('id'))

        # Apply sorting
        sort = self.request.GET.get('sort')
        if sort == 'placed_asc':
            queryset = queryset.order_by('student_count')
        elif sort == 'placed_desc':
            queryset = queryset.order_by('-student_count')
        else:
            queryset = queryset.order_by('Company')

        return queryset


class CompanyDetailView(LoginRequiredMixin, ListView):
	model = Student
	template_name = "company_detail.html"
	context_object_name = 'students'

	def get_queryset(self):
		company = self.kwargs.get('company')
		if not company:
			raise Http404("No Company specified.")
		
		queryset = Student.objects.filter(Company=company)
		if queryset.exists():
			return queryset
		else:
			raise Http404("No Students found for the specified Company.")

class CompanyCreateView(LoginRequiredMixin, UserPassesTestMixin , CreateView):
	model = Company
	template_name = "company_create.html"
	form_class = CompanyForm
	success_url = reverse_lazy('company_list')

	def test_func(self):
		current = Permission.objects.filter(staff = self.request.user)
		if current and current.first().status == 'A':
			return True
		return False

class CompanyUpdateView(LoginRequiredMixin, UserPassesTestMixin , UpdateView):
	model = Company
	template_name = "company_update.html"
	form_class = CompanyForm
	success_url = reverse_lazy('company_list')
	def form_valid(self, form):
		new_image = form.cleaned_data.get('logo')
		old_image = self.get_object().logo
		if old_image and old_image != new_image:
			os.remove(old_image.path)
		return super().form_valid(form)

	def test_func(self):
		current = Permission.objects.filter(staff = self.request.user)
		if current and current.first().status == 'A':
			return True
		return False

class CompanyDeleteView(LoginRequiredMixin, UserPassesTestMixin , DeleteView):
	model = Company
	template_name = "company_delete.html"
	success_url = reverse_lazy('company_list')
	def form_valid(self, form):
		os.remove(self.get_object().logo.path)
		return super().form_valid(form)
	
	def test_func(self):
		current = Permission.objects.filter(staff = self.request.user)
		if current and current.first().status == 'A':
			return True
		return False


# PLACEMENT ACTIVITY


class PlacementActivityListView(LoginRequiredMixin, ListView):
	model = PlacementActivity
	template_name = 'pa_list.html'
	def get_queryset(self):
		digital_id = self.kwargs.get('digital_id')
		query_set = PlacementActivity.objects.filter(student = digital_id)
		if query_set:
			return query_set
		return Http404('No records found for this digital_id')
	def get_context_data(self, **kwargs):
		context = super().get_context_data()
		context['did'] = self.kwargs.get('digital_id')
		return context


class PlacementActivityDetailView(LoginRequiredMixin, DetailView):
	model = PlacementActivity
	template_name = 'pa_detail.html'
	def get_object(self):
		pk_id = self.kwargs.get('pk')
		obj = PlacementActivity.objects.filter(id =pk_id)
		if obj:
			return obj.first()
		return Http404('No records found for this id')


class PlacementActivityUpdateView(LoginRequiredMixin, UserPassesTestMixin , UpdateView):
	model = PlacementActivity
	template_name = 'pa_update.html'
	fields = ['attending_date', 'company', 'info', 'result_date', 'result']
	def get_object(self):
		pk_id = self.kwargs.get('pk')
		obj = PlacementActivity.objects.filter(id =pk_id)
		if obj:
			return obj.first()
		return Http404('No records found for this id')
	
	def get_success_url(self):
		return reverse_lazy('placement_list', kwargs = {'digital_id' : self.object.student.digital_id})
	
	def test_func(self):
		current = Permission.objects.filter(staff = self.request.user)
		if current and current.first().status == 'A':
			return True
		return False
	
class PlacementActivityCreateView(LoginRequiredMixin, UserPassesTestMixin , CreateView):
	model = PlacementActivity
	template_name = 'pa_create.html'
	fields = ['attending_date', 'company', 'info', 'result_date', 'result']

	def get_success_url(self):
		return reverse_lazy('placement_list', kwargs = {'digital_id' : self.object.student.digital_id})

	def form_valid(self, form):
		form.instance.student = Student.objects.get(digital_id = int(self.kwargs.get('digital_id')))
		return super().form_valid(form)

	def test_func(self):
		current = Permission.objects.filter(staff = self.request.user)
		if current and current.first().status == 'A':
			return True
		return False

class PlacementActivityDeleteView(LoginRequiredMixin, UserPassesTestMixin , DeleteView):
	model = PlacementActivity
	template_name = 'pa_delete.html'
	def get_object(self):
		pk_id = self.kwargs.get('pk')
		obj = PlacementActivity.objects.filter(id =pk_id)
		if obj:
			return obj.first()
		return Http404('No records found for this id')

	def get_success_url(self):
		return reverse_lazy('placement_list', kwargs = {'digital_id' : self.object.student.digital_id})
	
	def test_func(self):
		current = Permission.objects.filter(staff = self.request.user)
		if current and current.first().status == 'A':
			return True
		return False

#dummy

class DepartmentList(LoginRequiredMixin,ListView):
	model = Student 
	template_name = "department_list.html"
	context_object_name = 'department_list'

	def get_queryset(self):
		batch = self.kwargs.get('batch')
		queryset = Student.objects.filter(batch=batch).values('branch', 'batch').annotate(student_count=Count('branch')).order_by('branch')
		print(queryset)
		if queryset:
			return queryset
		else:
			raise Http404("No Students found for the specified batch.")

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['batch'] = self.kwargs.get('batch')
		return context

class HomeView(View):
	def get(self, request):
		return render(request, 'home.html')
