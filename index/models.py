from django.db import models
import os

# Create your models here.

class Journal(models.Model):
	journal_name 		= models.CharField(verbose_name = "Journal", max_length=100)
	abbr_title			= models.CharField(verbose_name = "Abbr. Title", max_length=100)
	journal_url 		= models.CharField(verbose_name = "Journal URL", max_length=50)
	subject				= models.CharField(verbose_name = "subject", max_length=50, null= True, blank=True)
	issn_print 			= models.CharField(verbose_name = "ISSN Print", max_length=50 )
	issn_online			= models.CharField(verbose_name = "ISSN Online", max_length=50 )
	frequency			= models.CharField(verbose_name = "Frequency", max_length=50, blank=True, default="N/A")
	chief_editor		= models.CharField(verbose_name = "chief editor", max_length=50)
	origin_country		= models.CharField(verbose_name = "Origin", max_length=50,  blank=True, default="N/A")
	language			= models.CharField(verbose_name = "Language", max_length=50, blank=True, default="N/A")
	publisher			= models.CharField(verbose_name = "Publisher", max_length=50, blank=True, default="N/A")
	journal_info		= models.TextField(verbose_name = "Info", max_length=2000)
	journal_scope		= models.TextField(verbose_name = 'Scope', max_length=2000, null=True, blank=True)
	journal_cover		= models.ImageField(upload_to ='journals/', verbose_name = "Cover")
	journal_thumb		= models.ImageField(upload_to ='journals/', verbose_name = "Thumbnail")
	
	def __str__(self):
		return self.journal_name


class Volume(models.Model):
	journal 			= models.ForeignKey(Journal, on_delete=models.CASCADE)
	volume_name			= models.CharField(verbose_name = "Volume name", max_length=100)
	volume_year			= models.PositiveIntegerField(verbose_name="Year")
	issue_name			= models.CharField(verbose_name="Issue", max_length=100)

	def __str__(self):
		return self.volume_name

class Article(models.Model):
	volume 				= models.ForeignKey(Volume, on_delete=models.CASCADE)
	article_type		= models.CharField(verbose_name="Type", max_length=40)
	article_name 		= models.CharField(verbose_name = "Article", max_length=500)
	article_abbr		= models.CharField(verbose_name='Abbr', max_length=100, blank=True, null=True)
	author				= models.CharField(verbose_name = "Author", max_length=200)
	article 			= models.FileField(upload_to='articles/')
	abstract			= models.TextField(verbose_name='Abstract', max_length=2000, null=True, blank=True)
	doi 				= models.CharField(verbose_name='DOI', max_length=100)
	publish_date		= models.DateField()

	def __str__(self):
		return self.article_name

class Editor(models.Model):
	journal 			= models.ForeignKey(Journal, on_delete=models.CASCADE )
	designation 		= models.CharField(verbose_name="Designation", max_length=200)
	editor_name 		= models.CharField(verbose_name="Name", max_length=200)
	editor_info 		= models.CharField(verbose_name="Info", max_length=1000)
	profile				= models.ImageField(upload_to='editors/', blank=True, null=True)

	def __str__(self):
		return self.editor_name


#Featured Articles
def validate_only_ten(obj):
    model = obj.__class__
    if (model.objects.count() > 9 and
            obj.id != model.objects.get().id):
        raise ValidationError("Can only create 10 %s instance" % model.__name__)

class FeaturedArticle(models.Model):
	article_name 		= models.CharField(verbose_name = "Article", max_length=500)
	author				= models.CharField(verbose_name = "Author", max_length=200)
	article_type		= models.CharField(verbose_name="Type", max_length=40)
	article_abbr		= models.CharField(verbose_name='Abbr', max_length=100, blank=True, null=True)
	article 			= models.FileField(upload_to='features_articles/', blank=True)
	abstract			= models.TextField(verbose_name='Abstract', max_length=2000, null=True, blank=True)
	doi 				= models.CharField(verbose_name='DOI', max_length=100, null=True,blank=True)
	publish_date		= models.DateField()

	def clean(self):
		validate_only_ten(self)

	def __str__(self):
		return self.article_name

class TopEditor(models.Model):
	designation 		= models.CharField(verbose_name="Designation", max_length=200)
	editor_name 		= models.CharField(verbose_name="Name", max_length=200)
	editor_info 		= models.CharField(verbose_name="Info", max_length=1000)
	profile				= models.ImageField(upload_to='editors/', blank=True, null=True)

	def __str__(self):
		return self.editor_name


class TopReviewer(models.Model):
	designation 		= models.CharField(verbose_name="Reviewer Designation", max_length=200)
	reviewer_name 		= models.CharField(verbose_name="Reviewer Name", max_length=200)
	reviewer_info 		= models.CharField(verbose_name="Reviewer Info", max_length=1000)
	profile				= models.ImageField(upload_to='reviewers/', blank=True, null=True)

	def __str__(self):
		return self.reviewer_name

#Processing Fees
class JournalFee(models.Model):
	journal = models.ForeignKey(Journal, on_delete=models.CASCADE)
	usd 	= models.PositiveIntegerField(verbose_name="USD", null=True, blank=True)
	inr 	= models.PositiveIntegerField(verbose_name="INR", null=True, blank=True)

class MemberIn(models.Model):
	company_logo = models.ImageField(upload_to='membersin/', blank=True)
	company_name = models.CharField(verbose_name='Company name', blank=True, max_length=200)

	def __str__(self):
		return self.company_name

class Testimony(models.Model):
	testimony 		= models.TextField(verbose_name='testimony', max_length=2000)
	testimony_name	= models.CharField(verbose_name='Name', max_length=200)
	testimony_desg	= models.CharField(verbose_name='Designation(if any)', max_length=200, blank=True, null=True)
	testimony_dp	= models.ImageField(upload_to='testimony_dp/', blank=True, null=True)

	def __str__(self):
		return self.testimony_name

class Indexing(models.Model):
	journal = models.ForeignKey(Journal, on_delete=models.CASCADE)
	index_name = models.CharField(verbose_name='Indexing Name', max_length=300, null=True, blank=True)
	index_picture = models.ImageField(upload_to='indexing/', blank=True, null=True)
	index_url = models.CharField(verbose_name='Indexing URL', max_length=500, null=True, blank=True)

class ImpactFactor(models.Model):
	journal = models.ForeignKey(Journal, on_delete=models.CASCADE)
	impact_factor = models.CharField(verbose_name='Impact Factor', max_length=300, null=True, blank=True)
	impact_year = models.CharField(verbose_name='Impact Factor Year', max_length=500, null=True, blank=True)
	impact_url	= models.CharField(verbose_name='Impact URL', max_length=500, blank=True, null=True)

	def __str__(self):
		return self.journal.journal_name

class AuthorOfTheMonth(models.Model):
	author_name = models.CharField(verbose_name='Author Name', max_length=300, null=True, blank=True)
	author_desg = models.CharField(verbose_name='Author Designation', max_length=500, null=True, blank=True)
	author_dp	= models.ImageField(upload_to='author_of_the_month/', blank=True, null=True)
	last_updated= models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.author_name


class GlobalIndexing(models.Model):
	index_name = models.CharField(verbose_name='Indexer Name', max_length=300, null=True, blank=True)
	index_picture = models.ImageField(upload_to='indexer Logo', blank=True, null=True)
	index_url = models.CharField(verbose_name='Indexer URL(including http/https)', max_length=500, null=True, blank=True)

	def __str__(self):
		return self.index_name