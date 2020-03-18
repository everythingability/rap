from djongo import models # https://nesdis.github.io/djongo/get-started/
#from djongo.models.indexes import TextIndex
from djongo.models import CheckConstraint, Q
#from djongo.models.indexes import WildcardIndex
from django import forms
from datetime import datetime
#EmbeddedField

# An alternative to ManyToManyFields
#ArrayField https://nesdis.github.io/djongo/using-django-with-mongodb-array-field/

class HECategory( models.Model ):
    class Meta:
        verbose_name_plural = "HE Categories"
        verbose_name = "HE Category"
    name = models.CharField(max_length=255)
    search_terms = models.TextField(null=True, blank=True, default=None,
        help_text="These comma separated terms will searched for in projects. You don't need to add the Name")
    objects = models.DjongoManager()


    def __str__(self):
        #str(str(self.id) + "> " +
        return  str(self.name)

class GTRCategory(models.Model):

    class Meta:
        verbose_name_plural = "GtR Categories"
        verbose_name = "GtR Category"

    sid =  models.CharField(max_length=255, null=True, blank=True, default='') 
    name = models.CharField(max_length=255)
    percentage = models.IntegerField(null=True, blank=True, default=0)
    isHECategory = models.BooleanField(null=False,  default=False)

    objects = models.DjongoManager()

    def areas_as_list(self):
        # Reverse lookup
        s = ''
        for g in HEResearchArea.objects.filter(gtrs__id=self.id):
            s = s + str(g.name) + " , "
        return str(    s   )

    def __str__(self):
        return str(str(self.id) + "> " + self.name)

class HEResearchArea(models.Model):
    class Meta:
        verbose_name_plural = "HE Research Areas"
        verbose_name = "HE Research Area"

    hecategory = models.ForeignKey(HECategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    gtrs = models.ArrayReferenceField(
        to=GTRCategory,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    objects = models.DjongoManager()

    def gtr_as_list(self):
        # Children query
        s = ''
        for g in self.gtrs.all():
            s = s + str(g.name) + " , "
        return str(    s   )

    def children(self):
        
        return str(    self.gtrs.all().count()    )

    def __str__(self):
        return str(str(self.id) + "> " + self.name)


class Person(models.Model):
    id =  models.CharField(max_length=255, primary_key=True) 
    name = models.CharField(max_length=255, null=True, blank=True, default='')
    firstName = models.CharField(max_length=50, null=True, blank=True, default='')
    otherNames = models.CharField(max_length=50, null=True, blank=True, default='')
    surname = models.CharField(max_length=50, null=True, blank=True, default='')
    orchidID = models.CharField(max_length=50, null=True, blank=True, default='')

    def getName(self):
        return self.firstName + " " + self.otherNames + " " + self.surname

    def __str__(self):
        return  str(self.getName() )

class Organisation(models.Model):
    id =  models.CharField(max_length=255, primary_key=True) 
    name = models.CharField(max_length=255, null=True, blank=True, default='')
    
    class Meta:
        ordering = ('name',)

    def __str__(self):
        return str(self.name)

class Project(models.Model):

    '''
    'links', 'ext', 'id', 'outcomeid', 'href', 'created', 'updated', 'identifiers',
     'title', 'status', 'grantCategory', 'leadFunder', 'leadOrganisationDepartment', 
     'abstractText', 'techAbstractText', 'potentialImpact', 'healthCategories', 
     'researchActivities', 'researchSubjects', 'researchTopics', 'rcukProgrammes', 
     'start', 'end', 'participantValues'
    '''

    id =  models.CharField(max_length=255, primary_key=True)
    title = models.CharField(max_length=255)
    href = models.CharField(max_length=255, null=True, blank=True, default=None)
    abstractText = models.TextField(null=True, blank=True, default=None)
    start = models.DateField(null=True, blank=True, default=None )
    end = models.DateField(null=True, blank=True, default=None )
    created = models.DateField(null=True, blank=True, default=None )
    updated= models.DateField( null=True, blank=True, default=None)
    projectCategory = models.CharField(max_length=30,null=True, blank=True, default=None)
    leadFunder = models.CharField(max_length=30, null=True, blank=True, default=None)
    status = models.CharField(max_length=12, null=True, blank=True, default=None)
    awardPounds = models.IntegerField(null=True, blank=True, default=0)
    expenditurePounds = models.IntegerField(null=True, blank=True, default=0)
    department = models.CharField(max_length=255, null=True, blank=True, default='')
    GTRProjectUrl = models.CharField(max_length=255, null=True, blank=True, default=None)
    fundingOrgId = models.CharField(max_length=255, null=True, blank=True, default=None)
    pi = models.ForeignKey(Person, on_delete=models.CASCADE)
    leadOrganisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)


    gtrs = models.ArrayReferenceField(to=GTRCategory,on_delete=models.CASCADE,null=True,blank=True)
  
    objects = models.DjongoManager()

    def gtr_as_list(self):
        # Children query
        s = ''
        for g in self.gtrs.all():
            s = s + str(g.name) + " , "
        return str(    s   )

    def __str__(self):
        return str( self.title)



























class Blog(models.Model):
    class Meta:
        ''
        #abstract = True

    name = models.CharField(max_length=100)
    tagline = models.TextField(null=True, blank=True, default='')

    def __str__(self):
        return self.name
    
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = (
            'name', 'tagline'
        )

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(null=True, blank=True, default='')

    def __str__(self):
        return self.name

class Entry(models.Model):
    #blog = models.EmbeddedField(model_container=Blog)
    #
    #blog = models.EmbeddedField(model_container=Blog,model_form_class=BlogForm)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField( )
    mod_date = models.DateField(default=datetime.now, )
    authors = models.ArrayReferenceField(
        to=Author,
        on_delete=models.CASCADE,
    )
    n_comments = models.IntegerField(null=True, blank=True)
    n_pingbacks = models.IntegerField(null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True)
    objects = models.DjongoManager()

    class Meta:
        ''
        #indexes = [TextIndex(fields=['headline', ])]
        #constraints = [CheckConstraint(check=Q(author_age__gte=18), name='age_gte_18')]

    def __str__(self):
        return self.headline