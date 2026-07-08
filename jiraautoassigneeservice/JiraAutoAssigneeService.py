from project.logger import logger

from project.manual_updater import update_tasks_in_db, \
    save_assigned_tasks_to_db, \
    save_unassigned_tasks_to_db, check_all_users_are_active
from project.assigner import assign_tasks

import sentry_sdk


sentry_sdk.init("http://b59cd0944b0143ae9bff42fbfb8e7995@100.99.5.41:8000/4")

logger.level('INFO')


check_all_users_are_active()
update_tasks_in_db()
save_assigned_tasks_to_db()
save_unassigned_tasks_to_db()
assign_tasks()
