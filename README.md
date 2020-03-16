genWorkflowTaskQueue
====================

This package installs scripts that can be run from the command line. Script generates a setup and code structure that can be automatically install within cybercom. The template for generating queues for celery produces a folder with python package. Please see below on installation and operation.


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