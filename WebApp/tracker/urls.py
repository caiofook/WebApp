from django.urls import path
import tracker.views as tracker_views


#o path abaixo fica vazio pra indicar que é a home page.
#observe o <int:pk> para filtrar injections
urlpatterns=[
    path('', tracker_views.tracker, name='tracker'),
    path('load_tracker_data/', tracker_views.load_tracker_data, name='tracker_load'),
    path('save_tracker_data/', tracker_views.save_tracker_data, name='tracker_save')
]

