from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.urls import path
from MyApp.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Course_Home, name="course_home"),
    path('course_list/', CourseList, name="courseList"),
    path("course_details/<int:m_id>/", Course_Details_Page, name = "course_detail"),
  #  path("course_details1/<int:m_id>/", Course_Details_Page1, name = "course_detail1"),
    path('login1/', Login1, name="login"),
    path('logout/', Logout, name="logout"),
    path('register/', Register, name="register"),
    path("payMentMake", MakePayment, name="payment"),
    path("gotocourse/<int:m_id>/<int:n_id>", GoToCourse, name="gotocourse"),
    path("PayCheck/<str:Usr>/", PayChack, name="paycheck"),
    path('contact/', Contact, name="contact"),
    path('about/', About, name="about"),

    path('admin_add_course/', Admin_Add_Course, name="add_course"),
    path('admin_add_lectures/', Admin_Add_Lectures, name="add_lectures"),
    path('admin_add_instructor/', Admin_Add_Instructor, name="add_instructor"),

              ]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
