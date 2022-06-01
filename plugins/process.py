import psutil


def get_process_list():
    """
    Get a list of tuple, which contains current working process info.
    """
    process_list = []

    for pid in psutil.pids():
        try:
            process_object = psutil.Process(pid)
            process_name = process_object.name()
            process_bin = process_object.exe()
            process_list.append(
                (process_name, process_bin)
            )
        except psutil.AccessDenied:
            pass

    return process_list
