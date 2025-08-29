import psutil
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
from collections import deque

# Keep only last 60 data points (5 min at 5 sec interval)
max_points = 60

times = deque(maxlen=max_points)
cpu_usage = deque(maxlen=max_points)
ram_usage = deque(maxlen=max_points)
disk_usage = deque(maxlen=max_points)
ssd_usage = deque(maxlen=max_points)

fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, figsize=(8, 10))
plt.subplots_adjust(hspace=0.5)

start_time = time.time()

def update(frame):
    current_time = time.time() - start_time
    times.append(current_time)

    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    try:
        ssd = psutil.disk_usage('D:\\').percent
    except:
        ssd = 0

    cpu_usage.append(cpu)
    ram_usage.append(ram)
    disk_usage.append(disk)
    ssd_usage.append(ssd)

    # Clear and plot
    ax1.cla(); ax2.cla(); ax3.cla(); ax4.cla()

    ax1.plot(times, cpu_usage, label="CPU %", color="red")
    ax1.set_title("CPU Usage (Last 5 min)"); ax1.set_ylim(0, 100); ax1.legend(loc="upper right")

    ax2.plot(times, ram_usage, label="RAM %", color="blue")
    ax2.set_title("RAM Usage (Last 5 min)"); ax2.set_ylim(0, 100); ax2.legend(loc="upper right")

    ax3.plot(times, disk_usage, label="HDD %", color="green")
    ax3.set_title("HDD Usage (Last 5 min)"); ax3.set_ylim(0, 100); ax3.legend(loc="upper right")

    ax4.plot(times, ssd_usage, label="SSD %", color="orange")
    ax4.set_title("SSD Usage (Last 5 min)"); ax4.set_ylim(0, 100); ax4.legend(loc="upper right")

ani = animation.FuncAnimation(fig, update, interval=5000, cache_frame_data=False)  # 5 sec interval
plt.show()
