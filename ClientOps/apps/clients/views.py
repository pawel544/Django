from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from ClientOps.apps.clients.forms import ClientForm
from models import Client, ServiceType
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Q
from django.utils.dateparse import parse_date
from django.utils import timezone
from ..accounts.models import User
from ..accounts.views import is_admin
# Create your views here.

@login_required
def client_list(request):
    if request.method == 'GET':
        client = Client.objects.all( )
        return render(request, "client_list.html", {'clients': client})

@login_required
def client_create(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save()
            return redirect( "client_list", )
    else:
        form = ClientForm()

    return render(request, "client_create.html", {'form': form})

@login_required
def client_edit(request, code):
    client = get_object_or_404(Client , code= code)
    if client.manager != request.user and not is_admin(request.user):
        messages.error(request, "You cannot edit this client")
        return redirect("client_list")

    if  request.method == "POST" :
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect("client_list")
    else:
        form = ClientForm(instance=client)
    return render(request, "client_edit.html", {'form': form})

@user_passes_test(is_admin)
def assignment_employee(request,email, code):
    client = get_object_or_404(Client, code =code)
    employee = get_object_or_404(User, email=email)
    if request.method == "POST":
        client.manager = employee
        client.save(update_fields=['manager'])
        messages.success(request, "Employee assigned successfully.")
        return redirect("client_list")
    return render(request, "assignment_employee.html", {'client': client,
                                                                'employee': employee})
@login_required
def removal_client(request, code):
    client = get_object_or_404(Client, code= code)
    if request.method == "POST":
        client.deleted_at= timezone.now()
        client.save(update_fields=['deleted_at'])
        messages.success(request, "Client removed successfully.")
        return redirect("client_list")
    return render(request, "removal_client.html", {'client': client})


@login_required
def filter_client(request):
    code_from = request.GET.get('code_from')
    code_to = request.GET.get('code_to')
    tax_number_from = request.GET.get('tax_number_from')
    tax_number_to = request.GET.get('tax_number_to')
    manager = request.GET.get('manager')
    status_deleted = request.GET.get('status_deleted')
    status= request.GET.get('status')

    if status_deleted:
        clients = Client.objects.filter(deleted_at__isnull=False)
    else:
        clients = Client.objects.filter(deleted_at__isnull=True)
    if code_from :
        clients =clients.filter(code__gte=code_from,)
    if  code_to:
        clients =clients.filter(code__lte=code_to)
    if tax_number_from :
        clients = clients.filter(tax_number__gte=tax_number_from)
    if tax_number_to:
        clients = clients.filter(tax_number__lte=tax_number_to)
    if manager:
        clients = clients.filter(manager__email=manager)
    if status:
        clients = clients.filter(status=status)
    return render(request, "client_list.html", {'clients': clients})

@login_required
def search_client(request):
    search = request.GET.get('search')
    status_deleted = request.GET.get('status_deleted')
    if status_deleted:
        clients = Client.objects.filter(deleted_at__isnull=False)
    else:
        clients = Client.objects.filter(deleted_at__isnull=True)
    if search:
        query = (Q(code__icontains=search) |
                                Q(name_ar__icontains=search) |
                                Q(name_en__icontains=search) |
                                Q(tax_number__icontains=search) |
                                Q(status__icontains=search) |
                                Q(manager__email__icontains=search)|
                                Q(manager__first_name__icontains=search) |
                                Q(manager__last_name__icontains=search)
                                )

        data_search =parse_date(search)
        if data_search:
            query |= (Q(updated_at__date=data_search)|
                      Q(deleted_at__date=data_search)|
                      Q(created_at__date=data_search))

        clients = clients.filter(query)


    return render(request, "client_list.html", {'clients': clients})

@login_required
def services(request):

    services = ServiceType.objects.all()
    return render(request, "services.html", {'service': services})