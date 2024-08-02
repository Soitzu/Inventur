from django.shortcuts import render, HttpResponse, redirect
from .models import Hardware
from django.contrib import messages
import csv

# Create your views here.

def user_form(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        st_number = request.POST.get('st_number')
        mini_pc = request.POST.get('mini_pc') = 'on'
        laptop = request.POST.get('laptop') = 'on'
        drucker = request.POST.get('drucker') = 'on'
        monitore = request.POST.get('monitore') = 'on'
        monitor_count = request.POST.get('monitor_count')
        monitor_count = int(monitor_count) if monitor_count else 0
        sonstige_hardware = request.POST.get('sonstige_hardware') == 'on'
        sonstige_hardware_details = request.POST.get('sonstige_hardware_details')

        Hardware.objects.create(
        first_name=first_name,
        last_name=last_name,
        st_number=st_number,
        mini_pc=mini_pc,
        laptop=laptop,
        drucker=drucker,
        monitore=monitore,
        monitor_count=monitor_count,
        sonstige_hardware_details=sonstige_hardware_details,
        )
        return redirect('user_form')
        
    return render(request, "user_form.html")

def output_data(request):
    employees = Hardware.objects.all()
    return render(request, 'output_data.html', {'employees': employees})

def download_excel(request):
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="employee_data.csv"'},
    )

    writer = csv.writer(response)
    writer.writerow(['ID', 'Vorname', 'Nachname', 'ST-Nummer', 'Mini-PC', 'Laptop', 'Drucker', 'Monitore', 'Anzahl Monitore', 'Sonstige Hardware', 'Details zur sonstigen Hardware'])

    employees = Hardware.objects.all().values_list('id', 'first_name', 'last_name', 'st_number', 'mini_pc', 'laptop', 'drucker', 'monitore', 'monitor_count', 'sonstige_hardware_details')
    for employee in employees:
        writer.writerow(employee)

    return response
