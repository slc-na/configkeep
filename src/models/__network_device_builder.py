from .__network_device import NetworkDevice
from .__network_device_type import NetworkDeviceType

class NetworkDeviceBuilder:
    def __init__(self, device_type: NetworkDeviceType):
        self.__networkDevice = NetworkDevice(device_type)

        # Default values
        self.__networkDevice.__port = '22'
        self.__networkDevice.__secret = ''

    def set_host(self, host: str) -> 'NetworkDeviceBuilder':
        self.__networkDevice.__host = host
        return self
    
    def set_username(self, username: str) -> 'NetworkDeviceBuilder':
        self.__networkDevice.__username = username
        return self
    
    def set_password(self, password: str) -> 'NetworkDeviceBuilder':
        self.__networkDevice.__password = password
        return self
    
    def set_port(self, port: str) -> 'NetworkDeviceBuilder':
        self.__networkDevice.__port = port
    
    def set_secret(self, secret: str) -> 'NetworkDeviceBuilder':
        self.__networkDevice.__secret = secret
    
    def build(self) -> NetworkDevice:
        return self.__networkDevice