from django.urls import path

from . import views
urlpatterns = [
  path("", views.home, name="home"),
  path("signup/", views.signup, name="signup"),
  path("signin/", views.signin, name="signin"),
  path("logout/", views.logout_view, name="logout"),
  path("makepaper/question/", views.question, name="question"),
  path("makepaper/", views.makePaper, name="makepaper"),
  path("alltests/", views.allTests, name="alltests"),
  path("alltests/taketest/", views.takeTest, name="takeTest"),
  path("alltests/taketest/paper_done",views.paper_done,name="paper_done"),

]
