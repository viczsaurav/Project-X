from django.conf.urls import patterns, include, url

## http://<ip-address>:<port>/apis/<function-url>/<arg>
## example link = http://10.10.3.77:8000/apis/setattendancematric/a0119930e

urlpatterns = patterns('NotificationApp.notifyApp.views',

	### RESTful GET Requests
     url(r'^$', 'notify', name='notify'),
     url(r'^user/', 'user', name='user'),
     url(r'^requests/$', 'requests', name='requests'),
     url(r'^config/$', 'config', name='config'),

     # url(r'^getstudents/$', 'student_list', name='Student_List'),
     # url(r'^getstudents/(?P<rfid>[0-9]+)$', 'student_details_rfid', name='Student_details'),
     # url(r'^getstudentdetails/(?P<matric>.+)$', 'student_details_matric', name='Student_details_matric'),
     # url(r'^getattendance/$', 'attendance_list', name='Attendance_List'),     
     # url(r'^getstudentattendance/(?P<rfid>[0-9]+)$', 'attendance_student', name='Attendance_Student'),       
     # url(r'^getstudentattendancematric/(?P<matric>.+)$', 'attendance_student_matric', name='Attendance_Student_Matric'),   
     # url(r'^getlectureschedule/(?P<rfid>[0-9]+)$', 'lecture_schedule', name='Lecture_Schedule'),   
     # url(r'^update/$', 'student_update', name='Student_Update'),

    ### RESTful POST Requests
     # url(r'^setattendance/(?P<userid>.+)$', 'set_attendance', name='Set_Attendance'),
     # url(r'^setgcmregid/(?P<regid>.+)$', 'set_gcm_regID', name='Set GCM Reg ID'),



)
