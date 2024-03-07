from ._network_device import NetworkDevice as _NetworkDevice
from ._cisco_device import CiscoDevice as _CiscoDevice
from ._mikrotik_device import MikrotikDevice as _MikrotikDevice
from ._network_device_type import NetworkDeviceType as _NetworkDeviceType

class NetworkDeviceBuilder:
    def __init__(self, device_type: _NetworkDeviceType):
        # Solusi sementara
        if("cisco" in device_type.value):
            self.__networkDevice = _CiscoDevice(device_type)
        else:
            self.__networkDevice = _MikrotikDevice(device_type)

        # Default values
        self.__networkDevice.port = '22'
        self.__networkDevice.secret = ''
        self.__networkDevice.host = None
        self.__networkDevice.username = None
        self.__networkDevice.password = None

    def set_host(self, host: str) -> 'NetworkDeviceBuilder':
        self.__networkDevice.host = host
        return self
    
    def set_device_name(self, device_name: str) -> 'NetworkDeviceBuilder':
        self.__networkDevice.device_name = device_name
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
    
    def build(self) -> _NetworkDevice:
        return self.__networkDevice