import platform
import psutil

# Get CPU information
system_info = platform.uname()
print("System Info:")
print(f"    System: {system_info.system}")
print(f"    Node Name: {system_info.node}")
print(f"    Release: {system_info.release}")
print(f"    Version: {system_info.version}")
print(f"    Machine: {system_info.machine}")
print(f"    Processor: {system_info.processor}")

# Get CPU usage
cpu_usage = psutil.cpu_percent(interval=1, percpu=True)
print("\nCPU Usage:")
for i, percent in enumerate(cpu_usage):
    print(f"    Core {i + 1}: {percent}%")
