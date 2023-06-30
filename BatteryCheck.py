#!/usr/bin/env python3
''' a program to send you a notification when your battery gets almost full'''

# made by Sultan Bazher

# Twitter : SultanCYB
# Email : sultanxx575@gmail.com

from psutil import sensors_battery
from plyer import notification
from time import sleep

# languages for the notification : arabic (ar), english (en)
language = "ar"

while (1):

    battery_percent = sensors_battery()[0]
    charging = sensors_battery()[2]

    if battery_percent in range(95, 101) and charging:
        # you can change this range

        if language == 'ar':
            notification.notify(
                app_name="منبه البطارية",
                title="منبه البطارية",
                message="البطارية ممتلئة",
                app_icon=""  # if you have an icon you can give the path here
            )

        else:
            notification.notify(
                app_name="Battery check",
                title="Battery check",
                message="Your battery is full",
                app_icon=""  # if you have an icon you can give the path here
            )

        sleep(1200)  ## sleep for 20 minutes if it reached the range

    else:
        sleep(300)  ## sleep for 5 minutes if it didnt reach the range yet
