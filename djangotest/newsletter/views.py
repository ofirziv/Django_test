from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import ContactForm, SignUpForm
# Create your views here.
def home(request):
	title = 'Welcome'
	# if request.user.is_authenticated:
	# 	# is_authenticated was once a function' now it's an attribute
	# 	title = "My Title {}".format(request.user)

	# add form
	# if request.method == "POST": #if post method, printing the post details 
	# 	print("{}".format(request.POST))
	form = SignUpForm(request.POST or None)	
	context = {
		"title": title,
		"form": form
	}


	if form.is_valid():
		instance = form.save(commit=False)
		full_name = form.cleaned_data.get("full_name")
		email = form.cleaned_data.get("email")
		if not full_name:
			full_name = 'New Full Name'
		if not email:
			email = 'admin@example.edu'
		instance.full_name = full_name
		instance.email = email
		# if not instance.full_name:
		# 	instance.full_name = 'Justin'
		instance.save() # save the instance in the database
		context = {
			"title": "Thank you"
		}
	return render(request, "home.html", context)


def contact(request):
	title = 'Contact Us'
	title_aligned_center = True
	form = ContactForm(request.POST or None)
	if form.is_valid():
		# for key in form.cleaned_data:
		# 	print(key, form.cleaned_data.get(key))
		form_email = form.cleaned_data.get("email")
		form_message = form.cleaned_data.get("message")
		form_full_name = form.cleaned_data.get("full_name")
		# print(email, message, full_name)
		subject = "Site contact form"
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email, "ofirziv@gmail.comm"]
		contact_message = "{}: {}".format(form_full_name, form_message)
		send_mail(subject, 
			contact_message, 
			from_email, 
			to_email, 
			fail_silently=False)

	context = {
		"form": form,
		"title": title,
		"title_aligned_center": title_aligned_center
	}

	return render(request, "forms.html", context)











