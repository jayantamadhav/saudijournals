# -*- coding: utf-8 -*-
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('submitManuscript/', views.submitManuscript , name="submitManuscript"),
    path('journals/', views.journals , name="journals"),
    path('about-us/', views.about_us, name="about_us"),
    path('contact-us/', views.contact_us, name="contact_us"),
    path('<str:url>', views.journal_details , name="journal_details"),
    path('journal-details/<str:url>/<str:vol>/<str:issue>', views.volume_articles , name="volume_articles"),
    path('author-guidelines/', views.author_guidelines , name="author_guidelines"),
    path('processing_fees/', views.processing_fees , name="processing_fees"),
    path('submitted', views.submitted, name='submitted'),
    path('online-payment/', views.online_payment, name='online_payment'),
    path('reviewer-login/', views.reviewer_login, name='reviewer_login'),
    path('editor-login/', views.editor_login, name='editor_login'),
    path('publication-ethics/', views.publication_ethics, name='publication_ethics'),
    path('publication-certificate/', views.publication_certificate, name='publication_certificate'),
    path('editorial-certificate/', views.editorial_certificate, name='editorial_certificate'),
    path('reviewer_certificate/', views.reviewer_certificate, name='reviewer_certificate'),
    path('indexing/', views.global_indexing, name='global_indexing'),
    path('paypal-transaction-complete/', views.paypal_transaction_complete, name='paypal-transaction-complete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)