
# Voice Audio To Text Converter

This project is a simple Python script that converts audio files into text using the OpenAI API.

## Project Structure

- `main.py`: The main script that processes audio files and transcribes them into text.
- `requirements.txt`: Python dependencies required to run the project.
- `.env.example`: Example of the environment variables needed to run the project.
- `audios/`: Directory to place your audio files for transcription.
- `transcriptions.txt`: Output file where the transcriptions are saved.

## Setup Instructions

### Prerequisites

Ensure you have Python 3.6+ installed on your system.

### Steps to Run the Project

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/LSP20xx/voice-audio-to-text-converter
   cd voice-audio-to-text-converter
   ```

2. **Create and Activate a Virtual Environment**:
   - On Linux/MacOS:

     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

   - On Windows:

     ```bash
     python -m venv venv
     .\venv\Scripts\activate
     ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up Environment Variables**:
   - Create a `.env` file in the root directory based on the `.env.example` file.
   - Add your OpenAI API key in the `.env` file:

     ```env
     OPENAI_API_KEY=your-api-key-here
     ```

5. **Place Audio Files**:
   - Place the audio files you want to transcribe in the `audios/` directory.

6. **Run the Script**:

   ```bash
   python main.py
   ```

7. **View Transcriptions**:
   - The transcriptions will be saved in `transcriptions.txt` in the root directory.

## Supported Audio Formats

The following audio formats are supported:

- .ogg
- .mp3
- .wav
- .m4a
- .flac
- .aac

## License

This project is licensed under the MIT License.
