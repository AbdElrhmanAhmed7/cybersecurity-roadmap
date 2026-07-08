# PS0-C Day 16
from json import dumps,dump,load,JSONDecodeError

class SecurityToolkit:
    def __init__(self,name, version):
        self.name = name
        self.version = version
        self._logs = []
        
    def __str__(self):
        return f"{self.name} v{self.version}"
    
    def __repr__(self):
        return f"{type(self).__name__}('{self.name}', '{self.version}')"
    
    def __len__(self):
        return len(self.logs)
    
    @property
    def logs(self):
        return self._logs

    @logs.setter
    def logs(self, log):
        self._logs = log


    def scan(self, target):
        if not target:
            return None
        message = f"Scanning {target}..."
        self.log(message)
        print("Scanned.")

    def log(self, message):
        self.logs.append(message)
    
    def report(self, fmt="text"):
        if fmt == "text":
            return "\n".join(self.logs)
        elif fmt == "json":
            return dumps(self.logs, indent=4)

    def save_results(self, path):
        try:
            with open(path, "w") as f:
                dump(self.logs, f, indent=4)
        except IOError:
            print("An Error occured.")
            return False
        else:
            return True
        
    def load_results(self, path):
        try:
            with open(path, "r", encoding="UTF-8") as f:
                self.logs = load(f)
        except FileNotFoundError:
            print("The File not exist.")
            return False
        except JSONDecodeError:  # <--- ده المهم!
            print("Error: The file is empty or contains invalid JSON.")
            return False
        else:
            return True
        

tool = SecurityToolkit("Scanner", "3.2")

corrupt_file = "corrupt.json"
with open(corrupt_file, 'w') as f:
    f.write("This is NOT valid JSON! {")      
result = tool.load_results(corrupt_file)

