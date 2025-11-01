# Instrument Automation with Python and PyVISA

This is my first GitHub repository, created mainly for learning and sharing.
I hope it can help someone that is just starting like me :).
This project give us a really basic insight on Instrument Autotion with PyVisa, and its use on industry.


## 📂 Project Structure
```
instrument_automation/
│
├── test_list_resources.py     # Lists all connected instruments
├── test_current_set.py        # Sets current limit and resets the instrument
├── test_ramp_slew.py          # Performs a fast voltage ramp (e.g., 9V → 5V)
│
├── README_EN.md               # This file
└── LICENSE                    # MIT License
```

## ⚙️ Requirements
- Python 3.8 or higher  
- PyVISA library  
- Installed VISA driver (NI-VISA or Keysight IO Libraries Suite)

### Installation
```bash
pip install pyvisa
```

## ▶️ How to Run
```bash
python test_list_resources.py
python test_current_set.py
python test_ramp_slew.py
```

## 📘 License
This project is distributed under the MIT License — see the `LICENSE` file for details.
