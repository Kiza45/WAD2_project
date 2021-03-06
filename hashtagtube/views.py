from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from hashtagtube.models import Category, Comment
from hashtagtube.models import Page, UserProfile
from hashtagtube.forms import CategoryForm, PageForm
from hashtagtube.forms import UserForm, UserProfileForm
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime

def index(request):
    # Order the pages by the number of views in descending order.
    # Retrieve the top 4 only
    category_list = Category.objects.order_by('-title')[:5]
    page_list = Page.objects.order_by('-views')[:4]

    context_dict = {}
    context_dict['categories'] = category_list
    context_dict['page_list'] = page_list


    #Obtain our response object early so we can add cookie information.
    response = render(request, 'hashtagtube/index.html', context=context_dict)

    return response

def profile(request):

    followed = False
    category_list = Category.objects.order_by('-title')[:5]
    page_list = Page.objects.order_by('-views')[:4]

    try:
        session_user = UserProfile.user
    except ObjectDoesNotExist:
        return render(request, '404.html')

    context_dict = {}
    context_dict['categories'] = category_list
    context_dict['pages'] = page_list




    response = render(request, 'hashtagtube/profile.html', context=context_dict)
    return response


def video(request, video_id):
    try:
        video_file = Page.objects.get(id=video_id)
    except ObjectDoesNotExist:
        return render(request, 'hashtagtube/notFound.html')

    #session_user = User.objects.get(username=request.user.username)
    #video_comments = Comment.objects.filter(post=video_file).order_by('-id')
    video_file.views = video_file.views+1

    Liked = False
    #if session_user in video_file.likes.all():
    #    Liked = True

    return render(request, 'hashtagtube/video_page.html')


def show_category(request, category_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None
    return render(request, 'hashtagtube/category.html', context=context_dict)

@login_required
def add_category(request):
    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return redirect('/hashtagtube/')

        else:
            print(form.errors)

    return render(request, 'hashtagtube/add_category.html', {'form': form})

@login_required
def add_video(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        category = None

    if category is None:
        return redirect('/hashtagtube/')

    form = PageForm()

    if request.method == 'POST':
        form = PageForm(request.POST, request.FILES)

        if form.is_valid():
            if category:
                page = form.save(commit=False)
                page.category = category
                page.views = 0
                page.like_react = 0
                page.save()

                return redirect(reverse('hashtagtube:show_category',
                                        kwargs={'category_name_slug':
                                            category_name_slug}))
        else:
            print(form.errors)

    context_dict = {'form': form, 'category': category}
    return render(request, 'hashtagtube/add_video.html', context=context_dict)

@login_required
def restricted(request):
    context_dict={'boldmessage':"Since you're logged in, you can see this text!"}
    return render(request, 'hashtagtube/restricted.html', context=context_dict)


#def user_login(request):
    # If the request is a HTTP POST, try to pull out the relevant information.
   # if request.method == 'POST':
       # username = request.POST.get('username')
       # password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is
       # user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        #if user:
            # Is the account is active? It could have been disabled
           # if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
              #  lgoin(request, user)
               # return redirect(reverse('hashtagtube:index'))
           # else:
                # An inactive account was used - no logging in!
            #    return HttpResponse("Your hashtagtube account is disabled.")
      #  else:
            # Bad login details was provided, so we can't log the user in.
       #     print("Invalid login details: {username}, {password}")
        #    return HttpResponse("Invalid lgoin details supplied.")
    # The request is not a HTTP POST, so display the login form
   # else:
     #   return render(request, 'registration/login.html')


@login_required
#def user_logout(request):
 #   logout(request)

  #  return render(request, ('registration/logout.html'))


#def register(request):
    # A boolean value for telling the template
    # whether the registration was successful.
    # Set to False initially.
    # Code changes value to True when registration succeeds.
 #   registered = False

    # If it's a HTTP POST
  #  if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
   #     user_form = UserForm(request.POST)
    #    profile_form = UserProfileForm(request.POST)

        # If the two forms are valid...
     #   if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form date to the database.
      #      user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
       #     user.set_password(user.password)
        #    user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves.
            # we set commit=False. This delays saving the model
            # until we're ready to avoid integrity problems.
         #   profile = profile_form.save(commit=False)
          #  profile.user = user

            # Did the user provdie a profile picture?
            # If so, we need to get it from the input form and
            # put it in the UserProfile model.
          #  if 'picture' in request.FILES:
           #     profile.picture = request.FILES['picture']

           # profile.save()

           # registered = True
       # else:
            # Invalid form or forms
            # Print problems to the terminal
        #    print(user_form.errors, profile_form.errors)
   # else:
        # Not a HTTP POST, so we render our form using two ModelForm instances.
        # These forms will be blank, ready for user input.
    #    user_form = UserForm()
     #   profile_form = UserProfileForm()
    # render the template depending on the context.
   # return render(request, 'hashtagtube.register.html',
    #              context={'user_form': user_form,
     #                      'profile_form': profile_form,
      #                     'registered': registered})


#functions used for ajax asynchronous operations
@login_required
def like(request):
    #obtain the id of the video page
    video_id = request.GET['page_id']

    #obtain the page object if it exists, else raise an exception
    try:
        page = Page.objects.get(id=int(page_id))
    except Page.DoesNotExist:
        return HttpResponse(-1)
    except ValueError:
        return Httpresponse(-1)

    #update the like count on the page, save and return it
    page.like_react = page.like_react + 1
    page.save()

    return HttpResponse(page.like_react)


@login_required
def dislike(request):
    #obtain the id of the video page
    video_id = request.GET['page_id']

    #obtain the page object if it exists, else raise an exception
    try:
        page = Page.objects.get(id=int(page_id))
    except Page.DoesNotExist:
        return HttpResponse(-1)
    except ValueError:
        return Httpresponse(-1)

    #update the dislike count on the page, save and return it
    page.dislike_react = page.dislike_react + 1
    page.save()

    return HttpResponse(page.dislike_react)


@login_required
def love(request):
    #obtain the id of the video page 
    video_id = request.GET['page_id']

    #obtain the page object if it exists, else raise an exception
    try:
        page = Page.objects.get(id=int(page_id))
    except Page.DoesNotExist:
        return HttpResponse(-1)
    except ValueError:
        return Httpresponse(-1)

    #update the love count on the page, save and return it
    page.love_react = page.love_react + 1
    page.save()

    return HttpResponse(page.love_react)


@login_required
def haha(request):
    #obtain the id of the video page
    video_id = request.GET['page_id']

    #obtain the page object if it exists, else raise an exception
    try:
        page = Page.objects.get(id=int(page_id))
    except Page.DoesNotExist:
        return HttpResponse(-1)
    except ValueError:
        return Httpresponse(-1)

    #update the haha count on the page, save and return it
    page.haha_react = page.haha_react + 1
    page.save()

    return HttpResponse(page.haha_react)



@login_required
def follow_unfollow(request):
    #obtain the user profile and user id's
    #obtain the objects with those id's
    #if those don't exist, raise exception
    try:
        user_id = request.GET['user_id']
        user_page_id = request.GET['user_profile_id']
        user = UserProfile.objects.get(id=int(user_id))
        user_page = UserProfile.objects.get(id=int(user_page_id))
    except User.DoesNotExist:
        return HttpResponse(-1)
    except UserProfile.DoesNotExist:
        return HttpResponse(-1)
    except ValueError:
        return HttpResponse(-1)

    #if doesn't follow the user profile, add profile to user's following acc's
    #if they do follow, unfollow/remove the profile from user's following acc's
    #updates the follow relation between objects
    if 'follow' in request.GET:
        user.follow.add(user_page)
    elif 'unfollow' in request.GET:
        user.follow.remove(user_page)

    #save both user profile objects and return the followers count for the
    #profile that's being displayed
    user.save()
    user_page.save()

    return HttpResponse(user_page.count_followers())


@login_required
def submit_comment(request):
    # get page id, user's id and comment contents
    video_id = request.GET['page_id']
    comment_content = request.GET['input']
    author_id = request.GET['user_id']
# get the video page object, userprofile object
    try:
        video_page = Page.objects.get(id=int(page_id))
        author = UserProfile.objects.get(id=int(author_id))
    except Page.DoesNotExist:
        return HttpResponse(-1)
    except ValueError:
        return Httpresponse(-1)

# create appropriate comment object and return its contents
    comment = Comment.objects.get_or_create(
        author=author, video_page=video_page)[0]
    comment.comment = comment_content
    comment.save()

    return HttpResponse(comment.__str__())
