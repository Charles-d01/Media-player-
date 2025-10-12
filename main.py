"""
A Simple Multimedia Player App (Python)

Contributors: @ekemini-udofia (github)
              @charles-d01 (github)

Depndencies/Requirements:

Python Libraries:
              PyQt5 - pip install PyQt5
              

Compilation: 
              To compile the python script to an executable, install auto-py-to-exe
              - pip install auto-py-to-exe
              Select the main.py script in the auto-py-to-exe menu.
              select icon.ico found @ res/icon.ico

Code Functions:
              The open function gets the path of the video you want to play
              //write the rest of theis later

              

For further ideas/contributions feel free to reach out via email - ekeminiabasiudofia@gmail.com or charleyndubest@gmail.com



"""


from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QAction, QFileDialog, QStyle, QSlider, QSizePolicy
from PyQt5.QtGui import QIcon
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import Qt, QUrl
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyPlayer")
        self.setGeometry(700, 400, 500, 500)
        self.setWindowIcon(QIcon("res\icon.ico"))

        #--assign widgets--
        self.media_player = QMediaPlayer(self)
        self.vid_widget = QVideoWidget(self)
        self.pause_play_btn = QPushButton(self)
        self.duration_bar = QSlider(Qt.Horizontal)
        self.hbox = QHBoxLayout(self)
        self.vbox = QVBoxLayout(self)
        self.label = QLabel(self)
        self.widget = QWidget(self)



        self.InitUI()


    def InitUI(self):
        #--setup toolbar--
        self.open_btn = QAction(QIcon("res\open.png"), "Open", self)
        self.toolbar = self.addToolBar("Toolbar")
        self.toolbar.addAction(self.open_btn)
        self.open_btn.triggered.connect(self.open_file)

        self.exit_btn = QAction(QIcon("res\exit.png"), "exit", self)
        self.toolbar.addAction(self.exit_btn)
    
        #--setup Pause/Play botton and duation bar--
        self.pause_play_btn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.pause_play_btn.setEnabled(False)
        self.pause_play_btn.clicked.connect(self.Pause_Play_File)


        self.duration_bar.setRange(0,0)
        self.duration_bar.sliderMoved.connect(self.slider_change)

        #--setup layout and label--
        self.hbox.addWidget(self.pause_play_btn)
        self.hbox.addWidget(self.duration_bar)

        self.vbox.addWidget(self.vid_widget)
        self.vbox.addLayout(self.hbox)
        #central widgets
        self.widget.setLayout(self.vbox)
        self.setCentralWidget(self.widget)

        self.label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum) #create sizepolicy label


        #--set Outputs--
        self.media_player.setVideoOutput(self.vid_widget)
        #media payer signal
        self.media_player.stateChanged.connect(self.Change_Play_State)
        self.media_player.positionChanged.connect(self.slider_position)
        self.media_player.durationChanged.connect(self.slider_duation)



        

    def open_file(self):
        self.filename, _ = QFileDialog.getOpenFileName(self, "select media file", "", "Media Files(*.mp4 *.mp3 *.avi *.mkv *.wav)")
        
        if self.filename != '':
            self.media_player.setMedia(QMediaContent(QUrl.fromLocalFile(self.filename)))
            self.pause_play_btn.setEnabled(True)

    def Pause_Play_File(self):
        if self.media_player.state() == QMediaPlayer.PlayingState:
            self.media_player.pause()
        else:
            self.media_player.play()

    def Change_Play_State(self):
        if self.media_player.state() == QMediaPlayer.PlayingState:
            self.pause_play_btn.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
        else:
         self.pause_play_btn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))

    def slider_position(self, position):
        self.duration_bar.setValue(position)

    def slider_duation(self, duration):
        self.duration_bar.setRange(0, duration)

    def slider_change(self, position):
        self.media_player.setPosition(position)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())