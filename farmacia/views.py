from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    usuario = request.user
    return render(request, "inicio.html", {"usuario": usuario})