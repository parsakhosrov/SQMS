from django.shortcuts import render
from .models import QueueTicket


# =========================
# HOME PAGE (GLOBAL VIEW)
# =========================

def home(request):

    if request.method == "POST":

        name = request.POST.get("name")

        last_ticket = QueueTicket.objects.order_by('-ticket_number').first()

        next_number = 101
        if last_ticket:
            next_number = last_ticket.ticket_number + 1

        ticket = QueueTicket.objects.create(
            name=name,
            ticket_number=next_number,
            status="waiting"
        )


        return render(
            request,
            "SqmsApp/ticket.html",
            {"ticket": ticket}
        )

    waiting_count = QueueTicket.objects.filter(status="waiting").count()

    return render(
        request,
        "SqmsApp/home.html",
        {"waiting_count": waiting_count}
    )


# =========================
# OPERATOR PANEL
# =========================

def operator_panel(request):

    next_ticket = QueueTicket.objects.filter(
        status="waiting"
    ).order_by("created_at").first()

    if request.method == "POST":

        if next_ticket:

            next_ticket.status = "serving"
            next_ticket.save()


    waiting_count = QueueTicket.objects.filter(status="waiting").count()

    return render(
        request,
        "SqmsApp/operator.html",
        {
            "next_ticket": next_ticket,
            "waiting_count": waiting_count
        }
    )


