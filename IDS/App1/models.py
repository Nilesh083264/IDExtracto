from django.db import models

class IdentityInfo(models.Model):
    name = models.CharField(max_length=100,null=True)
    id_type = models.CharField(max_length=50,null=True)
    id_number = models.CharField(max_length=50,null=True)
    address = models.TextField(blank=True, null=True)
    mobile = models.CharField(max_length=15, blank=True, null=True)
    pincode = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.id_type}"
