from setuptools import setup, find_packages

setup(name='genWorkflowTaskQueue',
      version='0.4',
      packages=find_packages(),
      install_requires=[
          'jinja2',
      ],
      scripts=['genWorkflowTaskQueue']

      )
