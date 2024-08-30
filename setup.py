from setuptools import setup, find_packages

setup(name='generateTaskQueues',
      version='2.0.1',
      packages=find_packages(),
      install_requires=[
          'jinja2',
      ],
      include_package_data=True,
      scripts=['generateTaskQueue']

      )
