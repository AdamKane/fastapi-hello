import os
import shutil
from datetime import datetime

class PlanBackup:
    def __init__(self):
        self.root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.source_file = os.path.join(self.root_dir, 'PLAN.md')
        self.backup_dir = os.path.join(self.root_dir, 'archive', 'plans')

    def create_backup(self):
        if not os.path.exists(self.source_file):
            print(f"Error: Source file '{self.source_file}' not found.")
            return

        # Create backup directory if it doesn't exist
        os.makedirs(self.backup_dir, exist_ok=True)

        # Generate backup filename with current date, hours, minutes, seconds, and AM/PM
        current_datetime = datetime.now().strftime("%Y-%m-%d___%I-%M_%p")
        backup_filename = f"plan_{current_datetime}.md"
        backup_path = os.path.join(self.backup_dir, backup_filename)

        # Create the backup
        shutil.copy2(self.source_file, backup_path)
        print(f"Backup created: {backup_path}")

if __name__ == "__main__":
    backup = PlanBackup()
    backup.create_backup()
