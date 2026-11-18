# ME25C04 - Python Temperature Reading (Simulation)
import random
import time

while True:
    # LM35 maathiri voltage simulation
    voltage = random.uniform(0.20, 0.35) # 200mV to 350mV = 20°C to 35°C
    temperature = voltage * 100  # Formula: Temp = Voltage * 100
    
    print(f"Temperature: {temperature:.2f} °C")
    
    if temperature > 30:
        print("Alert: High Temperature! Fan ON")
    else:
        print("Temperature Normal")
    
    print("-" * 20)
    time.sleep(1)
