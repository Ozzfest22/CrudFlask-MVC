import functools
from flask import redirect, url_for, session

def login_required(func):
    @functools.wraps(func)
    def secure_function(*args, **kwargs):
        if "Email" and "IdUsuario" not in session:
            return redirect(url_for("login"))
        return func(*args, **kwargs)

    return secure_function