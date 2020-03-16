genWorkflowTaskQueue
====================

This package installs scripts that can run from the command line. The script generates a setup and code structure that can automatically be installed within Cybercom. The template for making queues for celery produces a folder with a python package. Please see below on installation and operation.


## Install

        pip install https://github.com/culibraries/genWorkflowTaskQueue/zipball/master


## Operation


        $ genWorkflowTaskQueue <name of queue> 
        $ cd <name of queue>
        $ git init
        $ git add *
        $ git commit -m "<commit message>"
        
        # Github create repo
        # Follow instructions to add remote and push