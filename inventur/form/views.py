from django.shortcuts import render, HttpResponse, redirect
from .models import Hardware
from django.contrib import messages
import csv

# Create your views here.

def user_form(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        mini_pc = request.POST.get('mini_pc') == 'on'
        laptop = request.POST.get('laptop') == 'on'
        drucker = request.POST.get('drucker') == 'on'
        monitore = request.POST.get('monitore') == 'on'
        monitor_count = request.POST.get('monitor_count')
        monitor_count = int(monitor_count) if monitor_count else 0

        hardware = Hardware(
            first_name=first_name,
            last_name=last_name,
            mini_pc=mini_pc,
            laptop=laptop,
            drucker=drucker,
            monitore=monitore,
            monitor_count=monitor_count,
        )
        hardware.save()
        messages.add_message(request, messages.INFO, "Hello world.")
        return redirect('success')
        
    return render(request, "user_form.html")

def success(request):
    return render(request, 'success.html')

def start(request):
    return render(request, 'start.html')

def redirect_start(request):
    return redirect('start')


def output_data(request):
    employees = Hardware.objects.all()
    return render(request, 'output_data.html', {'employees': employees})

def download_excel(request):
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="employee_data.csv"'},
    )

    writer = csv.writer(response)
    writer.writerow(['ID', 'Vorname', 'Nachname', 'Mini-PC', 'Laptop', 'Drucker', 'Monitore', 'Anzahl Monitore'])

    employees = Hardware.objects.all().values_list('id', 'first_name', 'last_name', 'mini_pc', 'laptop', 'drucker', 'monitore', 'monitor_count')
    for employee in employees:
        writer.writerow(employee)

    return response
