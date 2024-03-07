from .__network_device import NetworkDevice

class MikrotikDevice(NetworkDevice):
    from netmiko import BaseConnection

    def getConfig(self, connection: BaseConnection) -> str:
        return connection.send_command("/export")