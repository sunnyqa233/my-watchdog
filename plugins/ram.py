import psutil


def get_ram_used_percentage() -> float:
    return psutil.virtual_memory().percent


def get_swap_used_percentage() -> float:
    return psutil.swap_memory().percent
