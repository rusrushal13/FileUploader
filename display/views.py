from django.views import generic
from django.views.generic.edit import CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy
from .models import myfiles

class IndexView(generic.ListView):
	template_name ='display/index.html'
	
	def get_queryset(self):
		return myfiles.objects.all()

class DetailView(generic.DetailView):
	model =myfiles
	template_name ='display/details.html'

class FileCreate(CreateView):
	model =myfiles
	fields =['filename', 'type_of_file', 'size', 'location']


# from django.shortcuts import render, get_object_or_404
# from .models import myfiles

# def index(request):
# 	all_files =myfiles.objects.all()
# 	context ={'all_files': all_files}
# 	return render(request, 'display/index.html', context)

# def details(request, file_id):
# 	files =get_object_or_404(myfiles, pk =file_id)
# 	return render(request, 'display/details.html', {'files':files} )