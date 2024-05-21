HAPI Generate Task Queue
====================

This package installs scripts that can run from the command line. The script generates a python package that can be `pip` installed. The pacakage included a Dockerfile and the HAPI Github Action CI/CD yaml. Please see below on installation and operation.

## Install

        pip install https://github.com/harvard-huit/hapi-generate-taskqueue/zipball/master

## Upgrade

        pip install https://github.com/harvard-huit/hapi-generate-taskqueue/zipball/master  -U


## Operation

Please check or update the k8s vars file. Add specific secrets and env vars need for your code. 
`CELERY_QUEUE` - Needs to start with `hapi-` or update the Apigee App attribute `tenant-name` to include first part of  `CELERY_QUEUE` (eg: hapi or `hapi,ats,<< new queue name >>` ).


        $ generateTaskQueue <name of github repo or queue name> 
        $ cd <name of github repo or queue name>
        $ git init
        $ git add *
        $ git commit -m "<commit message>"
        