

#  A Simple Multimedia Player (Python + PyQt5)

A lightweight multimedia player built using **Python** and **PyQt5**.
Supports basic playback of common **video** and **audio** formats and provides an intuitive, modern GUI.

---

## 🧑‍💻 Contributors

* [@ekemini-udofia](https://github.com/ekemini-udofia)
* [@charles-d01](https://github.com/charles-d01)

---

## ✨ Features

* 🎬 **Play videos and audio files** (`.mp4`, `.mp3`, `.avi`, `.mkv`, `.wav`)
* ⏯ **Pause/Play toggle button**
* 📂 **File browser** to open media files
* 🧭 **Toolbar with Open and Exit actions**
* 📊 **Seek bar (duration slider)** to navigate through the media
* 🪟 **Resizable, PyQt5-based GUI**
* 🧱 **Supports executable packaging** via `auto-py-to-exe`

---

## 🧩 Requirements

Before running the app, install the required dependencies:

```bash
pip install PyQt5
```

> ✅ Python 3.7 or newer is recommended.

---

## 🏗️ Compilation to Executable

To convert the Python script to a standalone executable:

1. Install **auto-py-to-exe**:

   ```bash
   pip install auto-py-to-exe
   ```

2. Launch the converter:

   ```bash
   auto-py-to-exe
   ```

3. In the GUI:

   * Select the main script → `main.py`
   * Add your app icon → `res/icon.ico`
   * Choose **"One File"** and **"Window Based"** mode
   * Build the executable

Your `.exe` file will appear in the `output` folder.

---

## ▶️ Usage

1. Run the application:

   ```bash
   python main.py
   ```

2. Open a media file:

   * Click the **Open** icon in the toolbar
   * Select a file (`.mp4`, `.mp3`, `.avi`, `.mkv`, `.wav`)

3. Control playback:

   * Press the **Play/Pause** button to toggle playback
   * Use the **slider** to jump to a specific timestamp

4. Exit the app via the **Exit** toolbar icon or the window close button.

---

## 🧠 Code Overview

### Main Components

| Component      | Description                              |
| -------------- | ---------------------------------------- |
| `QMediaPlayer` | Handles playback of audio/video files    |
| `QVideoWidget` | Displays video output in the main window |
| `QSlider`      | Controls and displays playback position  |
| `QAction`      | Used for toolbar actions (Open/Exit)     |
| `QMainWindow`  | Main application window                  |

### Key Functions

| Function              | Purpose                                    |
| --------------------- | ------------------------------------------ |
| `open_file()`         | Opens file dialog and loads selected media |
| `Pause_Play_File()`   | Toggles between play and pause states      |
| `Change_Play_State()` | Updates play/pause button icon dynamically |
| `slider_position()`   | Updates slider position as media plays     |
| `slider_duation()`    | Sets slider range based on media length    |
| `slider_change()`     | Seeks to selected position in the media    |

---

## 🧾 File Structure

```
PyPlayer/
│
├── main.py               # Main application file
├── res/
│   ├── icon.ico          # Application icon
│   ├── open.png          # Toolbar 'Open' icon
│   └── exit.png          # Toolbar 'Exit' icon
├── README.md             # Project documentation
└── requirements.txt      # Dependency list (optional)
```

---

## 🧭 Future Enhancements

* Volume control
* Playlist support
* Full-screen toggle
* Keyboard shortcuts
* Media metadata display

---

## 🤝 Contributing

Contributions and ideas are welcome!
Feel free to open an **issue** or submit a **pull request**.

---

## 🪪 License

This project is open-source and distributed under the **MIT License**.
You’re free to use, modify, and distribute it with attribution.

Would you like me to include a **badges section** (Python version, license, PyQt5 version, etc.) and GitHub formatting (like demo screenshots or a GIF preview)? It would make your README look much more professional for GitHub.
