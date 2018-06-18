
from apps.api_root.views import api_root

from django.conf.urls import url, include


# ApiRoot
urlpatterns = [
    url(r"^$", api_root, name="api_root"),
]