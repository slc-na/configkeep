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