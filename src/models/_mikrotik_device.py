from ._network_device import NetworkDevice as _NetworkDevice

class MikrotikDevice(_NetworkDevice):
    from netmiko import BaseConnection

    def getConfig(self, connection: BaseConnection) -> str:
        # Solusi sementara untuk mikrotik, terutama device AP
        # Kedepannya boleh diganti karena kemungkinan kecil bisa ga ke-backup
        return connection.send_command_timing("/export")