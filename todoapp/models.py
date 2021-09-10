from django.db import models

# Create your models here.
class Task(models.Model):
    title=models.TextField(max_length=50)
    task_description=models.TextField()
    time=models.DateTimeField(auto_now_add=True)
    time=models.DateTimeField(blank=True, null=True)
    #send_reminder_email.apply_async(eta=datetime_object)
    #process_time_utc = datetime.datetime.fromtimestamp(time.mktime(x.utctimetuple()))
    #process_request.apply_async(eta=process_time_utc,kwargs={'description':xxxx})


    def __str__(self):
       return self.title

class User(models.Model):
    name=models.CharField(max_length=15)
    email=models.EmailField()    

    def __str__(self):
       return self.name
 


class Command(models.Model):
    def handle(self, **options):
        today=datetime.datetime.now().date()
        for schedule in Schedule.objects.filter(date=today, completed=False):
            print(schedule.user.email)
            subject='Schedule reminder'
            body='Hey,please complete your schedule'+schedule.name
            send_mail(subject,body,'user@gmail.com',[schedule.user.email])