import pySMART


def get_disk_temperature():
    """
    Get a list of tuple, contains disk temperature & device name.
    """
    disk_temperature_list = []

    device_list = pySMART.DeviceList()
    for device in device_list:
        disk_temperature_list.append(
            (device.attributes[194].raw_int, device.name)
        )

    return disk_temperature_list
