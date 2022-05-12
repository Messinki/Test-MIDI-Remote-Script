from __future__ import absolute_import, print_function, unicode_literals
import Live
from _Framework.ControlSurface import ControlSurface
from _Framework.ButtonElement import ButtonElement
from _Framework.InputControlElement import *
from _Framework.TransportComponent import TransportComponent
from _Framework.SliderElement import SliderElement
from _Framework.EncoderElement import EncoderElement
from _Framework.MixerComponent import MixerComponent
from _Framework.ClipSlotComponent import ClipSlotComponent
from _Framework.ChannelStripComponent import ChannelStripComponent
from _Framework.SceneComponent import SceneComponent
from _Framework.SessionComponent import SessionComponent

class Test(ControlSurface):
    u""" Script for Test Controllers """

    def __init__(self, c_instance):
        ControlSurface.__init__(self, c_instance)
        with self.component_guard():
            self._setup_device_and_transport_control()


    def _setup_device_and_transport_control(self):
        
       
        transport = TransportComponent()
        transport.set_play_button(ButtonElement(True, MIDI_CC_TYPE, 0, 118)) #this maps MIDI CC 118 on channel 1 to the play button
        transport.set_stop_button(ButtonElement(True, MIDI_CC_TYPE, 0, 117))
        transport.set_record_button(ButtonElement(True, MIDI_CC_TYPE, 0, 119))

       
  

