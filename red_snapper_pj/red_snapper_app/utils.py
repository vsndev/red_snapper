# from red_snapper_app import models
from red_snapper_app import models


def is_correct_password(requested_username, requested_password):
    requested_user = models.User.objects.get_or_none(username=requested_username)
    if requested_user and requested_user.password == requested_password:
        return True
    return False



