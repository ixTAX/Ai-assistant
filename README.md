# Ai-assistant
Voice Assistant Using RealTimeSTT, Cohere AI, and RealTimeTTS

This project is a simple voice assistant that:

- Listens to your voice and converts it to text using **RealtimeSTT**.
- Sends the text to **Cohere AI** to generate a short, helpful response.
- Converts the AI response back to speech using **RealtimeTTS**.


## How It Works

1. **Speech-to-Text (STT):**  
   The `AudioToTextRecorder` listens to your microphone input and transcribes your speech into text in real time.

2. **AI Response Generation:**  
   The transcribed text is sent to Cohere’s chat model which replies with short, concise answers (around 20-25 words, usually one sentence).

3. **Text-to-Speech (TTS):**  
   The AI-generated answer is converted into speech and played aloud using RealTimeTTS.


## Usage

1. **Run the python code:**
   Run the code and wait until it says 'speak now'.
   
2. **Speaking:**
   Speak into your microphone and wait for the Ai assistant to response.

3. **Continue Speaking:**
   After the answer of the Ai assistant you can continue speaking with the Ai, you have to wait for its answer first.

## Requirements
- Python 10.8 (What is used in this project, other versions might work)
- `RealtimeSTT` package, run "pip install RealtimeSTT" in your command prompt.
- `RealtimeTTS` package, run "pip install -U realtimetts[all]" in your command prompt.
- `cohere` Python SDK.
- A microphone and speakers.
- Cohere API key (sign up at Cohere).
- Internet connection for Cohere API calls.

## The Code

<img width="821" height="458" alt="image" src="https://github.com/user-attachments/assets/b9f9e506-f002-4ea3-9435-d43b9473cc9d" />


## The Output

<img width="504" height="120" alt="Screenshot 2025-08-03 210346" src="https://github.com/user-attachments/assets/a92c5eb6-cc87-480b-a93b-ef76c3e91449" />

