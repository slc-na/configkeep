from .__network_device_type import NetworkDeviceType

class NetworkDevice:
    __device_type: NetworkDeviceType
    __host: str
    __username: str
    __password: str
    __port: str
    __secret: str

    def __init__(self, device_type: NetworkDeviceType):
        self.__device_type = device_type

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

