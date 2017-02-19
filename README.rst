Installation
============

1. Install ffmpeg
2. Install mediainfo
3. Install celery
4. Install django-videokit 'pip install django-videokit'
5. Add 'videokit' to your INSTALLED_APPS

Usage Overview
==============
Settings
--------
Define MEDIA_ROOT and MEDIA_URL, example:

.. code-block:: python

    MEDIA_ROOT = os.path.join(BASE_DIR, 'media-uploads')
    MEDIA_URL = '/media/'

VideoField
----------
VideoField is a class very similar in nature to Django's out of the box ImageField. It allows you to upload a video file, retrieve video file properties, and generate thumbnails.

Using VideoField In Your Model
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    from django.db import models

    from videokit.models import VideoField

    class MediaItem(models.Model):
        video = VideoField( upload_to = upload_to, null = True, blank = True, 
                            width_field = 'video_width', height_field = 'video_height',
                            rotation_field = 'video_rotation',
                            mimetype_field = 'video_mimetype',
                            duration_field = 'video_duration',
                            thumbnail_field = 'video_thumbnail')
        video_width = models.IntegerField(null = True, blank = True)
        video_height = models.IntegerField(null = True, blank = True)
        video_rotation = models.FloatField(null = True, blank = True)
        video_mimetype = models.CharField(max_length = 32, null = True, blank = True)
        video_duration = models.IntegerField(null = True, blank = True)
        video_thumbnail = models.ImageField(null = True, blank = True)

Defined fields such as width_field, and height_field are optional but recommended. Using these fields ensures that the video properties are stored in the database rather than computed from the file.

VideoSpecField
--------------
VideoSpecField is a class that leverages ffmpeg to convert videos to other formats. Currently there is support for mp4, ogg and webm files.

Using VideoSpecField In Your Model
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    from django.db import models

    from videokit.models import VideoField

    class MediaItem(models.Model):
        video = VideoField( upload_to = upload_to, null = True, blank = True, 
                            width_field = 'video_width', height_field = 'video_height',
                            rotation_field = 'video_rotation',
                            mimetype_field = 'video_mimetype',
                            duration_field = 'video_duration',
                            thumbnail_field = 'video_thumbnail')
        video_width = models.IntegerField(null = True, blank = True)
        video_height = models.IntegerField(null = True, blank = True)
        video_rotation = models.FloatField(null = True, blank = True)
        video_mimetype = models.CharField(max_length = 32, null = True, blank = True)
        video_duration = models.IntegerField(null = True, blank = True)
        video_thumbnail = models.ImageField(null = True, blank = True)

        video_mp4 = VideoSpecField(source = 'video', format = 'mp4')
        video_ogg = VideoSpecField(source = 'video', format = 'ogg')
        video_webm = VideoSpecField(source = 'video', format = 'webm')

Generation of files is performed by a celery task when the file is accessed for the first time. You can check the status of the file by calling the generated method on VideoSpecField.
