from functools import wraps
from flask import abort
from flask_login import current_user
from .models import Permission


def permission_required(permission):
    def decorator(f):
        @wraps(f)
        def decorated_functiion
    return decorator


def admin_required(f):
    return permission_required(Permission.ADMIN)(f)
