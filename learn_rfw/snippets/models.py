from django.db import models

from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight



LEXERS =[ item for item in get_all_lexers() if item[1]]
Language_CHOICES = sorted([(item[1][0],item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([ (item,item) for item in get_all_styles() ])


# Create your models here.
class snippets(models.Model):
    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
    highlighted = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100,blank=True,default="")
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=Language_CHOICES,default="Python",max_length=100)
    style = models.CharField(choices=STYLE_CHOICES , default="friendly",max_length=100)
    
    # copy pasted code
    def save(self, *args, **kwargs):
   
        lexer = get_lexer_by_name(self.language)
        linenos = 'table' if self.linenos else False
        options = {'title': self.title} if self.title else {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos,
                                full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super(snippets, self).save(*args, **kwargs) 

    class Meta:
        ordering = ["created"]

# from django.contrib.gis.db import models
# from django.contrib.postgres.operations import CreateExtension
# from django.db import migrations

# class Migration(migrations.Migration):

#     operations = [
#         CreateExtension('postgis'),
#     ]


# class model1(models.Model):
#      geom = models.GeometryField(srid=4326,blank=True,null=True)
#      name = models.TextField(null=True)