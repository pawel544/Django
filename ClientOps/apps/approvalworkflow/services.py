from django.core.exceptions import ValidationError
from django.utils import timezone
from ClientOps.apps.approvalworkflow.models import Submission
from django.db import transaction

def create_submission( *,user):

        submission = Submission.objects.create(created_by=user)
        return submission
@transaction.atomic
def submit_submission(*,submission,user):
    if submission.created_by != user:
        raise ValidationError("You cannot submit someone else's submission.")
    if submission.status != Submission.Status.DRAFT:
        raise ValidationError("Only draft submissions can be submitted.")
    submission.status = Submission.Status.SUBMITTED
    submission.submission_date = timezone.now()
    submission.save(
            update_fields=['status', 'submission_date'])
    return submission
@transaction.atomic
def first_approve_submission(*, submission, user):
    if submission.status != Submission.Status.SUBMITTED:
        raise ValidationError("Only submitted submissions can be approved.")
    if submission.created_by == user:
        raise ValidationError("You cannot approve your own submission.")
    submission.status = Submission.Status.FIRST_APPROVED
    submission.first_approved_by= user
    submission.first_approved_at = timezone.now()
    submission.save(update_fields=['status', 'first_approved_by' ,'first_approved_at'])
    return submission

@transaction.atomic
def final_approve_submission(*, submission, user):
    if submission.status != Submission.Status.FIRST_APPROVED:
        raise ValidationError("Only first-approved submissions can be finally approved.")
    if submission.created_by == user:
        raise ValidationError("You cannot approve your own submission.")
    submission.status = Submission.Status.APPROVED
    submission.approved_by= user
    submission.approved_at = timezone.now()
    submission.save(update_fields=['status', 'approved_by' ,'approved_at'])
    return submission
@transaction.atomic
def reject_submission(*, submission, user, reason):
    if submission.created_by == user:
        raise ValidationError("The creator cannot reject the agreement.")
    if submission.status not in [Submission.Status.FIRST_APPROVED, Submission.Status.SUBMITTED]:
        raise ValidationError("Only submitted or first-approved submissions can be rejected.")
    if not reason.strip():
        raise ValidationError("Reason for rejection cannot be empty.")
    submission.status = Submission.Status.REJECTED
    submission.rejection_reason = reason.strip()
    submission.rejected_by= user
    submission.rejected_at = timezone.now()
    submission.save(update_fields=['status', 'rejected_by' ,'rejected_at', 'rejection_reason'])
    return submission