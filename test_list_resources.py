# Lists all instruments connected via PyVISA
import pyvisa

rm = pyvisa.ResourceManager()  # Open VISA resource manager
resources = rm.list_resources()  # List connected instruments
print("Connected instruments:", resources)
