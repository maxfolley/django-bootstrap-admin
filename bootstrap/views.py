import mimetypes, os
from django.conf import settings
from django.db.models import get_model
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt, csrf_protect

def download_file(request, file_path):
    full_path = os.path.join(settings.DOWNLOADS_ROOT, file_path)
    file = open(full_path, 'r')
    mimetype = mimetypes.guess_type(full_path)[0]
    if not mimetype: mimetype = "application/octet-stream"

    response = HttpResponse(file.read(), mimetype=mimetype)
    response["Content-Disposition"]= "attachment; filename=%s" % os.path.split(full_path)[1]
    return response


def update_order(request, model):
    indices = request.POST['indices'].split(',')
    model = get_model("website", model)
    records = model.objects.filter(pk__in=indices) 
    for record in records:
        pos = indices.index(str(record.id))
        record.order = pos
        record.save()
    return HttpResponse()

