from django.views.generic import CreateView
from .models import Permission
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib import messages
# Create your views here.
class RequestPermissionView(LoginRequiredMixin, CreateView):
	model = Permission
	template_name = 'request_permission.html'
	fields = ("reason",)
	success_url = reverse_lazy('batch_list')

	def form_valid(self, form):
        # Check if the user has already created a permission
		existing_permission = Permission.objects.filter(staff=self.request.user).exists()
		if existing_permission:
			# If a permission already exists, redirect or handle the error as needed
			# For example, redirecting back to the form with an error message

			return redirect('batch_list')  # Redirect to some error page or back to the form
		else:
			# If no existing permission, proceed with saving the form
			form.instance.staff = self.request.user 
			return super().form_valid(form)
	
# form validation
# cron job
# ball
# yes we ball

# django_project/settings.py
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5" # new
CRISPY_TEMPLATE_PACK = "bootstrap5" # new