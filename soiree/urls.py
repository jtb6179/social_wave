from django.urls import path
from .views import MemoDetails, MemoAPIView, GenericUserAPIView, UserAPIView
from django.conf import settings
from django.conf.urls.static import static

# from soiree.views import homePage, specific_memo

urlpatterns = [
    path('memos/', MemoAPIView.as_view()),
    path('memos/<int:id>', GenericUserAPIView.as_view()),
    # path('memos/', memo_list),
    # path('memo_details/<int:pk>', memo_detail),
    path('memo_details/<int:pk>/', MemoDetails.as_view()),
    path('users/', UserAPIView.as_view()),
    path('user/<int:id>', GenericUserAPIView.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)