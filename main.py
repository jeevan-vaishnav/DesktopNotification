from socket import timeout
import time

from plyer import notification

if __name__ == "__main__":
    while(True):
        notification.notify(
            title="Please Drink Water",
            message="How much water do you need?\n15.5 cups (3.7 liters) for men \n 11.5 cups (2.7 liters)day for women.",
            app_icon="E:\Python Learning\PythonPratice\DesktopNotificaiton\icon.ico",
            timeout=10
        )
        time.sleep(60*60)
