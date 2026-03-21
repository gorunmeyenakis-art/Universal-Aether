# master_run.py

"""
This script is responsible for automatic dependency management and the master control system for the SGY Universal.
It runs `sgy_format.py` and manages all SGY Universal Master operations.
"""

import subprocess
import sys

class SGYUniversalManager:
    def __init__(self):
        self.dependencies = ["sgy_format.py"]

    def install_dependencies(self):
        for dependency in self.dependencies:
            self.check_and_install(dependency)

    def check_and_install(self, dependency):
        try:
            __import__(dependency.replace('.py', ''))
        except ImportError:
            print(f"Installing {dependency}...")
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', dependency])

    def run_sgy_format(self):
        print("Running sgy_format.py...")
        subprocess.run([sys.executable, 'sgy_format.py'])

    def manage_operations(self):
        self.install_dependencies()
        self.run_sgy_format()

if __name__ == '__main__':
    manager = SGYUniversalManager()
    manager.manage_operations()