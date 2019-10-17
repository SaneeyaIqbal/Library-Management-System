from django.contrib import admin
from django import forms
from .models import Librarian,Book,Member,Record


class LibrarianAdmin(admin.ModelAdmin):
    list_display = ('librarian_ID','librarian_name','librarian_contact',)
    ordering = ('librarian_ID',)


# class AuthorAdmin(admin.ModelAdmin):
#     list_display = ('author_name', 'about_author',)

class BookForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(BookForm,self).__init__(*args,**kwargs)
    def clean(self):
        book_name=self.cleaned_data.get('book_name')
        #category = self.cleaned_data.get('category')
        #in_stock = self.cleaned_data.get('in_stock')
        if len(book_name) < 10:
            raise forms.ValidationError("Name is too short",code="invalid")
        return self.cleaned_data

class BookAdmin(admin.ModelAdmin):
    list_display = ('isbn', 'book_name', 'category', 'number_of_copy', 'in_stock', 'is_available', 'price')
    ordering = ('book_name',)
    form = BookForm

class MemberAdminForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(MemberAdminForm,self).__init__(*args,**kwargs)
    def clean(self):
        member_name = self.cleaned_data.get('member_name')
        if len(member_name) < 10:
            raise forms.ValidationError("Name is short",code="invalid")
        return self.cleaned_data

class MemberAdmin(admin.ModelAdmin):
    list_display = ('member_ID', 'member_name', 'member_contact', 'member_email', 'member_address')
    ordering = ('member_name',)
    form = MemberAdminForm

# class RecordAdminForm(forms.ModelForm):
#    def __init__(self, *args, **kwargs):
#        super(RecordAdminForm, self).__init__(*args, **kwargs)
#    def clean(self):
#        borrowed_book =self.cleaned_data.get('borrowed_book')
#        if borrowed_book.in_stock == 0:
#            raise forms.ValidationError("Book is not available.", code="invalid")
#        return self.cleaned_data
#    def save(self, commit=True):
#        return super(RecordAdminForm, self).save(commit)

class RecordAdmin(admin.ModelAdmin):
    list_display = ('borrowed_ID', 'borrowed_member', 'borrowed_book', 'issued_librarian', 'issue_date', 'return_date',
                    'is_return', 'book_returned','returned_date')
    # form = RecordAdminForm


admin.site.register(Librarian, LibrarianAdmin)
#admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(Record, RecordAdmin)