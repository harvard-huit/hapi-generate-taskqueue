from setuptools import setup, find_packages

setup(name='genWorkflowTaskQueue',
      version='0.3',
      packages= find_packages(),
      install_requires=[
          'jinja2',
      ],
      scripts=['genWorkflowTaskQueue']
      #entry_points={
      #  'console_scripts': [
      #      'genWorkflowTaskQueue = genWorkflowTaskQueue',
      #  ]
      #}
)
