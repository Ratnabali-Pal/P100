# Multi-Video Summarization Project

This project uses OpenAI's Whisper to transcribe audio from video files. The output is provided as both a plain text file and an SRT subtitle file.

## Setup

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    cd <your-repository-name>
    ```

2.  **Install dependencies:**

    This project requires `ffmpeg` to be installed on your system.

    *   **On Ubuntu/Debian:**
        ```bash
        sudo apt update && sudo apt install ffmpeg
        ```
    *   **On macOS (using Homebrew):**
        ```bash
        brew install ffmpeg
        ```
    *   **On Windows:**
        Download the executable from the [official ffmpeg website](https://ffmpeg.org/download.html) and add it to your system's PATH.

    After installing `ffmpeg`, install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  Place the audio file you want to transcribe (e.g., `1.wav`) in the root directory of the project.

2.  Run the `transcribe.py` script:
    ```bash
    python transcribe.py
    ```

The script will generate two files:
*   `1.txt`: A plain text file containing the full transcription.
*   `1.srt`: A subtitle file with timestamps.```