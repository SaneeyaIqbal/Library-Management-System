from django.test import TestCase
#from libraryapp.models import Book
from .models import Book,Author,Member


class AuthorTestCase(TestCase):
    def setUp(self):
        Author.objects.create(author_name="brettMard")
        Author.objects.create(author_name="willey")

    def test_case_author_correct_title(self):
        brettMard = Author.objects.get(author_name="brettMard")
        willey = Author.objects.get(author_name="willey")
        self.assertEqual(brettMard.get_title(), "brettMard")
        self.assertEqual(willey.get_title(), "willey")


# class BookTestCase(TestCase):
#     def setUp(self):
#         Author.objects.create(author_name="brettmard")
#         Book.objects.create(book_name="Postgresql",ISBN = "1234567891",category="Database",
#                             availability="True",number_of_copy="2",in_stock="3",book_price="100")
#
#
#     def test_case_book_correct_title(self):
#         postgresql = Book.objects.get(book_name="Postgresql",ISBN = "1234567891")
#         brettmard = Author.objects.get(author_name="brettmard")
#
#         self.assertEqual(postgresql.get_title(),"Postgresql","1234567891")
#
#         self.assertEqual(brettmard.get_author(),"brettmard")

class MemberTestCase(TestCase):
    def setUp(self):
        Member.objects.create(member_ID = 1,member_name="Saniya",member_contact="2256565",
                              member_email="s.saneeya@gmail.com",member_address="Tumkur")

    def test_case_member_correct_details(self):
        Saniya = Member.objects.get(member_name="Saniya",member_address="Tumkur")

        self.assertEqual(Saniya.get_details(),"SaniyaTumkur")