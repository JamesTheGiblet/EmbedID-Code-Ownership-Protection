# Prelude: Importing modules we don't really need
import time
import sys
import random

# Act I: Define a character to speak
class Speaker:
    def __init__(self, name):
        self.name = name
        self.voice_style = "dramatic"
    
    def breathe(self):
        print(f"{self.name} inhales deeply...")
        time.sleep(0.5)
    
    def pause(self, duration=1):
        print(f"{self.name} pauses for {duration} second(s)...")
        time.sleep(duration)
    
    def speak(self, message):
        print(f"{self.name} ({self.voice_style} voice): {message}")

# Act II: Define the message
class Message:
    def __init__(self):
        self.words = ["Hello", ",", "World", "!"]
    
    def assemble(self):
        return " ".join([word if word.isalpha() else word for word in self.words])

# Act III: The stage manager
class StageManager:
    def __init__(self, speaker, message):
        self.speaker = speaker
        self.message = message
    
    def prepare_scene(self):
        print("Setting the stage...")
        time.sleep(1)
        print("Lights on.")
        time.sleep(1)
        print("Audience silent.")
        time.sleep(1)
    
    def cue_speaker(self):
        self.speaker.breathe()
        self.speaker.pause()
        final_message = self.message.assemble()
        self.speaker.speak(final_message)

# Act IV: The performance
def main():
    print("🎬 The Performance Begins 🎬")
    actor = Speaker("Narrator")
    script = Message()
    director = StageManager(actor, script)
    
    director.prepare_scene()
    director.cue_speaker()
    print("🎭 Curtain Call 🎭")

# Encore: Run the show
if __name__ == "__main__":
    main()