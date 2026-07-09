from django.db import models


class QueueTicket(models.Model):
    name = models.CharField(max_length=100)
    ticket_number = models.IntegerField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    STATUS_CHOICES = (
        ('waiting', 'Waiting'),
        ('serving', 'Serving'),
        ('done', 'Done'),
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='waiting'
    )

    def __str__(self):
        return f"A-{self.ticket_number}"