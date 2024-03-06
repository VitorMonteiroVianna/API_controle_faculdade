from django.http import JsonResponse

def alunos(request):
    if request.method == 'GET':
        aluno = {'id': '123', 'nome': 'Clebin'}
        return JsonResponse(aluno)