from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Home, Announcements
from .forms import *
import os

# Calculate django application execute directory path.
PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))


# This function will return and render the home page when url is http://localhost:8000/tausite/.

def home(request):
    # Get the index template file absolute path.
    index_file_path = PROJECT_PATH + '/templates/home.html'
    homes = Home.objects.all()
    context = {'home': homes}

    # Return the index file to client.
    return render(request, index_file_path, context)


def email_list(request):
    # Get the index template file absolute path.
    index_file_path = PROJECT_PATH + '/templates/interviews.html'
    emails = Email.objects.all()
    context = {'email': emails}

    # Return the index file to client.
    return render(request, index_file_path, context)


# This function will display Annoucement in a list page
# the request url is http://localhost:8000/tausite/list_all
def announcement_list(request):
    # Get all announcement model object order by date column.
    announcements = Announcements.objects.order_by('date')

    # Add the annoucement list in Django context.
    context = {'Announcements': announcements}

    # Get the list page absolute path.
    announcement_file_path = PROJECT_PATH + '/templates/Announcement List.html'

    # Render and return to the list page.
    return render(request, announcement_file_path, context)


# Display the Announcements detail information in web page. The input parameter is announcement id.
# The request url is http://localhost:8000/tausite/show_detail/3/.
def announcement_detail(request, id):
    # Get annoucements by id
    announcement = Announcements.objects.get(id=id)

    # Set the announcements object in context.
    context = {'Announcement': announcement}

    # Get announcement detail page absolute file path.
    announcements_file_path = PROJECT_PATH + '/templates/Announcement Details.html'

    # Return the announcements detail page.
    return render(request, announcements_file_path, context)


def picture_image_view(request):
    image_file_path = PROJECT_PATH + '/templates/image_upload.html'
    success_file_path = PROJECT_PATH + '/templates/success.html'
    if request.method == 'POST':
        form = PictureForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('/tausite/success')
    else:
        form = PictureForm()
    return render(request, image_file_path, {'form': form})


def success(request):
    return HttpResponse('successfuly uploaded')


def display_picture_images(request):
    if request.method == 'GET':
        showPictureSite = PROJECT_PATH + '/templates/display_picture_images.html'
        # getting all the objects of hotel.
        pictures = Picture.objects.all()
        return render(request, showPictureSite,
                      {'picture_images': pictures})
