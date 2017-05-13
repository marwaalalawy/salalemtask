from django.db import models

class offer(models.Model):
	companyName=models.CharField(max_length=200)
	description=models.CharField(max_length=200)
	date=models.CharField(max_length=200)
	create_date=models.DateTimeField('date published')
	location=models.CharField(max_length=200)


#     def __str__(self):
#     	return self.company_name +'_' +self.discription
    	
# class company(models.Model):
# 	offer=models.Foreignkey(Offer,on_delete=models.CASCADE)
# 	name=models.CharField(max_length=200)
# 	email=models.CharField(max_length=200)
# 	password=models.CharField(max_length=200)