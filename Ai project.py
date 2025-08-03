from RealtimeSTT import AudioToTextRecorder
from RealtimeTTS import TextToAudioStream, SystemEngine, AzureEngine, ElevenlabsEngine
import cohere

co = cohere.Client('Your API Key')
engine = SystemEngine() 
stream = TextToAudioStream(engine)
message = ""
def process_text(text):
    print("You Said: " + text)
    message = text
    response = co.chat(
    message=message,
    model="command",
    temperature=0.2,
    max_tokens=50,
    chat_history=[
        {"role": "SYSTEM", "message": "You are a helpful assistant. Answer with short answers, around 20-25 words, in one sentence" }
    ]
    )
    answer = response.text
    print()
    print(answer)
    stream.feed(answer)
    stream.play_async()

if __name__ == '__main__':
    print("Wait until it says 'speak now'")
    recorder = AudioToTextRecorder()

    while True:
        recorder.text(process_text)
        
        