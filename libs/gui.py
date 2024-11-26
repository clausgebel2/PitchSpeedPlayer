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

from PyQt6.QtWidgets import QPushButton, QVBoxLayout, QWidget, QFileDialog, QSlider, QLabel, QHBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon

class AudioPlayerGUI(QWidget):
    def __init__(self, event_handler):
        super().__init__()
        self.event_handler = event_handler
        self.init_ui()


    def init_ui(self):
        layout = QVBoxLayout()

        self.open_button = QPushButton('Open Audio File')
        self.open_button.setIcon(QIcon('icons/open.png'))
        self.open_button.clicked.connect(self.open_file)
        layout.addWidget(self.open_button)

        speed_layout = QVBoxLayout()

        self.speed_slider = QSlider(Qt.Orientation.Horizontal)
        self.speed_slider.setMinimum(1)
        self.speed_slider.setMaximum(200)
        self.speed_slider.setValue(100)
        self.speed_slider.valueChanged.connect(self.event_handler.set_speed)
        speed_layout.addWidget(self.speed_slider)

        speed_hlayout = QHBoxLayout()
        self.speed_slider_label = QLabel('Speed: 1.0')
        self.speed_slider.valueChanged.connect(self.update_speed_label)
        speed_hlayout.addWidget(self.speed_slider_label)
        speed_hlayout.addStretch()

        self.reset_speed_button = QPushButton('Reset Speed')
        self.reset_speed_button.setIcon(QIcon('icons/reset.png'))
        self.reset_speed_button.setFixedWidth(100)
        self.reset_speed_button.clicked.connect(self.reset_speed)
        speed_hlayout.addWidget(self.reset_speed_button)

        speed_layout.addLayout(speed_hlayout)

        pitch_layout = QVBoxLayout()

        self.pitch_slider = QSlider(Qt.Orientation.Horizontal)
        self.pitch_slider.setMinimum(1)
        self.pitch_slider.setMaximum(200)
        self.pitch_slider.setValue(100)
        self.pitch_slider.valueChanged.connect(self.event_handler.set_pitch)
        pitch_layout.addWidget(self.pitch_slider)

        pitch_hlayout = QHBoxLayout()
        self.pitch_slider_label = QLabel('Pitch: 1.0')
        self.pitch_slider.valueChanged.connect(self.update_pitch_label)
        pitch_hlayout.addWidget(self.pitch_slider_label)
        pitch_hlayout.addStretch()

        self.reset_pitch_button = QPushButton('Reset Pitch')
        self.reset_pitch_button.setIcon(QIcon('icons/reset.png'))
        self.reset_pitch_button.setFixedWidth(100)
        self.reset_pitch_button.clicked.connect(self.reset_pitch)
        pitch_hlayout.addWidget(self.reset_pitch_button)

        pitch_layout.addLayout(pitch_hlayout)

        layout.addLayout(speed_layout)
        layout.addLayout(pitch_layout)

        button_layout = QVBoxLayout()
        button_layout.addStretch()

        button_hlayout = QHBoxLayout()
        self.play_button = QPushButton('Play')
        self.play_button.setIcon(QIcon('icons/play.png'))
        self.play_button.clicked.connect(self.event_handler.play)
        button_hlayout.addWidget(self.play_button)

        self.pause_button = QPushButton('Pause')
        self.pause_button.setIcon(QIcon('icons/pause.png'))        
        self.pause_button.clicked.connect(self.event_handler.pause)
        button_hlayout.addWidget(self.pause_button)

        self.stop_button = QPushButton('Stop')
        self.stop_button.setIcon(QIcon('icons/stop.png'))            
        self.stop_button.clicked.connect(self.event_handler.stop)
        button_hlayout.addWidget(self.stop_button)

        button_layout.addLayout(button_hlayout)

        layout.addLayout(button_layout)

        self.setLayout(layout)


    def open_file(self):
        file_dialog = QFileDialog()
        filename, _ = file_dialog.getOpenFileName(self, 'Open Audio File', '', 'Audio Files (*.mp3 *.wav *.ogg)')
        if filename:
            self.event_handler.set_file(filename)
            self.event_handler.play()


    def update_speed_label(self, value):
        self.speed_slider_label.setText(f'Speed: {value / 100.0}')


    def update_pitch_label(self, value):
        self.pitch_slider_label.setText(f'Pitch: {value / 100.0}')


    def reset_speed(self):
        self.speed_slider.setValue(100)


    def reset_pitch(self):
        self.pitch_slider.setValue(100)


    def closeEvent(self, event):
        self.event_handler.stop()
        event.accept()
