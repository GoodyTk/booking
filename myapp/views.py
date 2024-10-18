from django.shortcuts import render, redirect # type: ignore
from .models import Room, Booking
from django.http import HttpResponse

# Create your views here.
def room_list(request):
    rooms = Room.objects.all()
    context = {
        "rooms": rooms,
    }

    return render(request, "booking/room_list.html", context)

def booking_room(request):
    if request.method == "POST":
        start_time = request.POST.get("start-time")
        end_time = request.POST.get("end-time")
        room_number = request.POST.get("room-number")
        
        try:
            room = Room.objects.get(number=room_number)
        except Room.DoesNotExist: 
            return HttpResponse("room no exists", status=404)

        booking = Booking.objects.create(
            user = request.user,
            room = room,
            start_time = start_time,
            end_time = end_time
        )

        return redirect("booking-details", pk=booking.id)
    
    else:
        return render(request, "booking/booking_form.html")
    
def booking_details(request, pk):
    booking = Booking.objects.get(id=pk)

    context = {
        "booking": booking
    }
    return render(request, "booking/booking_details.html", context)

def home_page(request):
    return render(request, "index.html")