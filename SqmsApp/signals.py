from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import QueueTicket
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


@receiver(post_save, sender=QueueTicket)
def queue_ticket_updated(sender, instance, **kwargs):
    #from .models import QueueTicket
    #from channels.layers import get_channel_layer
    #from asgiref.sync import async_to_sync

    channel_layer = get_channel_layer()

    waiting_qs = QueueTicket.objects.filter(status="waiting")
    waiting_count = waiting_qs.count()

    # 🔥 GLOBAL UPDATE
    async_to_sync(channel_layer.group_send)(
        "queue_global",
        {
            "type": "queue_update",
            "data": {
                "type": "global",
                "waiting": waiting_count
            }
        }
    )

    # 🔥 USER UPDATE (FIX اصلی اینجاست)
    avg_time = 5

    all_waiting_tickets = list(waiting_qs)

    for ticket in all_waiting_tickets:
        people_ahead = waiting_qs.filter(
            ticket_number__lt=ticket.ticket_number
        ).count()

        async_to_sync(channel_layer.group_send)(
            f"user_{ticket.ticket_number}",
            {
                "type": "queue_update",
                "data": {
                    "type": "user",
                    "people_ahead": people_ahead,
                    "estimated_time": waiting_count * avg_time
                }
            }
        )