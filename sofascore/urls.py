from django.urls import path


from . import views

urlpatterns = [
    path('', views.home_view, name='main_table'),
    path('update', views.update_package, name='package'),
    path('preds_package', views.preds_package, name='preds_package')
    ]