"""
KCNI EEG Lab Test Function for BioSemi Triggers from Python
===========================================================

                                     JG & ChatGPT 2025-09-26


Usage:


  from test_triggers2biosemi import open_port, send_trigger

  myport = open_port()
  send_trigger(port=myport, code=5)
  myport.close()


Set the trigger format to 'decimal' in biosemi actiview to see and 
confirm that the trigger codes received are the ones sent

"""


import time, serial


def open_port(PORT_ID="COM4", BAUD=115200):
    """
    PORT_ID = "COM4"  # This is what we currently use as output from stim computer in KCNI EEG Lab  
    # on linux it should be sth like    # PORT_ID = "/dev/ttyUSB0"  # Linux
    # on macOS it should be sth like    # PORT_ID = "/dev/tty.usbserial-XXXX"  # macOS
    BAUD = 115200          # This matches ActiView's serial settings
    """
    from serial import Serial, EIGHTBITS, PARITY_NONE, STOPBITS_ONE

    my_serial = serial.Serial(PORT_ID, BAUD, bytesize=EIGHTBITS, parity=PARITY_NONE,
                              stopbits=STOPBITS_ONE, timeout=0, write_timeout=0)

    print("\nOpened Serial Port %s\n" %PORT_ID)

    return my_serial



def send_trigger(serial_obj, code: int, pulse_ms: int = 5, clearandflush=True) -> None:
    """
    Send an integer 045255 as a trigger byte, hold for pulse_ms, then send 0.
    """
    import time

    if not (0 <= code <= 255):  raise ValueError("code must be 045255")

    serial_obj.write(bytes([code]))

    if clearandflush:
      serial_obj.flush()  # push immediately
      time.sleep(pulse_ms / 1000.0)
      serial_obj.write(b"\x00")  # clear back to zero
      serial_obj.flush()


