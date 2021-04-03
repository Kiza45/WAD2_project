import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                        'wad2_project.settings')

import django
django.setup()
from django.core.files import File
from hashtagtube.models import Category, Page, UserProfile
from django.contrib.auth.models import User
from wad2_project.settings import MEDIA_DIR

def populate():

#list of users to populate the db
    users = ['rrico1997', 'MarcosItalianCuisine', 'outdoorsLover']

#lists of videos divided into categories
    food_videos = [
        {'title': 'Preparing tomatoes Italian way',
         'video':'tomatoes.mp4',
         'thumbnail':'tomatoes_thumbnail.jpg',
         'views': 5,
         'like_react':1,
         'dislike_react':0,
         'haha_react':0,
         'love_react':1 },
         {'title': 'Making original mexican guacamole',
          'video':'mexican.mp4',
          'thumbnail':'mexican_thumbnail.jpg',
          'views':8,
          'like_react':3,
          'dislike_react':1,
          'haha_react':1,
          'love_react':0 },
          {'title': 'Thai Broccoli and Corn Recipe',
           'video':'broccolli.mp4',
           'thumbnail':'broccolli_thumbnail.jpg',
           'views':10,
           'like_react':1,
           'dislike_react':0,
           'haha_react':0,
           'love_react':3 } ]

    sport_videos = [
            {'title': 'Score',
             'video':'basketball.mp4',
             'thumbnail':'basketball_thumbnail.jpg',
             'views':10,
             'like_react':4,
             'dislike_react':1,
             'haha_react':2,
             'love_react':2 },
             {'title': 'Beautiful day for skiing.',
              'video':'skiing.mp4',
              'thumbnail':'skiing_thumbnail.jpg',
              'views':15,
              'like_react':4,
              'dislike_react':1,
              'haha_react':1,
              'love_react':6 },
              {'title': 'Attacked by the wave',
               'video':'surfing.mp4',
               'thumbnail':'surfing_thumbnail.jpg',
               'views':10,
               'like_react':2,
               'dislike_react':2,
               'haha_react':5,
               'love_react':0 } ]

    music_videos = [
            {'title': 'Drumming',
             'video':'drums.mp4',
             'thumbnail':'drums_thumbnail.jpg',
             'views':15,
             'like_react':3,
             'dislike_react':1,
             'haha_react':0,
             'love_react':0 },
             {'title': 'Pre-pandemic club night!',
              'video':'club.mp4',
              'thumbnail':'club_thumbnail.jpg',
              'views':15,
              'like_react':3,
              'dislike_react':0,
              'haha_react':0,
              'love_react':8 } ]


#dictionary of categories with video pages for each
    categories = { 'Food': {'pages': food_videos},
                   'Sport': {'pages': sport_videos},
                   'Music': {'pages': music_videos} }

#variables i use to randomly pick an author for a video at each iteration
    i=1
    n=3

#iterate over dictionaries and create objects
    for cat, cat_data in categories.items():
        c = add_category(cat)
        u = add_user(users[i%n])
        for p in cat_data['pages']:
            add_page(c, p['title'], p['video'], p['thumbnail'], u, p['views'], p['like_react'],
                        p['dislike_react'], p['haha_react'], p['love_react'])
            i=i+1
        n=n+1

#print the results nicely
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'- {c}: {p}, {p.author}')


def add_page(cat, title, video, thumbnail, user, views=0, like=0, dislike=0, haha=0, love=0):
    #create or get the object and assign attributes
    p = Page.objects.get_or_create(category=cat, title=title)[0]

    p.author = user
    p.views = views
    p.like_react = like
    p.dislike_react = dislike
    p.haha_react = haha
    p.love_react = love

    #retrieve the video file from the directory it's stored in
    #convert it to the django file and save as attribute
    path_name = MEDIA_DIR+'/videos/'+video
    f = open(path_name, 'rb')
    django_file = File(f)
    p.video.save(video, django_file, save=True)
    f.close()

#retrieve the thumbnail file from the directory it's stored in
#convert it to the django file and save as attribute

    path_name = MEDIA_DIR+'/thumbnails/'+thumbnail
    f = open(path_name, 'rb')
    django_file = File(f)
    p.thumbnail.save(thumbnail, django_file, save=True)
    f.close()

    p.save()
    return p

def add_category(title):
    c = Category.objects.get_or_create(title=title)[0]
    c.save()
    return c

def add_user(username):
    #create a user object
    user = User.objects.create_user(username=username, password='password')
    user.save()
    #create a UserProfile object related to the user created above
    profile = UserProfile.objects.get_or_create(user=user)[0]
    profile.username=username
    profile.save()
    return profile

if __name__ == '__main__':
    print('Starting Hashtagtube population script...')
    populate()
