# FilePermessionsChecker class, test1
from pathlib import Path
import stat
from json import dump

class FilePermessionsChecker():
    def scan(self, directory):
        for file_path in Path(directory).rglob("*"):
            if file_path.is_file():
                file_permissions = stat.filemode(file_path.stat().st_mode)
                yield str(file_path), file_permissions, file_permissions[3].lower() == "s"

    def suid_find(self, directory):
        suid_files = []
        for file_path, file_permissions, is_suid in self.scan(directory):
            if is_suid:
                suid_files.append(file_path)
        return suid_files

    def world_writable(self, directory):
        world_files = []
        for file_path, file_permissions, is_suid in self.scan(directory):
            if file_permissions[8] == "w":
                world_files.append(file_path)
        return world_files

    def report_json(self, data, output):
        with open(output, "w", encoding="UTF-8") as f:
            dump(data, f, indent=4)

test = FilePermessionsChecker()
print(test.report_json(test.world_writable("/home"), "testing.json"))