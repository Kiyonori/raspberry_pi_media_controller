import analog_digital_converter.GetWattage as GetWattage
import analog_digital_converter.GetADS as GetADS
import adafruit_ads1x15.ads1115 as ads1115
from adafruit_ads1x15.ads1x15 import Mode

ads = GetADS.execute()

while True:
    wattage: float = GetWattage.execute(
        ads,
        ads1115.P0,
        ads1115.P1,
        Mode.CONTINUOUS,
        samples_per_second=860,
    )

    print(wattage)
