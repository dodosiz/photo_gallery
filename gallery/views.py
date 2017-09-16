from django.shortcuts import render, get_object_or_404
from .models import Photo, Topic


# put the column number here
topic_column_number = 3
image_column_number = 5


def index(request):
    topics = Topic.objects.all()
    list_of_topics = []
    j = 0
    entry = []
    for t in topics:
        j += 1
        entry.append(t)
        if (j % topic_column_number) == 0:
            list_of_topics.append(entry)
            entry = []
            j = 0
    list_of_topics.append(entry)
    return render(request, 'gallery/index.html', {'topics': topics, 'list_of_topics': list_of_topics})


def topic(request, topic_name):
    topic = Topic.objects.get(name=topic_name)
    images = Topic.objects.get(name=topic_name).photo_set.all()
    list_of_images = []
    j = 0
    entry = []
    for i in images:
        j += 1
        entry.append(i)
        if (j % image_column_number) == 0:
            list_of_images.append(entry)
            entry = []
            j = 0
    list_of_images.append(entry)
    return render(request, 'gallery/topic.html', {'topic': topic, 'images': images, 'list_of_images': list_of_images})


def detail(request, topic_name, photo_id):
    photo = get_object_or_404(Photo, topic__name=topic_name, id=photo_id)
    return render(request, 'gallery/detail.html', {'photo': photo})
