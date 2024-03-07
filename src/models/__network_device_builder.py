from .__network_device import NetworkDevice
from .__network_device_type import NetworkDeviceType

class NetworkDeviceBuilder:
    def __init__(self, device_type: NetworkDeviceType):
        self.__networkDevice = NetworkDevice(device_type)

        # Default values
        self.__networkDevice.port = '22'
        self.__networkDevice.secret = ''
        self.__networkDevice.host = None
        self.__networkDevice.username = None
        self.__networkDevice.password = None

    def set_host(self, host: str) -> 'NetworkDeviceBuilder':
        self.__networkDevice.host = host
        return self
    
    def set_username(self, username: str) -> 'NetworkDeviceBuilder':
        self.__networkDevice.username = username
        return self
    
    def set_password(self, password: str) -> 'NetworkDeviceBuilder':
        self.__networkDevice.password = password
        return self
    
    def set_port(self, port: str) -> 'NetworkDeviceBuilder':
        self.__networkDevice.port = port
        return self
    
    def set_secret(self, secret: str) -> 'NetworkDeviceBuilder':
        self.__networkDevice.secret = secret
        return self
    
    def build(self) -> NetworkDevice:
        return self.__networkDevice