from django.db import models
import uuid

def get_student_path(instance, filename):
	ext = filename.split(".")[-1]
	u = str(uuid.uuid4())
	return f"student_profiles/{u}_{instance.digital_id}.{ext}"

def get_company_logo_path(instance, filename):
	ext = filename.split(".")[-1]
	u = str(uuid.uuid4())
	return f"company_logos/{u}_{instance.company_id}.{ext}"

def pdf_upload_path(instance, filename):
	ext = filename.split(".")[-1]
	u = str(uuid.uuid4())
	return f"resumes/{u}_{instance.digital_id}_resume.{ext}"

class Company(models.Model):
	name = models.CharField(max_length = 100)
	def __str__(self):
		return f"{self.name}"

# Create your models here.
class Student(models.Model):

	IT = "IT"
	CORE = "Core"
	MANAGEMENT = "Management"
	status_codes = [

	(IT , "IT"),
	(CORE , "Core"),
	(MANAGEMENT , "Management"),

	]

	
	register_no = models.BigIntegerField(unique=True)
	name = models.CharField(max_length = 100)
	batch = models.IntegerField()
	degree = models.CharField(max_length=6, null=True, blank = True)
	branch = models.CharField(null=True,max_length=50, blank = True)
	On_Off_Campus = models.CharField(null=True, max_length=20,blank = True)
	Company = models.CharField(max_length = 50, null=True, blank = True)
	Cost_To_Company=models.IntegerField(null=True)

	def __str__(self):
		return f"{self.register_no} - {self.name}"


class PlacementActivity(models.Model):
	FAILED = "F"
	PASSED = "P"
	NOT_ANNOUNCED = "N"
	result_choices = [
	(FAILED , "Failed"),
	(PASSED, "Passed"),
	(NOT_ANNOUNCED, "Not Announced")
	]
	attending_date = models.DateField(null=True, blank = True)
	#student = models.ForeignKey(Student,to_field='digital_id', db_column='digital_id', on_delete = models.CASCADE)
	#company = models.ForeignKey(Company,to_field='company_id', db_column='company_id', on_delete = models.CASCADE)
	info = models.TextField(null = True, blank = True)
	result_date = models.DateField(null=True, blank = True)
	result = models.CharField(choices = result_choices, max_length=1, default='N')

	def __str__(self):
		return f"{self.company.name}-{self.student.name}"

