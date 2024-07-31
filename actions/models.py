from django.db import models
from django.conf import settings
# Create your models here.
class Permission(models.Model):
	REJECTED = 'R'
	ACCEPTED = 'A'
	NOT_ACKNOWLEDGED = 'N'
	status_choices = [
		(REJECTED , 'Rejected'),
		(ACCEPTED , 'Accepted'),
		(NOT_ACKNOWLEDGED , 'Not yet acknowledged'),
	]
	staff = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	requested_time = models.TimeField(auto_now_add=True)
	acknowledged_time = models.TimeField(null=True, blank = True)
	status = models.CharField(max_length = 1, choices=status_choices, default=NOT_ACKNOWLEDGED)
	reason = models.TextField(null=True, blank = True)

	def __str__(self):
		return f"{self.staff} - {self.status}"
