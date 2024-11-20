from gtts import gTTS
import os

# Text you want to convert to speech
text = "FE!N, FE!N, FE!N, FE!N, FE!N (yeah)"

# Language for speech (en for English)
language = 'en'

# Create gTTS object
tts = gTTS(text=text, lang=language, slow=False)

# Save the converted speech to an audio file
tts.save("output.mp3")

# Play the audio file (optional)
os.system("start output.mp3")  # For Windows
# For Linux/macOS, you can use 'os.system("mpg321 output.mp3")' instead
