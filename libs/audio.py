"""
Author: Claus Gebel

Pitch Speed Player
Copyright (C) 2024 Claus Gebel

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst

class AudioPlayer:
    def __init__(self):
        Gst.init(None)
        
        self.pipeline = Gst.Pipeline()
        
        self.file_source = Gst.ElementFactory.make("filesrc", "file-source")
        self.decoder = Gst.ElementFactory.make("decodebin", "decoder")
        self.audio_converter = Gst.ElementFactory.make("audioconvert", "converter")
        self.pitch = Gst.ElementFactory.make("pitch", "pitch")
        self.speed = Gst.ElementFactory.make("pitch", "speed")
        self.audio_sink = Gst.ElementFactory.make("autoaudiosink", "audio-output")
        
        self.pipeline.add(self.file_source)
        self.pipeline.add(self.decoder)
        self.pipeline.add(self.audio_converter)
        self.pipeline.add(self.pitch)
        self.pipeline.add(self.speed)
        self.pipeline.add(self.audio_sink)
        
        self.file_source.link(self.decoder)
        self.audio_converter.link(self.pitch)
        self.pitch.link(self.speed)
        self.speed.link(self.audio_sink)
        
        self.decoder.connect("pad-added", self.on_pad_added)


    def set_file(self, filename):
        self.file_source.set_property("location", filename)


    def on_pad_added(self, src, pad):
        sink_pad = self.audio_converter.get_static_pad("sink")
        if not sink_pad.is_linked():
            pad.link(sink_pad)


    def set_speed(self, value):
        speed = value / 100.0
        self.speed.set_property('tempo', speed)


    def set_pitch(self, value):
        pitch = value / 100.0
        self.pitch.set_property('pitch', pitch)


    def play(self):
        self.pipeline.set_state(Gst.State.PLAYING)


    def pause(self):
        self.pipeline.set_state(Gst.State.PAUSED)


    def stop(self):
        self.pipeline.set_state(Gst.State.NULL)
