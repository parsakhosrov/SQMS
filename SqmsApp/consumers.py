from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
import json


class QueueConsumer(AsyncWebsocketConsumer):

    async def connect(self):

        self.ticket_number = self.scope["url_route"]["kwargs"].get("ticket_number")

        # اگر ticket_number هست → user mode
        if self.ticket_number:
            self.group_name = f"user_{self.ticket_number}"
        else:
            # home page → global mode
            self.group_name = "queue_global"

        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        await self.accept()


        # initial data
        data = await self.get_data()
        await self.send(text_data=json.dumps(data))

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def queue_update(self, event):
        print("QUEUE UPDATE:", event)

        await self.send(
            text_data=json.dumps(event["data"])
        )

    @sync_to_async
    def get_data(self):

        from .models import QueueTicket

        waiting_qs = QueueTicket.objects.filter(status="waiting")
        waiting_count = waiting_qs.count()

        # 🔥 HOME MODE
        if not self.ticket_number:
            return {
                "type": "global",
                "waiting": waiting_count
            }

        # 🔥 USER MODE
        my_ticket = int(self.ticket_number)

        people_ahead = waiting_qs.filter(
            ticket_number__lt=my_ticket
        ).count()

        avg_time = 5

        return {
            "type": "user",
            "waiting": waiting_count,
            "people_ahead": people_ahead,
            "estimated_time": waiting_count * avg_time
        }