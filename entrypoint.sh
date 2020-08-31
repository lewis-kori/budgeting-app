#!/bin/bash
sleep 2 #sleep the container for 2 seconds to allow the postgres container to start up and allow connections
python manage.py migrate 
python manage.py migrate_all_schemas  # Apply database migrations to all schemas
python manage.py collectstatic --noinput  # Collect static files

# # Prepare log files
touch /gunicorn/logs/access.log
touch /gunicorn/logs/error.log

# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn budgeting.wsgi:application \
    --bind 0.0.0.0:8099 \
    --workers 3 \
    --log-level=info \
    --access-logfile=/gunicorn/logs/access.log \
    --error-logfile=/gunicorn/logs/error.log \
    --capture-output \
    "$@"
