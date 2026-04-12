# master_run.py

"""Bootstrap runner for local project dependencies and the main formatter."""

from pathlib import Path
import subprocess
import sys


class SGYUniversalManager:
    def __init__(self):
        self.project_root = Path(__file__).resolve().parent
        self.requirements_file = self.project_root / "requirements.txt"
        self.script_path = self.project_root / "sgy_format.py"

    def install_dependencies(self):
        if not self.requirements_file.exists():
            return
        requirements = [
            line.strip()
            for line in self.requirements_file.read_text(encoding="utf-8").splitlines()
            if line.strip() and not line.lstrip().startswith("#")
        ]
        if not requirements:
            print("No third-party dependencies declared; skipping pip install.")
            return
        print(f"Installing dependencies from {self.requirements_file.name}...")
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "-r", str(self.requirements_file)]
        )

    def run_sgy_format(self):
        print(f"Running {self.script_path.name}...")
        subprocess.run([sys.executable, str(self.script_path)], check=True)

    def manage_operations(self):
        self.install_dependencies()
        self.run_sgy_format()

if __name__ == '__main__':
    manager = SGYUniversalManager()
    manager.manage_operations()
