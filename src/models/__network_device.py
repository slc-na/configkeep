from .__network_device_type import NetworkDeviceType

class NetworkDevice:
    def __init__(self, device_type: NetworkDeviceType):
        self.__device_type = device_type
        self.__host = None
        self.__username = None
        self.__password = None
        self.__port = None
        self.__secret = None

    # Allows class to be passed as kwargs
    def __iter__(self):
        return iter({
            'device_type': self.__device_type,
            'host': self.__host,
            'username': self.__username,
            'password': self.__password,
            'port': self.__port,
            'secret': self.__secret
        })

