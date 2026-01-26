import voices
class Song:

    def __init__(self,voices):
        self.voices = voices

    def addVoice(self,oscillator,octave):
        self.voices = self.voices + [voices.Voice(oscillator,octave)]
    
    def build(self):
        pass