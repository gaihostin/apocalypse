import platform
OS_ENV = "other"

if "linux" in platform.platform().lower():
    OS_ENV = "linux"

