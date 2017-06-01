from django.http import JsonResponse

from .models import Planilla


def planilla_delete(request):
    pkp = request.POST.get('identificadorP_id')
    identificador = Planilla.objects.get(id=pkp)
    response = {'delete': True, 'class': 'hide'}

    if identificador.id > 0:
        identificador.delete()

    return JsonResponse(response)