from django.db import models
class Rooms(models.Model):
    room_type = models.CharField(max_length=100)
    room_rate = models.TextField()
    room_img = models.ImageField(upload_to='abc')

    def __str__(self):
        return self.room_type


class Booking(models.Model):
    cus_name=models.CharField(max_length=255)
    cus_phone=models.CharField(max_length=10)
    cus_email=models.EmailField()
    room_type=models.ForeignKey(Rooms,on_delete=models.CASCADE)
    book_date=models.DateField()
    booked_on=models.DateField(auto_now=True)
