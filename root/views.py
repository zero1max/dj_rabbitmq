import logging
from root.forms import FeedbackForm
from django.shortcuts import render, redirect
from django.contrib import messages
from root.tasks import send_feedback_email_task

logger = logging.getLogger(__name__)


def feedback_form_view(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]
            print(email)
            print(message)
            subject = "Yangi fikr-mulohaza"  # noqa

            send_feedback_email_task.delay(email, subject, message) # type: ignore

            messages.success(request, "Fikr-mulohazangiz yuborildi, rahmat!")  # noqa
            return redirect("success")  # bu URL'ni `urls.py` da belgilang # noqa
    else:
        form = FeedbackForm()

    return render(request, "feedback.html", {"form": form})


def success_view(request):
    return render(request, "success.html")