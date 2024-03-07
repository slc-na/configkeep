from netmiko.exceptions import ReadTimeout

from .__network_device import NetworkDevice

class MikrotikDevice(NetworkDevice):
    from netmiko import BaseConnection

    def getConfig(self, connection: BaseConnection) -> str:
        # Solusi sementara untuk mikrotik, terutama device AP
        # Kedepannya boleh diganti karena kemungkinan kecil bisa ga ke-backup
        try:
            return connection.send_command("/export")
        except ReadTimeout:
            return connection.send_command_timing("/export")