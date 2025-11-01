# Set current and reset the instrument
import pyvisa, time

ADDR = "USB0::0x0699::0x0346::C010101::INSTR"  # VISA address of the instrument

rm = pyvisa.ResourceManager()  # Open VISA resource manager
psu = rm.open_resource(ADDR, timeout=5000)  # Connect to the instrument

psu.write("CURR 15.0")  # Set current to 15 A
time.sleep(10)  # Wait for 10 seconds
psu.write("*RST")  # Reset the instrument
