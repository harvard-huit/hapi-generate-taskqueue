HAPI Generate Task Queue
====================

This package installs scripts that can run from the command line. The script generates a python package that can be `pip` installed. The pacakage included a Dockerfile and the HAPI Github Action CI/CD yaml. Please see below on installation and operation.

## Install

        pip install https://github.com/harvard-huit/hapi-generate-taskqueue/zipball/master

## Upgrade

        pip install https://github.com/harvard-huit/hapi-generate-taskqueue/zipball/master  -U


## Operation

Please check or update the k8s vars files. Add specific secrets and env vars need for your code. 
`CELERY_QUEUE` - Needs to start with `hapi-` or update the Apigee App attribute `tenant-name` to include first part of  `CELERY_QUEUE` (eg: hapi or `hapi,ats,<< new queue name >>` ).


        $ generateTaskQueue <name of github repo or queue name> 
        $ cd <name of github repo or queue name>
        $ git init
        $ git add *
        $ git commit -m "<commit message>"

## Celery worker

The generated queue is a Celery worker. Its pieces:

- `<name>/tasks/tasks.py` - the task definitions.
- `deploy/celeryconfig.py` - Celery settings. It must sit next to the worker's working directory so `import celeryconfig` resolves.
- `deploy/startCeleryWorker` - the container entrypoint (`CMD ["/app/startCeleryWorker"]`).
- `deploy/requirements.txt` - runtime dependencies. The defaults are `celery>=5.5.0,<6.0` and `pymongo>=4.9.0,<5.0`. Those floors are the first releases with Python 3.13 and musllinux (Alpine) wheels, so the image installs without compiling from source.
- `Dockerfile` - based on `python:3.13-alpine`. It creates an unprivileged `celery` user, installs `requirements.txt` into a venv at `/app/venv`, then installs the queue package and runs as `celery`.

If a dependency has no musllinux wheel and must compile a C extension, add a throwaway build layer. The Dockerfile header shows the `apk add --virtual .build-deps` pattern.

### k8s vars

`k8s_vars/` has one shared file and one file per stack:

- `common_k8s_vars.yml` - everything shared by all environments: secret refs, the RabbitMQ/Mongo/CyberCom volume mounts, `target_namespace: celery-worker`, `target_replica_count`.
- `dev_k8s_vars.yml`, `stage_k8s_vars.yml`, `prod_k8s_vars.yml` - only the per-environment deltas. Currently that is `MONGO_HOSTS`, which differs for dev, stage and prod.

`harvard-huit/hapi-action-k8svars` deep-merges the stack file over `common_k8s_vars.yml` at deploy time. Keep values that are the same everywhere in the common file, and add an entry to a stack file only when it really differs. Keep the list-valued entries keyed by `name` or `key` so they merge rather than duplicate.

If the queue calls the Apigee X management API, uncomment the `apigee-auth` secret refs and the `apigee-auth` volume mount in `common_k8s_vars.yml`. The task then reads its service-account key from `/xkeys`.

### Local environment

To run the worker locally against a stack's settings, generate a `.env` from its `k8s_vars` from the repo root:

        $ genLocalEnvFile -s dev -t shell

This resolves the `target_app_secrets_ref` entries from AWS Secrets Manager and writes `export` lines to `./.env`. Secrets for `dev` are in the dev AWS account. For `stage` or `prod`, switch accounts with `aws-login` first.
