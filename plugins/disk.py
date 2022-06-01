import psutil


def get_disk_usage():
    """
    Get a list of tuple containing partition usage(%) and partition mount-point and device name.
    """
    usage_list = []

    for partition in psutil.disk_partitions():
        mount_point = partition.mountpoint
        usage = psutil.disk_usage(mount_point)
        if "snap" in mount_point:  # Filter out ubuntu snap partition.
            pass
        else:
            usage_list.append(
                (usage.percent, mount_point, partition.device)
            )

    return usage_list
