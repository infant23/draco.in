from django.shortcuts import redirect


def redirect_blog(request):
	return redirect('dracoin:index', permanent=True)