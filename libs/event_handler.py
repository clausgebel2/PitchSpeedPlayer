"""
Author: Claus Gebel

Pitch and Speed Changer
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

class EventHandler:
    def __init__(self, audio_player):
        self.audio_player = audio_player


    def set_file(self, filename):
        self.audio_player.set_file(filename)


    def set_speed(self, value):
        self.audio_player.set_speed(value)


    def set_pitch(self, value):
        self.audio_player.set_pitch(value)


    def play(self):
        self.audio_player.play()


    def pause(self):
        self.audio_player.pause()
        

    def stop(self):
        self.audio_player.stop()
