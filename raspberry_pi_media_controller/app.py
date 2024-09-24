import math
import time
import board
import busio

import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.ads1x15 import Mode
from adafruit_ads1x15.analog_in import AnalogIn

from datetime import datetime
import csv

# Data collection setup
RATE = 860

# Create the I2C bus with a fast frequency
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1115(i2c)

chan0 = AnalogIn(ads, ADS.P0, ADS.P1)
chan1 = AnalogIn(ads, ADS.P2, ADS.P3)

# ADC Configuration
ads.mode = Mode.CONTINUOUS
ads.data_rate = RATE

def getRMS():
    voltage_ch0 : float
    sum_ch0 : float = 0
    voltage_ch1 : float
    sum_ch1 : float = 0

    counter= 0
    timepo = time.time()
    while (time.time() - timepo < 1):
        voltage_ch0 = chan0.voltage
        sum_ch0 = sum_ch0 + voltage_ch0**2
        counter = counter +1

    voltage_ch0 = math.sqrt( sum_ch0 / counter)

    counter= 0
    timepo = time.time()
    while (time.time() - timepo < 1):
        voltage_ch1 = chan1.voltage
        sum_ch1 = sum_ch1 + voltage_ch1**2
        counter = counter +1

    voltage_ch1 = math.sqrt( sum_ch1 / counter)

    return voltage_ch0,voltage_ch1


total_watth_ch0 : float = 0.0;
total_watth_ch1 : float = 0.0;

last_day = 0

while True:

    s_time = time.time()

    dt = datetime.fromtimestamp(s_time)
    if last_day!=dt.day:
        total_watth_ch0 = 0
        total_watth_ch1 = 0
        last_day = dt.day

    rms_vol_ch0,rms_vol_ch1 = getRMS()
    pass_sec = time.time()-s_time

    current_ch0 = (rms_vol_ch0 / 62) * 1800
    current_ch1 = (rms_vol_ch1 / 62) * 1800

    watt_ch0 = current_ch0 * 100
    watt_ch1 = current_ch1 * 100

    watth_ch0 = (pass_sec * watt_ch0) / 3600
    watth_ch1 = (pass_sec * watt_ch1) / 3600

    total_watth_ch0 += watth_ch0
    total_watth_ch1 += watth_ch1

    today = dt.strftime("%Y-%m-%d")
    nowtime = dt.strftime("%H:%M:%S")
    file_end = dt.strftime("%Y%m%d")

    print ('日付: %s 時刻: %s 全電力: %.2fw(%.2fwh) 電力ch0: %.2fw(%.2fwh) 電力ch1 %.2fw(%.2fwh)' % (today,nowtime,watt_ch0+watt_ch1,total_watth_ch0+total_watth_ch1,watt_ch0,total_watth_ch0,watt_ch1,total_watth_ch1))

    # with open('homepower_%s.csv' % (file_end),'a') as f:
    #     writer = csv.writer(f)
    #     writer.writerow([today,nowtime,watt_ch0+watt_ch1,total_watth_ch0+total_watth_ch1,watt_ch0,total_watth_ch0,watt_ch1,total_watth_ch1])