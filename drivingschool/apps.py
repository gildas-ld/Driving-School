# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.apps import AppConfig
from django.core.signals import request_finished


class DrivingSchoolConfig(AppConfig):
    name = "drivingschool"

    def ready(self):
        # Implicitly connect signal handlers decorated with @receiver.
        # Explicitly connect signal handlers.
        from .signals import update_stock

        request_finished.connect(update_stock, sender=self)
