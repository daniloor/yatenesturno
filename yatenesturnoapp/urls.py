from django.urls import path

from yatenesturnoapp import views



urlpatterns = [
    path('',views.home, name="home"),
    path('categorias',views.categories,name="categories" ),
    path('contacto',views.contact,name="contact" ),
    path('pasos',views.steps,name="steps"),
    path('categorias/<categoryName>',views.categorytype,name="categorytype" )

]
