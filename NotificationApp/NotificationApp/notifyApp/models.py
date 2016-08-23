from django.db import models

# Create your models here.

class user(models.Model):	
    userid = models.IntegerField(primary_key=True, db_column='UserId') # Field name made lowercase.
    username = models.CharField(max_length=135, db_column='UserName') # Field name made lowercase.
    user_email = models.CharField(max_length=135, db_column='User_Email', blank=True) # Field name made lowercase.
    user_phone = models.CharField(max_length=135, db_column='User_Phone', blank=True) # Field name made lowercase.

    class Meta:
        db_table = u'UserInfo'
        app_label= 'notify'

