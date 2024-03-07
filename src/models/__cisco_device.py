from .__network_device import NetworkDevice
from utils.constants import NETWORK_DEVICE_PASSWORD

class CiscoDevice(NetworkDevice):
    from netmiko import BaseConnection

    def getConfig(self, connection: BaseConnection) -> str:
        connection.enable()
        output = connection.send_command("show run")

        # Untuk remove 3 line info
        output = output.split('\n')[3::]
        return "\n".join(output)