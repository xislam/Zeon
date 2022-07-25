from django.contrib import admin

from partner_site.models import ContactUs
from partner_site.models import Direction
from partner_site.models import PartnerAnswer
from partner_site.models import PartnerCV
from partner_site.models import QuestionCV
from partner_site.models import SocialNetwork
from partner_site.models import Status


@admin.register(SocialNetwork)
class SocialNetworkInlineModel(admin.ModelAdmin):
    fields = ["name"]


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    fields = [
        "name",
        "email",
        "social_network",
        "social_network_text",
        "phone_number",
        "status",
    ]
    list_display = [
        "name",
        "email",
        "social_network",
        "social_network_text",
        "phone_number",
        "status",
    ]
    list_filter = ["status"]


@admin.register(QuestionCV, PartnerAnswer, Direction, Status)
class PersonAdmin(admin.ModelAdmin):
    pass


@admin.register(PartnerCV)
class SocialNetworkInlineModel(admin.ModelAdmin):
    fields = [
        "full_name",
        "email",
        "direction",
        "question",
        "answer",
        "countries",
        "file_cv",
        "status",
    ]
    list_display = [
        "full_name",
        "email",
        "direction",
        "question",
        "answer",
        "countries",
        "file_cv",
        "status",
    ]
    list_filter = ["status"]
