from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from hashtagtube.models import Category
from hashtagtube.models import Page
from hashtagtube.forms import UserForm, UserProfileForm

def index(request):
    # Order the pages by the number of views in descending order.
    # Retrieve the top 4 only 
    category_list = Category.objects.order_by('-title')[:5]
    page_list = Page.objects.order_by('-views')[:4]

    context_dict = {}
    context_dict['categories'] = category_list
    context_dict['pages'] = page_list


    #Obtain our response object early so we can add cookie information.
    response = render(request, 'hashtagtube/index.html', context=context_dict)

    return response

def user_login(request):
    #If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
    	username = request.POST.get('username')
    	password = request.POST.get('password')
        
        # Use Django's machinery to attempt to see if the username/password 
        # combination is valid - a User object is returned if it is
    	user = authenticate(username=username, password=password)

    	# If we have a User object, the details are correct.
    	if user:
    		# Is the account is active? It could have been disabled
    		if user.is_active:
    			# If the account is valid and active, we can log the user in.
    			# We'll send the user back to the homepage.
    			lgoin(request, user)
    			return redirect(reverse('hashtagtube:index'))
    		else:
    			# An inactive account was used - no logging in!
    			return HttpResponse("Your hashtagtube account is disabled.")
    	else:
            # Bad login details was provided, so we can't log the user in.
            print("Invalid login details: {username}, {password}")
            return HttpResponse("Invalid lgoin details supplied.")
    # The request is not a HTTP POST, so display the login form
    else:
        return render(request, 'hashtagtube/login.html')

def register(request):
	# A boolean value for telling the template 
	# whether the registration was successful.
	# Set to False initially. 
	# Code changes value to True when registration succeeds.
	registered = False

	# If it's a HTTP POST
	if request.method == 'POST':
		# Attempt to grab information from the raw form information.
		# Note that we make use of both UserForm and UserProfileForm.
		user_form = UserForm(request.POST)
		profile_form = UserProfileForm(request.POST)

		# If the two forms are valid...
		if user_form.is_valid() and profile_form.is_valid():
			#Save the user's form date to the database.
			user = user_form.save()

			# Now we hash the password with the set_password method.
			# Once hashed, we can update the user object.
			user.set_password(user.password)
			user.save()

			# Now sort out the UserProfile instance.
			# Since we need to set the user attribute ourselves.
			# we set commit=False. This delays saving the model
			# until we're ready to avoid integrity problems.
			profile = profile_form.save(commit=False)
			profile.user = user

			# Did the user provdie a profile picture?
			# If so, we need to get it from the input form and 
			# put it in the UserProfile model.
			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']

			profile.save()

			registered = True
		else:
			# Invalid form or forms
			# Print problems to the terminal
			print(user_form.errors, profile_form.errors)
	else:
		# Not a HTTP POST, so we render our form using two ModelForm instances.
		# These forms will be blank, ready for user input.
		user_form = UserForm()
		profile_form = UserProfileForm()
	#render the template depending on the context.
	return render(request, 'hashtagtube.register.html',
		           context = {'user_form': user_form,
		                       'profile_form': profile_form,
		                       'registered': registered})


















