
# Run eeg-expy visual n170 with biosemi serial triggers
from eegnb.experiments.visual_n170.n170 import VisualN170
from eegnb.devices.eeg import EEG

thiseeg = EEG(device="biosemi", serial_port="COM4")
thisexp = VisualN170(eeg=thiseeg)
thisexp.duration = 15       # short run for test
thisexp.use_fullscr = False # best for debugging
thisexp.screen_num = 1 
thisexp.run()

"""
# Alternative version, creating serial object manually and handing to eeg-expy
from test_triggers2biosemi import open_port, send_trigger
thisport = open_port()
thiseeg = EEG(device="biosemi", serial_port=None)
thiseeg.serial = thisport
thisexp = VisualN170(eeg=thiseeg)
thisexp.duration = 15       # short run for test
thisexp.use_fullscr = False # best for debugging
thisexp.screen_num = 1 
thisexp.run()
"""
