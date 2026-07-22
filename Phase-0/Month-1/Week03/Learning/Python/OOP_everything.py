# Exercising on everything i learnt in OOP
# Mini Home-Network Security Toolbox

from abc import ABC, abstractmethod

class NetworkDevice:
    total_devices = 0

    def __init__(self, name, ip_address, mac_address):
        self.name = name
        self._ip_address = ip_address
        self.__mac_address = mac_address
        self.last_log = None

        NetworkDevice.total_devices += 1

    @property
    def ip_address(self):
        return self._ip_address
    
    @ip_address.setter
    def ip_address(self, new_value):
        if new_value.count(".") == 3 and new_value:
            self._ip_address = new_value
        else:
            raise ValueError("Wrong Ip address format.")

    def get_mac_address(self):
        return self.__mac_address
    
    def set_mac_address(self, new_value):
        if len(new_value) == 17:
            self.__mac_address = new_value
        else:
            raise ValueError("Wrong Mac address format.")
        
    @staticmethod
    def is_valid_ip(ip):
        if ip.count(".") == 3 and ip:
            return True
        return False
    
    @classmethod
    def from_string(cls, value):
        new_class = value.split(",")
        return cls(new_class[0], new_class[1], new_class[2])
    
    def __str__(self):
        return f"Name : '{self.name}', Ip address : '{self.ip_address}', Mac address : '{self.get_mac_address()}'"

    def __eq__(self, other):
        if self.get_mac_address() == other.get_mac_address():
            return True
        else:
            return False
        
    def update_log(self, timestamp, status):
        self.last_log = self.ConnectionLog(timestamp, status)
        
    def status_report(self):
        return f"All nice in NetworkDevice class"

    class ConnectionLog:
        def __init__(self, timestamp, status):
            self.timestamp = timestamp
            self.status = status

class Scannable(ABC):
    @abstractmethod
    def scan(self):
        pass

class Firewall:
    def __init__(self):
        self.blocked_ip = ["123.456.9.1"]

    def is_blocking(self, ip):
        if ip in self.blocked_ip:
            return True
        return False

class Laptop(NetworkDevice):
    def __init__(self, name, ip_address, mac_address, os_name):
        super().__init__(name, ip_address, mac_address)
        self.os_name = os_name

    def __str__(self):
        return super().__str__() + f", Os_name: '{self.os_name}'"
    
    def status_report(self):
        return f"Our os {self.os_name} is good."
    
class Router(NetworkDevice):
    def __init__(self, name, ip_address, mac_address):
        super().__init__(name, ip_address, mac_address)
        self.firewall = Firewall()

    def status_report(self):
        return f"Our router is nice."

class SmartCamera(NetworkDevice, Scannable):
    def __init__(self, name, ip_address, mac_address):
        super().__init__(name, ip_address, mac_address)

    def scan(self):
        return f"No thing is found."
    
    def status_report(self):
        return self.scan()
    
class NetworkMonitorDashboard:
    def __init__(self):
        self.devices = []

    def add_device(self, device):
        self.devices.append(device)

    def list_all(self):
        for device in self.devices:
            print(device)

def run_security_scan(devices):
    for device in devices:
        print(device.scan())
            

if __name__ == "__main__":
    laptop = Laptop("Hp-678", "134.928.1.4", "AA:CC:DDA", "win12")
    router = Router("We - Fast", "134.928.1.1", "AA:CC:DDC")
    smart_camera = SmartCamera("FHD Sony 4.8", "134.928.1.7", "AA:CC:DDD")
    from_string = NetworkDevice.from_string("New Phone,134.928.1.8,AA:CC:DDD:FF")
    laptop.update_log("10:20pm", "Connected")
    print(laptop.last_log.status)
    print(NetworkDevice.total_devices)
    devices = [laptop, router, smart_camera]
    for device in devices:
        print(device.status_report())

    NetworkMonitor = NetworkMonitorDashboard()
    for device in devices:
        NetworkMonitor.add_device(device)

    NetworkMonitor.list_all()
    run_security_scan(devices= [smart_camera])
    try:
        run_security_scan(devices= [laptop])
        error = Scannable()
    except Exception as e:
        pass
    new_laptop = Laptop("Hp-6788", "134.928.1.3", "AA:CC:DDA", "win12")
    print( new_laptop == laptop)

