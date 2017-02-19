from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from media.forms import MediaItemCreateForm
from media.models import MediaItem

def list(request):
    template = 'media/list.html'

    media_items = MediaItem.objects.all()

    context = {
        'media_items' : media_items,
    }

    return render(request, template, context)

def item_create(request):
    template = 'media/item_create.html'

    item_create_form = MediaItemCreateForm()

    if request.method == 'POST':
        item_create_form = MediaItemCreateForm(request.POST, request.FILES)

        if item_create_form.is_valid():
            video = request.FILES.get('video', None)

            if video:
                media_item = MediaItem(video = video)
                media_item.save()

                media_item.video_mp4.generate()
                media_item.video_ogg.generate()

                return HttpResponseRedirect(reverse('list'))

    context = {
        'item_create_form' : item_create_form,
    }

    return render(request, template, context)
