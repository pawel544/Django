from django.db import models
from ..accounts.models import User
# Create your models here.

class Submission(models.Model):
    class Status(models.TextChoices):
        DRAFT="draft","Draft"
        SUBMITTED= "submitted" ,"Submitted"
        FIRST_APPROVED="first approved" ,"First Approved"
        APPROVED="approved","Approved"
        REJECTED="rejected","Rejected"

    status = models.CharField(choices=Status.choices,default=Status.DRAFT ,max_length=30)
    rejection_reason = models.TextField(blank = True)
    submission_date = models.DateTimeField( null=True, blank=True)
    first_approved_at = models.DateTimeField(null=True, blank=True)
    approved_at = models.DateTimeField(null= True, auto_now_add= True)
    rejected_at = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(User ,on_delete=models.PROTECT, related_name='submission')
    first_approved_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='first_approved_submissions')
    approved_by = models.ForeignKey(User ,on_delete=models.PROTECT, related_name='approved_submissions')
    rejected_by = models.ForeignKey(User ,on_delete=models.PROTECT, null= True, blank= True,
                                    related_name='rejected_submissions')

class ApprovalAction(models.Model):
    class Action(models.TextChoices):
        DRAFT = "draft", "Draft"
        SUBMITTED = "submitted", "Submitted"
        FIRST_APPROVED = "first approved", "First Approved"
        APPROVED = "approved", "Approved"
        REJECTED = "rejected", "Rejected"

    submission = models.ForeignKey(Submission ,on_delete=models.PROTECT, related_name='action')
    action = models.CharField(choices=Action.choices,default=Action.DRAFT ,max_length=30)
    performer_by = models.ForeignKey(User ,on_delete=models.PROTECT)
    resons = models.TextField(blank = True)
    created_by = models.DateTimeField(auto_now_add= True)