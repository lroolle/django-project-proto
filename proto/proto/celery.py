import os
from datetime import timedelta
from celery import Celery
from django.conf import settings


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jclife.settings")

app = Celery("jclife")


class CeleryConfig(object):
    broker_url = settings.CELERY_BROKER_URL  # "redis://127.0.0.1:6379/8"
    result_backend = settings.CELERY_RESULT_BACKEND  # "redis://127.0.0.1:6379/7"
    timezone = "Asia/Shanghai"

    task_routes = {
        "auth.tasks.*": {"queue": "auth"},
        "wechat.tasks.*": {"queue": "wechat"},
    }

    beat_schedule = {}
    if settings.IS_PRODUCTION:
        beat_schedule.update(
            {
                "update_wechat_access_token_task": {
                    "task": "wechat.tasks.update_access_token_task",
                    "schedule": timedelta(seconds=(2 * 60 * 60) - 30),
                }
            }
        )


app.config_from_object(CeleryConfig)
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS + ["jclife"])
