from abc import ABC, abstractmethod

from .__network_device_type import NetworkDeviceType

class NetworkDevice(ABC):
    from netmiko import BaseConnection
    
    def __init__(self, device_type: NetworkDeviceType):
        self.device_type = device_type
        self.device_name = "Network Device"
        self.host = None
        self.username = None
        self.password = None
        self.port = None
        self.secret = None
    
    @abstractmethod
    def getConfig(self, net_connect: BaseConnection) -> str:
        pass

    # Allows class to be passed as kwargs
    def toDict(self):
        return dict({
            'device_type': self.device_type.value,
            'host': self.host,
            'username': self.username,
            'password': self.password,
            'port': self.port,
            'secret': self.secret
        })
    
    # Debug purpose
    def __str__(self):
       return (
f"""Device Type : {self.device_type.value}
Host        : {self.host}
Username    : {self.username}
Password    : {self.password}
Port        : {self.port}
Secret      : {self.secret}
"""
        )
