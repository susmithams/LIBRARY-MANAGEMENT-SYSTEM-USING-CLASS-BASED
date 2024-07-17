
from django.urls import path
from .views import *

urlpatterns=[
    path('index/', Index),
    path('studentregister/',studentreg.as_view(),name='student'),
    path('studlogin/',studlogin.as_view(),name='slogin'),
    path('profileview/',ProfileView.as_view(),name='profile'),
    path('profileupdate/<pk>',profileUpdate.as_view(),name='proup'),
    path('addbook/',Add_Book.as_view(),name='addbook'),
    path('booksview/',LibBooksView.as_view(),name='booksview'),
    path('bookdelete/<pk>',BookDelete.as_view(),name='bookdelete'),
    path('bookdetail/<pk>',BookView.as_view(),name='bookview'),
    path('studentbooks/',StudentBooksView.as_view(),name='studentbooks'),
    path('studentbookdetail/<pk>',StudentSingleBookView.as_view(),name='studentbook'),

    path('request/<pk>', CreateBookRequestView.as_view(),name='create_request'),
    path('requestedbooks/',DisplayRequestBooksView.as_view(),name='display_request'),
    path('bookupdate/<pk>',BookUpdate.as_view(),name='bookupdate'),
    path('libbookrequest/',LibraryBookRequestView.as_view(),name='libraryview'),
    # path('acceptbooks/<pk>',AcceptBooksRequestView.as_view(),name='acceptbooks'),
    path('acceptbooksview/',AcceptBooksView.as_view(),name='acceptbookview'),
    path('acceptbuttonview/<pk>',AcceptButtonView.as_view(),name='acceptbuttonview'),
    path('studentborrow/',StudentBorrowBooks.as_view(),name='studentborrow'),
    path('libraryindex/',LibraryIndex),
    path('logout/',Logoutview.as_view(),name='logout'),

    path('successmsg/',success,name='success'),

    path('empregister/', userreg.as_view(), name='employee'),
    path('emplogin/', userlogin.as_view(), name='elogin'),
    path('empview/', EmployeeView.as_view(), name='emp'),
    path('empupdate/<pk>', EmployeeUpdate.as_view(), name='empup'),
]