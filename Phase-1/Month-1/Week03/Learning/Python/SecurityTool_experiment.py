# Day 15 Exercise


class SecurityTool:
    def __init__(self, name, version):
        self.name = name
        self.version = version

    def __str__(self):
        return f"{self.name} v{self.version}"
    
    def __repr__(self):
        return f"{type(self).__name__}('{self.name}', '{self.version}')"
    
    def run(self):
        raise NotImplementedError("Subclasses must implement its run().")
    
class Scanner(SecurityTool):
    def __init__(self, name, version, target):
        super().__init__(name, version)
        self.target = target

    def run(self):
        return f"Scanning {self.target}....."

class PortScanner(Scanner):
    def __init__(self, name, version, target, ports):
        super().__init__(name, version, target)
        self.ports = ports

    def run(self):
        return f"Scanning ports {self.ports} on {self.target}..."


p = PortScanner("Nmap", "7.0", "192.168.1.1", [22, 80, 443])

# 1. Test isinstance
print(isinstance(p, SecurityTool))  # True (لأن PortScanner ابن Scanner ابن SecurityTool)
print(isinstance(p, Scanner))       # True
print(isinstance(p, PortScanner))   # True

# 2. Test issubclass
print(issubclass(PortScanner, SecurityTool))  # True
print(issubclass(PortScanner, Scanner))       # False (الأب مش ابن لابنه)
    
