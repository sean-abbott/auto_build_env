__author__ = 'sean-abbott'

from setuptools import setup
from distutils.cmd import Command
import subprocess
import sys

def readme():
    with open('README.rst') as f:
        return f.read()

class BaseCommand(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

class RunDepCommand(BaseCommand):
    description = "install runtime dependencies"
    def run(self):
        cmd = ["pip", "install", "-r", "requirements.txt"]
        ret = subprocess.call(cmd)
        sys.exit(ret)

class TestDepCommand(BaseCommand):
    description = "install runtime dependencies"
    def run(self):
        cmd = ["pip", "install", "-r", "test_requirements.txt"]
        ret = subprocess.call(cmd)
        sys.exit(ret)

class BuildDepCommand(BaseCommand):
    description = "install runtime dependencies"
    def run(self):
        cmd = ["pip", "install", "-r", "build_requirements.txt"]
        ret = subprocess.call(cmd)
        sys.exit(ret)

def get_command_class():
    base = {}
    base['run_deps'] = RunDepCommand
    base['test_deps'] = TestDepCommand
    base['build_deps'] = BuildDepCommand
    return base

setup(
  name='auto_build_env',
  version=0.1,
  cmdclass=get_command_class(),
  description='Automatic Build Environment Generator',
  long_description=readme(),
  author='Sean Abbott',
  author_email='sean.abbott@datarobot.com',
  packages=['abe'],
  package_dir={'abe': 'src/abe'},
  package_data={
    '': ['*.rst'],
    'abe': ['templates/*']
  },
  entry_points={
      'console_scripts': ['abe=abe.cli:cli']
  },
)
