import voices
import builder
import oscillators
class Song:

    def __init__(self,voices):
        self.voices = voices

    def addVoice(self,oscillator,octave,notes):
        self.voices = self.voices + [voices.Voice(oscillator,octave,notes)]
    
    def build(self):
        voices = []
        for x in range(len(self.voices)):
            cont = True
            voice = iter(self.voices[x])
            wav = []
            while cont:
                try:
                    wav = wav + [next(voice)]
                except:
                    cont=False
        voices = voices + wav
        builder.build(voices)
song = Song([voices.Voice(oscillators.sin_oscillation,0,["C","C","G","G","A","A","G"])])
song.build()