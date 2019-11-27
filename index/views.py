# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from index.models import *
from django.core.mail import send_mail, EmailMessage 
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

def index(request):
	context = {}
	journals = Journal.objects.all()
	top_editors = TopEditor.objects.all()
	top_reviewers = TopReviewer.objects.all()
	featured_articles = FeaturedArticle.objects.all().order_by('-publish_date')[:10]
	memberin = MemberIn.objects.all()
	testimonies = Testimony.objects.all()
	global_indexing = GlobalIndexing.objects.all()
	aotm = AuthorOfTheMonth.objects.order_by('-id').first()
	context = {
		'aotm'	: aotm,
		'top_editors' : top_editors,
		'top_reviewers' : top_reviewers,
		'featured_articles' : featured_articles,
		'journals' : journals,
		'memberin' : memberin,
		'testimonies' : testimonies,
		'global_indexing' : global_indexing,
	}
	return render(request, 'index/index.html', context )

def about_us(request):
	context = {}
	journals = Journal.objects.all()
	top_editors = TopEditor.objects.all()
	top_reviewers = TopReviewer.objects.all()
	aotm = AuthorOfTheMonth.objects.order_by('-id').first()
	memberin = MemberIn.objects.all()
	context = {
		'aotm' : aotm,
		'top_editors' : top_editors,
		'top_reviewers' : top_reviewers,
		'journals' : journals,
		'memberin' : memberin
	}
	return render(request, 'index/about_us.html', context)

def contact_us(request):
	context = {}
	journals = Journal.objects.all()
	top_editors = TopEditor.objects.all()
	top_reviewers = TopReviewer.objects.all()
	aotm = AuthorOfTheMonth.objects.order_by('-id').first()
	memberin = MemberIn.objects.all()
	context = {
		'top_editors' : top_editors,
		'top_reviewers' : top_reviewers,
		'aotm' : aotm,
		'journals' : journals,
		'memberin' : memberin
	}
	return render(request, 'index/contact_us.html', context)

def journals(request):
	context = {}
	journals = Journal.objects.all().order_by('id')
	top_editors = TopEditor.objects.all()
	top_reviewers = TopReviewer.objects.all()
	aotm = AuthorOfTheMonth.objects.order_by('-id').first()
	memberin = MemberIn.objects.all()
	context = {
		'top_editors' : top_editors,
		'top_reviewers' : top_reviewers,
		'aotm' : aotm,
		'journals' : journals,
		'memberin' : memberin
	}
	return render(request, 'index/journals.html', context)

def journal_details(request, url):
	context = {}
	journals = Journal.objects.all()
	journal = Journal.objects.filter(journal_url = url).first()
	volumes = Volume.objects.filter(journal_id = journal.id).order_by('-volume_year', 'id')
	editors = Editor.objects.filter(journal_id = journal.id)
	indexing = Indexing.objects.filter(journal_id = journal.id)
	impact_factor = ImpactFactor.objects.filter(journal_id = journal.id)
	aotm = AuthorOfTheMonth.objects.order_by('-id').first()
	top_editors = TopEditor.objects.all()
	top_reviewers = TopReviewer.objects.all()
	memberin = MemberIn.objects.all()
	articles = Article.objects.all().filter(volume__journal__id = journal.id).order_by('-publish_date')[:7]
	'''for volume in volumes:
		for article in filtered_article.all().filter(volume = volume):
			articles.append(article)
	articles = list(articles)[:7]'''
	latest_articles = Article.objects.all().order_by('-publish_date')
	context = {
		'latest_articles' : latest_articles,
		'journal' 	: journal,
		'volumes' 	: volumes,
		'featured_articles'	: articles,
		'editors'	: editors,
		'journals'	: journals,
		'top_editors' : top_editors,
		'top_reviewers' : top_reviewers,
		'memberin' : memberin,
		'indexing' : indexing,
		'impact_factor' : impact_factor,
		'aotm' : aotm,
	}
	return render(request, 'index/journal_details.html', context)

def volume_articles(request, url, vol, issue):
	context = {}
	journals = Journal.objects.all()
	top_editors = TopEditor.objects.all()
	top_reviewers = TopReviewer.objects.all()
	memberin = MemberIn.objects.all()
	journal = Journal.objects.get(journal_url = url)
	volume = Volume.objects.get(journal=journal, volume_name=vol, issue_name=issue)
	volume_name = volume
	issue_name = volume.issue_name
	articles = Article.objects.filter(volume=volume)
	aotm = AuthorOfTheMonth.objects.order_by('-id').first()
	context = {
		'volume_name' 	: volume_name,
		'issue_name' 	: issue_name,
		'featured_articles'		: articles,
		'journal'		: journal,
		'top_editors' : top_editors,
		'top_reviewers' : top_reviewers,
		'journals' : journals,
		'memberin' : memberin,
		'aotm' : aotm,
	}
	return render(request, 'index/volume_articles.html', context)

def author_guidelines(request):
	context = {}
	journals = Journal.objects.all()
	top_editors = TopEditor.objects.all()
	top_reviewers = TopReviewer.objects.all()
	aotm = AuthorOfTheMonth.objects.order_by('-id').first()
	memberin = MemberIn.objects.all()
	context = {
		'top_editors' : top_editors,
		'top_reviewers' : top_reviewers,
		'journals' : journals,
		'memberin' : memberin,
		'aotm' : aotm,
	}
	return render(request, 'index/author_guidelines.html', context)

def processing_fees(request):
	context = {}
	journal_fees = JournalFee.objects.all()
	journals = Journal.objects.all()
	top_editors = TopEditor.objects.all()
	top_reviewers = TopReviewer.objects.all()
	aotm = AuthorOfTheMonth.objects.order_by('-id').first()
	memberin = MemberIn.objects.all()
	context = {
		'top_editors' : top_editors,
		'top_reviewers' : top_reviewers,
		'aotm' : aotm,
		'journals' : journals,
		'memberin' : memberin,
		'journal_fees': journal_fees
	}
	return render(request, 'index/processing_fees.html', context)


def submitManuscript(request):
	context = {}
	journals = Journal.objects.all()
	top_editors = TopEditor.objects.all()
	top_reviewers = TopReviewer.objects.all()
	aotm = AuthorOfTheMonth.objects.order_by('-id').first()
	memberin = MemberIn.objects.all()
	context = {
		'top_editors' : top_editors,
		'top_reviewers' : top_reviewers,
		'aotm' : aotm,
		'journals' : journals,
		'memberin' : memberin
	}
	if request.POST:
		data = request.POST
		file = request.FILES['file']
		subject = 'Manuscript Submission'
		message = '------Personal Details------' + '\n\n' + 'Name : ' + data['title'] + ' ' + data['first'] + ' ' + data['last'] + '\n' + 'University : ' + data['university'] + '\n' + 'Address : ' + data['address'] + '\n' + 'Email : ' + data['email'] + '\n' + 'Phone : ' + data['phone'] + '\n\n' + '------Document Details------' + '\n\n' + 'Journal : ' + data['journal'] + '\n'	+ 'Artile Type : ' + data['article-type'] + '\n' + 'Manuscript Title : ' + data['manuscript-title'] + '\n' + 'Abstract : ' + data['abstract'] + '\n'
		email_from = settings.EMAIL_HOST_USER
		recipient_list = ['easpublisher@gmail.com',]
		email = EmailMessage( subject, message, email_from, recipient_list )
		email.attach(file.name, file.read(), file.content_type)
		email.send()
		return render(request, 'index/submitted.html', {})
	return render(request, 'index/submitManuscript.html', context)

def submitted(request):
	return render(request, 'index/submitted.html', {})

@csrf_exempt
def online_payment(request):
	return render(request, 'index/online_payment.html' ,{})

def reviewer_login(request):
	return render(request, 'index/reviewer_login.html' ,{})

def editor_login(request):
	return render(request, 'index/editor_login.html' ,{})

def publication_ethics(request):
	context = {}
	journals = Journal.objects.all()
	top_editors = TopEditor.objects.all()
	top_reviewers = TopReviewer.objects.all()
	memberin = MemberIn.objects.all()
	aotm = AuthorOfTheMonth.objects.order_by('-id').first()
	context = {
		'top_editors' : top_editors,
		'journals' : journals,
		'memberin' : memberin,
		'aotm' : aotm,
		'top_reviewers' : top_reviewers,
	}
	return render(request, 'index/publication_ethics.html' ,context)

def publication_certificate(request):
	context = {}
	journals = Journal.objects.all()
	top_editors = TopEditor.objects.all()
	top_reviewers = TopReviewer.objects.all()
	memberin = MemberIn.objects.all()
	aotm = AuthorOfTheMonth.objects.order_by('-id').first()
	context = {
		'top_editors' : top_editors,
		'journals' : journals,
		'memberin' : memberin,
		'aotm' : aotm,
		'top_reviewers' : top_reviewers,
	}
	if request.POST:
		data = request.POST
		subject = 'Publication Certificate'
		message = '------Details------' + '\n\n' + 'Manuscript Title : ' + data['title'] + '\n' + 'Author(s) : ' + data['authors'] + '\n' + 'Journal : ' + data['journal'] + '\n' + 'Publication Year : ' + data['pub_year'] + '\n' + 'Volume : ' + data['volume'] + '\n' + 'Issue : ' + data['issue'] + '\n' + 'Page Numbers: ' + data['pg_no'] + '\n' + 'Email : ' + data['email'] + '\n' + 'Phone : ' + data['phone'] 
		email_from = settings.EMAIL_HOST_USER
		recipient_list = ['easpublisher@gmail.com',]
		email = EmailMessage( subject, message, email_from, recipient_list )
		email.send()
		return render(request, 'index/submitted.html', {})
	return render(request, 'index/publication_certificate.html' ,context)


def editorial_certificate(request):
	context = {}
	journals = Journal.objects.all()
	top_editors = TopEditor.objects.all()
	top_reviewers = TopReviewer.objects.all()
	memberin = MemberIn.objects.all()
	aotm = AuthorOfTheMonth.objects.order_by('-id').first()
	context = {
		'top_editors' : top_editors,
		'journals' : journals,
		'memberin' : memberin,
		'aotm' : aotm,
		'top_reviewers' : top_reviewers,
	}
	if request.POST:
		data = request.POST
		subject = 'Editorial Certificate'
		message = '------Details------' + '\n\n' + 'Full Name : ' + data['name'] + '\n' + 'Complete Affiliation : ' + data['affiliation'] + '\n' + 'Journal : ' + data['journal'] + '\n' + 'Certificate Type : ' + data['certificate'] + '\n' + 'Email : ' + data['email'] + '\n' + 'Phone : ' + data['phone'] 
		email_from = settings.EMAIL_HOST_USER
		recipient_list = ['easpublisher@gmail.com',]
		email = EmailMessage( subject, message, email_from, recipient_list )
		email.send()
		return render(request, 'index/submitted.html', {})
	return render(request, 'index/editorial_certificate.html' ,context)


def reviewer_certificate(request):
	context = {}
	journals = Journal.objects.all()
	top_editors = TopEditor.objects.all()
	top_reviewers = TopReviewer.objects.all()
	memberin = MemberIn.objects.all()
	aotm = AuthorOfTheMonth.objects.order_by('-id').first()
	context = {
		'top_editors' : top_editors,
		'journals' : journals,
		'memberin' : memberin,
		'aotm' : aotm,
		'top_reviewers' : top_reviewers,
	}
	if request.POST:
		data = request.POST
		subject = 'Reviewer Certificate'
		message = '------Details------' + '\n\n' + 'Full Name : ' + data['name'] + '\n' + 'Complete Affiliation : ' + data['affiliation'] + '\n' + 'Journal : ' + data['journal'] + '\n' + 'Certificate Type : ' + data['certificate'] + '\n' + 'Email : ' + data['email'] + '\n' + 'Phone : ' + data['phone'] 
		email_from = settings.EMAIL_HOST_USER
		recipient_list = ['easpublisher@gmail.com',]
		email = EmailMessage( subject, message, email_from, recipient_list )
		email.send()
		return render(request, 'index/submitted.html', {})
	return render(request, 'index/reviewer_certificate.html' ,context)

@csrf_exempt
def paypal_transaction_complete(request):
	if request.POST:
		pass
		#print(request.POST)
	return response('success')


def global_indexing(request):
	context = {}
	journal_fees = JournalFee.objects.all()
	journals = Journal.objects.all()
	top_editors = TopEditor.objects.all()
	top_reviewers = TopReviewer.objects.all()
	aotm = AuthorOfTheMonth.objects.order_by('-id').first()
	memberin = MemberIn.objects.all()
	global_indexing = GlobalIndexing.objects.all()
	context = {
		'top_editors' : top_editors,
		'aotm' : aotm,
		'journals' : journals,
		'memberin' : memberin,
		'global_indexing' : global_indexing,
		'top_reviewers' : top_reviewers,
	}
	return render(request, 'index/global_indexing.html', context)
