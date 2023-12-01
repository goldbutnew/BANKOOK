from django.urls import path
from . import views


urlpatterns = [
    # 게시판 urls
    path('articles/', views.article_list),
    path('articles/<int:article_pk>/', views.article_detail),
    path('comments/all/<int:article_pk>', views.comment_list),
    path('comments/<int:comment_pk>/', views.comment_detail),
    path('articles/<int:article_pk>/comments/', views.comment_create),

    # 예/적금 urls
    path('deposit/', views.deposit_product_save),
    path('deposit/data/', views.deposit_product_DB),
    path('deposit/option/', views.deposit_option_DB),
    path('saving/', views.saving_product_save),
    path('saving/data/', views.saving_product_DB),
    path('saving/option/', views.saving_option_DB),

    # 환율 urls
    path('exchanges/', views.exchanges),
]
