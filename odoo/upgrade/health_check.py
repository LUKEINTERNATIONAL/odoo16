import psutil

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    memory_info = psutil.virtual_memory()
    return memory_info.percent

def main():
    cpu_usage = get_cpu_usage()
    memory_usage = get_memory_usage()

    print(f"CPU Usage: {cpu_usage}%")
    print(f"Memory Usage: {memory_usage}%")

if __name__ == "__main__":
    main()
