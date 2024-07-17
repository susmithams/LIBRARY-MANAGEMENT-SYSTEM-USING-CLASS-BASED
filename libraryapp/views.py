from django.shortcuts import render,HttpResponse,redirect
from django.views import generic
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,authenticate
from .models import *
from datetime import datetime,timedelta
from django.utils import timezone


from django.shortcuts import get_object_or_404
# Create your views here.

# class index(generic.View):
#     template_name='index.html'

def Index(request):
    return render(request,'index.html')
class studentreg(generic.CreateView):
    form_class = studregform
    template_name = 'student.html'
    success_url = reverse_lazy('slogin')
    def form_valid(self, form):
        user =form.save(commit=False)
        password=form.cleaned_data['password']
        user.set_password(password)
        user.save()
        department=form.cleaned_data['department']
        phone=form.cleaned_data['phone']
        roll_no=form.cleaned_data['roll_no']
        register_id=form.cleaned_data['register_id']
        college_name=form.cleaned_data['college_name']
        userdetails.objects.create(user=user,department=department,phone=phone,roll_no=roll_no,register_id=register_id,college_name=college_name)
        return super().form_valid(form)


class studlogin(generic.View):
    form_class=AuthenticationForm
    template_name='studlogin.html'
    def get(self,request):
        data=User.objects.all()
        for i in data:
            request.session['userid']=i.id
        form=AuthenticationForm
        return render(request,'studlogin.html',{'form':form})
    def post(self,request):
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('profile')
            else:
                return HttpResponse('Invalid credentials...')
        else:
            return HttpResponse('Form is invalid...')

def success(request):
    return render(request,'success.html')


class ProfileView(generic.DetailView):
    model = userdetails
    template_name = 'profile.html'
    context_object_name = 'user'
    def get_object(self): #
        # userid = self.request.session.get('userid')
        # return userdetails.objects.get(user_id=userid)
          user=self.request.user #this is the method that is used to get the details of current logged in user
          return get_object_or_404(userdetails,user=user)
#it returns userdetails that matches the user datas that are logged in
class profileUpdate(generic.UpdateView):
    model = User
    form_class=EditProfileForm
    template_name = 'userupdate.html'
    success_url = reverse_lazy('profile')

    def get_object(self): #getting any object coming into the function
        user=super().get_object()   #method used to get datas into the user( here ,primary key)get object with a specific id passing into the url
        self.userdetails_instance=userdetails.objects.get(user=user)   #oroo instanceilekkum corresponding data store cheyyanam.the instance value
                    #which is used in django forms to specify which perticular instance the form is prefilled
                    #what happens is that the form is filled with the data from the perticular record.
        return user
    def get_form(self,form_class=None):
               #get_form used to modify the forms that to be returned.its a builtin function
        form=super().get_form(form_class)   #we get the form of editprofile
        form.fields['phone'].initial=self.userdetails_instance.phone  #extra fields add cheyanam
        form.fields['department'].initial = self.userdetails_instance.department
        form.fields['roll_no'].initial = self.userdetails_instance.roll_no
        form.fields['register_id'].initial = self.userdetails_instance.register_id
        form.fields['college_name'].initial = self.userdetails_instance.college_name
        return form

    def form_valid(self,form):
        response=super().form_valid(form)
        self.userdetails_instance.phone=form.cleaned_data['phone']
        self.userdetails_instance.department = form.cleaned_data['department']
        self.userdetails_instance.roll_no = form.cleaned_data['roll_no']
        self.userdetails_instance.register_id = form.cleaned_data['register_id']
        self.userdetails_instance.college_name = form.cleaned_data['college_name']
        #save all other datas
        self.userdetails_instance.save()
        return response


class Add_Book(generic.CreateView):
    form_class = libbookform
    template_name = 'addbook.html'
    success_url = reverse_lazy('success')

class LibBooksView(generic.ListView):
    model = LibraryBookDetail
    template_name = 'booksview.html'
    context_object_name ='data'

class BookDelete(generic.DeleteView):
    model = LibraryBookDetail
    template_name = 'delete.html'
    success_url = reverse_lazy('booksview')


class BookView(generic.DetailView):
    model = LibraryBookDetail
    template_name = 'detailbookview.html'

class BookUpdate(generic.UpdateView):
    model = LibraryBookDetail
    template_name = 'bookupdate.html'
    fields = ['book_name','book_img','auther','book_id','description','available_copies']
    success_url = reverse_lazy('booksview')




class StudentBooksView(generic.ListView):
    model = LibraryBookDetail
    template_name = 'studentbooksview.html'
    context_object_name ='data'


class StudentSingleBookView(generic.DetailView):
    model = LibraryBookDetail
    template_name = 'studentdetailbookview.html'




#------------------book request function----------------------------------------

class CreateBookRequestView(generic.View):
    def get(self,request,pk):
        book=get_object_or_404(LibraryBookDetail,id=pk)  #pk aayittulla bookine modelill ninnum edukkuka
        user_detail=get_object_or_404(userdetails,user=request.user)  #login aayittulla user

        #check if the user has already requestedfor this book

        if BookRequest.objects.filter(user=user_detail,book=book).exists():
            return HttpResponse('you have already requested this book')
        else:
            BookRequest.objects.create(user=user_detail,book=book)
            return HttpResponse('your request has been sent')


class DisplayRequestBooksView(generic.ListView):
    model=BookRequest
    template_name='requested_books.html'
    context_object_name='requested_books'

#     you can override your query in listview using get_query()
    def get_queryset(self):
        user=self.request.user
        return BookRequest.objects.filter(user__user__id=user.id)


# ------------------------library section------------------------

def LibraryIndex(request):
    return render(request,'library_index.html')
class LibraryBookRequestView(generic.ListView):
    model = BookRequest
    template_name = 'librarybookrequestview.html'
    context_object_name ='books'




class AcceptButtonView(generic.View):
    def get(self,request,pk):
        book_request=get_object_or_404(BookRequest,id=pk)
        book=get_object_or_404(LibraryBookDetail,book_id=book_request.book.book_id)
        AcceptedBooksNewModel.objects.create(
            book_name=book_request.book.book_name,
            auther=book_request.book.auther,
            request_date=book_request.request_date,userd=book_request.user,
            return_date=timezone.now()+timedelta(days=10)

        )
        if book.availablecopies>0:
            book.availablecopies-=1
            book.save()
        else:
            return HttpResponse("no available copies left")
        book_request.delete()
        return HttpResponse("Request Accepted")
# class AcceptBooksRequestView(generic.View):
#     def get(self,request,pk,accepted_date=None):
#         book_request=get_object_or_404(BookRequest,id=pk)
#         accepted_book=AcceptedBooks.objects.create(details=book_request,
#                                                    fine=0,
#                                                    return_date=timezone.now()+timedelta(days=10))
#
#         accepted_date=accepted_book.accepted_date
#         current_date=timezone.now()
#         return_date=accepted_date+timedelta(days=10)
#
#         fine=0
#         if current_date>return_date:
#             days_late=(current_date-return_date).days
#             fine=days_late * 10
#         accepted_book.return_date=return_date
#         accepted_book.fine=fine
#         accepted_book.save()
#         # book_request.delete()
#         return HttpResponse('item accepted')
#         # return redirect(AcceptBooksView)

class AcceptBooksView(generic.ListView):
    model=AcceptedBooksNewModel
    template_name='Accepted_books.html '
    context_object_name = 'data'
    def get_queryset(self):
        queryset=super().get_queryset()    #objects.all()
        current_date=timezone.now()
        #data preprocess
        for accepted_book in queryset:
            if current_date > accepted_book.return_date:
                overdue_days = (current_date - accepted_book.return_date).days
                accepted_book.fine = overdue_days * 10
            else:
                accepted_book.fine=0
            accepted_book.save()   #save the calculated fine if you want to store it
        return queryset


###------------------------Logout section-----------------------------------------------------------------------------------------####
from django.contrib.auth import logout

class Logoutview(generic.View):
    def get(self,request):
        logout(request)
        return redirect('slogin')


class StudentBorrowBooks(generic.ListView):
    models=AcceptedBooksNewModel
    template_name="studentborrowbooks.html"
    context_object_name='data'

    def get_queryset(self):
        user = self.request.user
        return AcceptedBooksNewModel.objects.filter(userd__user__id=user.id)




###------------------------------------------------------------------------------------------------------#####
class userreg(generic.CreateView):
    form_class = RegisterForm
    template_name = 'employee.html'
    success_url = reverse_lazy('elogin')
    def form_valid(self, form):
        user =form.save(commit=False)
        password=form.cleaned_data['password']
        user.set_password(password)
        user.save()
        higher_qualification=form.cleaned_data['higher_qualification']
        phone=form.cleaned_data['phone']
        age=form.cleaned_data['age']
        job=form.cleaned_data['job']

        usermodel.objects.create(user=user,higher_qualification=higher_qualification,phone=phone,age=age,job=job)
        return super().form_valid(form)




class userlogin(generic.View):
    form_class=AuthenticationForm
    template_name='employeelogin.html'
    def get(self,request):
        data=User.objects.all()
        for i in data:
            request.session['userid']=i.id
        form=AuthenticationForm
        return render(request,'employeelogin.html',{'form':form})
    def post(self,request):
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('emp')
            else:
                return HttpResponse('Invalid credentials...')
        else:
            return HttpResponse('Form is invalid...')


class EmployeeView(generic.DetailView):
    model = usermodel
    template_name = 'employeeview.html'
    context_object_name = 'user'
    def get_object(self): #
        userid = self.request.session.get('userid')
        return usermodel.objects.get(user_id=userid)



class EmployeeUpdate(generic.UpdateView):
    model = User
    form_class=EdituserForm
    template_name = 'employeeupdate.html'
    success_url = reverse_lazy('emp')

    def get_object(self): #getting any object coming into the function
        user=super().get_object()   #method used to get datas into the user( here ,primary key)get object with a specific id passing into the url
        self.usermodel_instance=usermodel.objects.get(user=user)   #oroo instanceilekkum corresponding data store cheyyanam.the instance value
                    #which is used in django forms to specify which perticular instance the form is prefilled
                    #what happens is that the form is filled with the data from the perticular record.
        return user
    def get_form(self,form_class=None):
               #get_form used to modify the forms that to be returned.its a builtin function
        form=super().get_form(form_class)   #we get the form of editprofile
        form.fields['phone'].initial=self.usermodel_instance.phone  #extra fields add cheyanam
        form.fields['age'].initial = self.usermodel_instance.age
        form.fields['job'].initial = self.usermodel_instance.job
        form.fields['higher_qualification'].initial = self.usermodel_instance.higher_qualification
        return form

    def form_valid(self,form):
        response=super().form_valid(form)
        self.usermodel_instance.phone=form.cleaned_data['phone']
        self.usermodel_instance.age= form.cleaned_data['age']
        self.usermodel_instance.job = form.cleaned_data['job']
        self.usermodel_instance.higher_qualification = form.cleaned_data['higher_qualification']

        #save all other datas
        self.usermodel_instance.save()
        return response