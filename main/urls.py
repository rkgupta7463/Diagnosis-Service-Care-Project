from django.urls import path
from .views import index,heart_disease,kidney,debates

urlpatterns = [
    path('',index,name="index"),
    path('Heart Disease/prediction/',heart_disease,name="heart_disease"),
    path('Kidney Disease/prediction/',kidney,name="kidney_disease"),
    path('debates Disease/prediction/',debates,name="diabetes")
]
