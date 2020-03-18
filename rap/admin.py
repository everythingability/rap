from django.contrib import admin



from .models import  Author, Entry, Blog
from .models import Project, GTRCategory, HECategory, HEResearchArea, Person

#admin.site.register(Entry)
#admin.site.register(Author)
admin.site.register( Person )

#gtr_as_list

@admin.register(GTRCategory)
class GTRCategoryAdmin(admin.ModelAdmin):
	model = GTRCategory
	list_display = ('__str__',
	 
	   'areas_as_list',
	'id'
		
)




@admin.register(HEResearchArea)
class HEResearchAreaAdmin(admin.ModelAdmin):
	model = HEResearchArea
	list_display = ('__str__',
	   'children',
	   'gtr_as_list',
	'id'
		
)

@admin.register(Project)
class HEResearchAreaAdmin(admin.ModelAdmin):
	model = Project
	list_display = ('__str__','title','gtr_as_list', 'status')
	search_fields = ['title', "abstractText"]
	list_filter = ('leadFunder','leadOrganisation', 'status' )


admin.site.register([ HECategory])
