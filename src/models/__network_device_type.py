from enum import Enum

class NetworkDeviceType(Enum):
    """
    Enum untuk jenis os network device yang dipakai SLC.

    Untuk value dari setiap OS network device yang ada, bisa dilihat listnya di url berikut https://github.com/ktbyers/netmiko/blob/develop/PLATFORMS.md
    """
    CISCO_IOS = 'cisco_ios'
    CISCO_IOS_XE = 'cisco_xe'
    MIKROTIK_SWITCH_OS = 'mikrotik_switchos'
    MIKROTIK_ROUTER_OS = 'mikrotik_routeros'

    @staticmethod
    def from_string(string: str) -> 'NetworkDeviceType':
        """
        Converts string to enum
        """

        string = string.lower()

        translators = {
            "cisco ios xe": NetworkDeviceType.CISCO_IOS_XE,
            "cisco ios": NetworkDeviceType.CISCO_IOS,
            "mikrotik switchos": NetworkDeviceType.MIKROTIK_SWITCH_OS,
            "mikrotik routeros": NetworkDeviceType.MIKROTIK_ROUTER_OS,
        }

        if translators.get(string) is None:
            raise ValueError(f"device type \"{string}\" not found. Available keys: {", ".join([i for i in translators.keys()])}")

        return translators[string]
