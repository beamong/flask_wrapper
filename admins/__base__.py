# coding: utf-8

"""
"""

from __future__ import unicode_literals, print_function

import flask_login
from flask_admin.contrib import sqla


class MyModelView(sqla.ModelView):
    def is_accessible(self):
        return True
        return flask_login.current_user.is_authenticated