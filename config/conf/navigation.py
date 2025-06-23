from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

PAGES = [
    {
        "seperator": False,
        "items": [
            {
                "title": _("Home page"),
                "icon": "home",
                "link": reverse_lazy("admin:index"),
            }
        ],
    },
    {
        "title": _("Auth"),
        "separator": True,  # Top border
        "items": [
            {
                "title": _("Users"),
                "icon": "group",
                "link": reverse_lazy("admin:accounts_user_changelist"),
            },
        ],
    },
    {
        "title": _("Mahsulot va Kategoryalar"),
        "separator": True,  
        "items": [
            {
                "title": _("Banner"),
                "icon": "group",
                "link": reverse_lazy("admin:api_bannermodel_changelist"),
            },
            # {
            #     "title": _("Banner"),
            #     "icon": "group",
            #     "link": reverse_lazy("admin:api_bannermodel_changelist"),
            # },
            # {
            #     "title": _("Banner"),
            #     "icon": "group",
            #     "link": reverse_lazy("admin:api_bannermodel_changelist"),
            # },
        ],
    },
]
