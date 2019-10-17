from django.db import models
from datetime import date, timedelta, datetime
from django.db.models import signals
from django.dispatch import receiver

# Create your models here.


class Librarian(models.Model):
    librarian_ID = models.AutoField(primary_key=True)
    librarian_name = models.CharField(max_length=100)
    librarian_contact= models.IntegerField()

    def __str__(self):
        return str(self.librarian_name)


# class Author(models.Model):
#     author_name = models.CharField( max_length=100)
#     about_author = models.TextField(null=True, blank= True)
#
#     def __str__(self):
#        return self.author_name


class Book(models.Model):
    isbn = models.IntegerField()
    book_name = models.CharField(max_length=100)
    category = models.CharField(null=True,blank=True,max_length=100)
    number_of_copy = models.IntegerField(default=1)
    in_stock = models.IntegerField(default=1)
    availability = models.BooleanField(default=True)
    description = models.TextField(null=True,blank=True)
    price = models.IntegerField(default=0,null=True,blank=True)
    book_author = models.CharField(max_length=50,null=True,blank=True)

    def __str__(self):
        return self.book_name

    def is_available(self):
        if self.in_stock > 0:
            return True
        else:
            return False
    is_available.boolean = True
    is_available.short_description = 'Available'


class Member(models.Model):
    member_ID = models.AutoField(primary_key=True)
    member_name = models.CharField(max_length=100)
    member_contact= models.IntegerField()
    member_email = models.EmailField()
    member_address = models.TextField(null=True)

    def __str__(self):
        return str(self.member_name)


class Record(models.Model):
    borrowed_ID = models.AutoField(primary_key=True)
    borrowed_member = models.ForeignKey(Member, on_delete=models.CASCADE)
    borrowed_book = models.ForeignKey(Book, on_delete=models.CASCADE)
    issued_librarian = models.ForeignKey(Librarian, on_delete=models.CASCADE)
    issue_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(default=date.today() + timedelta(days=7))
    is_return = models.BooleanField(default=False)
    returned_date = models.DateField(default=date.today() + timedelta(days=7))
    book_returned = models.BooleanField(auto_created=True, default=False)
    time = models.TextField(default=datetime.now())

    def __str__(self):
        return str(self.borrowed_member)


# @receiver(signals.pre_save, sender=Record)
# def is_returned(sender, instance, **kwargs):
#     stock = instance.borrowed_book.in_stock
#     if not instance.book_returned:
#         if instance.borrowed_book.number_of_copy >= stock:
#             stock += 1
#             book = instance.borrowed_book
#             instance.book_returned = True
#             book.in_stock = stock
#             if stock > 0:
#                 book.availability = True
#             book.save()


@receiver(signals.post_save, sender=Record)
def is_borrowed(sender, instance, created, **kwargs):
    if not instance.book_returned:
        if created:
            stock = instance.borrowed_book.in_stock
            if stock > 0:
                stock -= 1
                book = instance.borrowed_book
                book.in_stock = stock
                if stock <= 0:
                    book.availability = False
                book.save()
    else:
        stock = instance.borrowed_book.in_stock
        book = instance.borrowed_book
        book.in_stock = stock + 1
        book.save()
