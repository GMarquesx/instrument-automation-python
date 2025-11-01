import pyvisa, time

ADDR = "USB0::0x0699::0x0346::C010101::INSTR"  # VISA address of the instrument

rm = pyvisa.ResourceManager()  # Open VISA resource manager
psu = rm.open_resource(ADDR)  # Open communication with the instrument

psu.write("SLEW RATE MAX")  # Set slew rate to maximum
psu.write("VOLT 9")         # Set voltage to 9V
psu.write("OUTP ON")        # Turn on the output

psu.write("SLEW RATE 800")  # Set slew rate to 800 V/s
psu.write("VOLT 5")         # Change voltage to 5V

time.sleep(0.005)           # Wait 5 ms for ramp
psu.write("OUTP OFF")       # Turn off output
