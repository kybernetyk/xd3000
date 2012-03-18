# Create your views here.

from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
import datetime
import md5
from django.core.servers.basehttp import FileWrapper
from django.views.decorators.csrf import csrf_exempt


import os

from img.models import Image

@csrf_exempt
def index(request):
    if request.method == "POST":
        data = request.FILES['infile'] # or self.files['image'] in your form
        file = ContentFile(data.read())
        path = default_storage.save(data.name, file)
        tmp_file = os.path.join(settings.MEDIA_ROOT, path)

        #create entry in database
        img = Image()
        img.filename = tmp_file
        urlname = md5.new(img.filename + str(datetime.datetime.now())).hexdigest() #replace this
        img.urlname = urlname
        img.pub_date = datetime.datetime.now()
        img.content_type = data.content_type
        img.pub_ip = str(request.META['REMOTE_ADDR'])
        img.save()
        return render_to_response('success.html',{'img' : img})
        #return HttpResponseRedirect(img.urlname)
    else:
        return render_to_response('index.html', {},context_instance=RequestContext(request))

def show(request, img_name):
    #img = Image.
    img_name = img_name.rstrip('/').strip('/')
    #img = get_list_or_404(Image, urlname=img_name)
    img = get_object_or_404(Image, urlname=img_name)
    f = file(img.filename)
    sze = f.tell()
    resp = HttpResponse(FileWrapper(f), content_type=img.content_type)
    #resp['Content-Length'] = sze
    return resp
    #return HttpResponse("Text only, please: " + str(img), content_type="text/plain")
