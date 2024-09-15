# Filipino to English Translation with OpenAI

This Python project captures audio input in Filipino from the microphone, converts it to text, and then uses OpenAI's GPT model to translate the text into English. The translated text is then spoken back to the user using a text-to-speech engine.

## Features

- **Speech Recognition**: Captures audio input from the microphone and converts it to text using Google's Web Speech API.
- **Translation**: Uses OpenAI's GPT model to translate recognized Filipino text to English.
- **Text-to-Speech**: Outputs the translated English text audibly using a text-to-speech engine (`pyttsx3`).

## Requirements

- Python 3.x
- `speech_recognition`
- `pyttsx3`
- `openai`
- `pyaudio`
