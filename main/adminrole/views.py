from django.shortcuts import render, redirect, get_object_or_404
from guest.models import *
from studentrole.models import *
from registration.models import *
from .models import *
from .forms import *
from django.core.mail import send_mail
from django.utils import timezone
from datetime import datetime
from django.contrib import messages

def maintenance(request):
    # Retrieve all maintenance requests from the database
    all_requests = MaintenanceRequest.objects.all()

    # Separate requests into fulfilled and not fulfilled
    fulfilled_requests = all_requests.filter(fulfilled=True)
    not_fulfilled_requests = all_requests.filter(fulfilled=False)

    context = {
        'fulfilled_requests': fulfilled_requests,
        'pending_requests': not_fulfilled_requests,
    }

    return render(request, 'maintenance.html', context)

def send_confirmation_email(email, name, number, CheckIn, CheckOut, capacity):
    subject = 'Guest Booking Approved'
    message = f'Your guest room booking request at COEP hostel has been approved!\n\n\
    Booking Details:\n\
        Guest Name: {name}\n\
        Room No: {number}\n\
        Dates: {CheckIn} to {CheckOut}\n\
        No of Guests: {capacity}'
    from_email = 'djangoproject24@gmail.com'
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)

def guest_booking(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        booking_id = request.POST.get('booking_id')

        if action == 'approve':
            booking = get_object_or_404(Booking, id=booking_id)
            booking.approved = True
            send_confirmation_email(booking.guest_email, booking.guest_name, booking.room.room_number, booking.check_in_date, booking.check_out_date, booking.room.capacity)
            booking.save()
        elif action == 'reject':
            booking = get_object_or_404(Booking, id=booking_id)
            booking.delete()

        return redirect('guest_booking')

    booking_requests = Booking.objects.filter(approved=False)
    return render(request, 'guest_booking.html', {'booking_requests': booking_requests})

from django.contrib import messages

def checkinout(request):
    error_messages = []

    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'checkout':
            form = CheckOutForm(request.POST)
            if form.is_valid():
                mis = form.cleaned_data['mis']
                year = form.cleaned_data['year']
                year_model = None
                if year == 'FirstYear':
                    year_model = FirstYear
                elif year == 'SecondYear':
                    year_model = SecondYear
                elif year == 'ThirdYear':
                    year_model = ThirdYear
                else:
                    year_model = FinalYear

                student = year_model.objects.filter(application_id=mis, selected=True)
                if student.exists():
                    if CheckInOut.objects.filter(mis=mis, check_in_time=None).exists():
                        error_messages.append('This user is already checked out and has not checked in yet.')
                    else:
                        checkout = form.save(commit=False)
                        checkout.check_out_time = timezone.localtime(timezone.now())
                        checkout.save()
                        error_messages.append('User checked out successfully')
                else:
                    error_messages.append('No student found with the provided details.')

        elif action == 'checkin':
            form = CheckInForm(request.POST)
            if form.is_valid():
                mis = form.cleaned_data['mis']
                try:
                    student = CheckInOut.objects.get(mis=mis, check_in_time=None)
                    student.check_in_time = timezone.localtime(timezone.now())
                    student.save()
                    error_messages.append('User checked in successfully')
                except CheckInOut.DoesNotExist:
                    error_messages.append('This user is not checked out. Please check out first before checking in.')

    entries = CheckInOut.objects.all()
    checkinform = CheckInForm()
    checkoutform = CheckOutForm()
    return render(request, 'checkinout.html', {
        'checkinform': checkinform,
        'checkoutform': checkoutform,
        'entries': entries,
        'error_messages': error_messages
    })

def admin_home(request):
    bookings = Booking.objects.all()
    dates_list = []
    current_year = datetime.now().year
    current_month = datetime.now().month
    monthly_data = [[0]*12 for i in range(2)]
    for booking in bookings:
        if booking.check_in_date.year == current_year:
            monthly_data[0][booking.check_in_date.month - 1] += 1
            monthly_data[1][booking.check_in_date.month - 1] += float(booking.charges)/1000
        dates_list.append([booking.check_in_date, booking.check_out_date, booking.room_id])
    total_rooms = GuestRoom.objects.count()
    dates_list.sort(key=lambda x: x[0])
    context = {
            'available_rooms':total_rooms,
            'not_available':0,
            'current_month': monthly_data[1][current_month-1],
            'monthly_occupancy': monthly_data[0],
            'monthly_revenue': monthly_data[1]
    }

    if request.method == 'POST':
        specific_date = request.POST.get('specificdate')
        specific_date = datetime.strptime(specific_date, '%Y-%m-%d').date()
        available_rooms = total_rooms

        for check_in_date, check_out_date, room_id in dates_list:
            if check_in_date <= specific_date:
                if check_out_date >= specific_date:
                    available_rooms -= 1
            else:
                break
        
        context = {
            'available_rooms':available_rooms,
            'not_available':total_rooms - available_rooms,
            'current_month': monthly_data[1][current_month-1]*1000,
            'monthly_occupancy': monthly_data[0],
            'monthly_revenue': monthly_data[1]
        }

    return render(request, 'adminhome.html', context)