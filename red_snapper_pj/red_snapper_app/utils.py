# from red_snapper_app import models
from red_snapper_pj.red_snapper_app import models
from django.db import models


def is_correct_password(requested_username, requested_password):
    if requested_username == models.User.username and requested_password == models.User.password:
        return True
    return False




