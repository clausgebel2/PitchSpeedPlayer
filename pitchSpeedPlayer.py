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

import sys
from PyQt6.QtWidgets import QApplication
from libs.audio import AudioPlayer
from libs.event_handler import EventHandler
from libs.gui import AudioPlayerGUI

if __name__ == '__main__':
    app = QApplication(sys.argv)
    audio_player = AudioPlayer()
    event_handler = EventHandler(audio_player)
    player_gui = AudioPlayerGUI(event_handler)
    player_gui.resize(300, 200)
    player_gui.setWindowTitle("Pitch Speed Player")
    player_gui.show()
    sys.exit(app.exec())
