web: gunicorn freecodecamp.wsgi
ws: gunicorn freecodecamp.asgi:application -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8000