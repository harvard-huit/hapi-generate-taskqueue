from setuptools import setup, find_packages

setup(name='genWorkflowTaskQueue',
      version='0.0',
      packages= find_packages(),
      install_requires=[
          'jinja2',
      ],
      entry_points={
        'console_scripts': [
            'genWorkflowTaskQueue = genWorkflowTaskQueue.__main__:main',
        ]
    }
)
