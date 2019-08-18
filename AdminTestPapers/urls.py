from django.urls import path

from . import views
urlpatterns = [
  path("", views.home, name="home"),
  path("signup/", views.signup, name="signup"),
  path("signin/", views.signin, name="signin"),
  path("logout/", views.logout_view, name="logout"),
  path("makepaper/question/", views.question, name="question"),
  path("makepaper/", views.makePaper, name="makepaper"),
  path("taketest/", views.takeTest, name="takeTest"),

]
