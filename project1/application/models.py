from django.db import models

# Create your models here.
class company_model(models.Model):
	company_name = models.CharField(unique=True,max_length=100)
	company_id = models.IntegerField(primary_key=True)
	class Meta:
		db_table ='company_db'
	
class jobs_model(models.Model):
	job_id = models.IntegerField(primary_key=True)
	job_tittle = models.CharField(max_length=100)
	salary = models.IntegerField()
	Experience= models.IntegerField()
	company_id= models.ForeignKey(company_model,related_name='jobs',on_delete=models.CASCADE)
	class Meta:
		db_table= "jobs_db"		
