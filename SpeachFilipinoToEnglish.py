import speech_recognition as sr
import pyttsx3
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(
    api_key='',
    organization='',
    project='',
)

def audio_to_text_and_translate():
    # Initialize recognizer class (for recognizing the speech)
    recognizer = sr.Recognizer()
    
    # Initialize the text-to-speech engine
    tts_engine = pyttsx3.init()

    # Use the microphone as the audio source
    with sr.Microphone() as source:
        print("Please speak into the microphone...")
        
        # Adjust for ambient noise and record audio
        recognizer.adjust_for_ambient_noise(source)
        audio_data = recognizer.listen(source)
        
        print("Processing your input...")
        
        # Convert audio to text using Google Web Speech API
        try:
            filipino_text = recognizer.recognize_google(audio_data)
            print(f"Recognized text: {filipino_text}")
            
            # Send the recognized text to ChatGPT for translation
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": f"Translate this Filipino text to English: {filipino_text}"}],
                temperature=1,
                max_tokens=2048,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )

            # Extract the content of the response
            translated_text = response.choices[0].message.content
            print("Translated text:", translated_text)
            
            # Use the text-to-speech engine to say the translated text
            tts_engine.say(translated_text)
            tts_engine.runAndWait()

        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
            tts_engine.say("Sorry, I could not understand the audio.")
            tts_engine.runAndWait()
        except sr.RequestError:
            print("Could not request results; check your network connection.")
            tts_engine.say("Could not request results; check your network connection.")
            tts_engine.runAndWait()

if __name__ == "__main__":
    audio_to_text_and_translate()
