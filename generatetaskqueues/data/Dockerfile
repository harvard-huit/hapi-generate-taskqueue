# Base celery-worker image for a generated task queue.
# Base: python:3.13-alpine (musl) — clean vulnerability scan (0 CVEs) and small footprint.
# celery + pymongo ship musllinux wheels, so no compiler/apk build layer is needed by default.
# If your queue adds a dependency that must COMPILE a C extension (no musllinux wheel), add a
# throwaway build layer, e.g.:
#   RUN apk add --no-cache --virtual .build-deps build-base libffi-dev \
#     && pip install -r /app/requirements.txt \
#     && apk del .build-deps
FROM python:3.13-alpine

ENV LANG=C.UTF-8 \
    LC_ALL=C.UTF-8 \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    VENV_PATH=/app/venv \
    PATH=/app/venv/bin:$PATH

WORKDIR /app

# Unprivileged runtime user (busybox adduser/addgroup syntax).
RUN addgroup -S celery && adduser -S -G celery -h /app celery

# Celery runtime config + entrypoint (celeryconfig.py must sit next to the worker's CWD so
# `import celeryconfig` resolves).
COPY deploy/celeryconfig.py deploy/startCeleryWorker deploy/requirements.txt /app/

# Install dependencies, then the queue package itself.
RUN python -m venv "$VENV_PATH" \
    && pip install --upgrade pip \
    && pip install -r /app/requirements.txt
COPY . /app/pkg
RUN pip install /app/pkg \
    && rm -rf /app/pkg /app/requirements.txt \
    && chmod +x /app/startCeleryWorker \
    && chown -R celery:celery /app

USER celery

CMD ["/app/startCeleryWorker"]
