import math
NOTES = {
            "X": 0.0,
            'C': 261.63,
            'C#': 277.18,
            'D': 293.66,
            'D#': 311.13,
            'E': 329.63,
            'F': 349.23,
            'F#': 392.00,
            'G': 392.00,
            'G#': 415.30,
            'A': 440.00,
            'A#': 466.16,
            'B': 493.88
}


class Voice:
    def __init__(self, oscillator, octave, notes=[]):
        self.notes = notes
        self.oscillator = oscillator
        self.multiplier = math.pow(2.0,octave*1.0) # 
    
    def __iter__(self):
        for note in self.notes:
            oscillator = self.oscillator(NOTES[note]*self.multiplier,.5)
            for x in range(11025): ## 44100/4 = quarter second beat
                yield next(oscillator)
        raise StopIteration
    
    
    def remove(self,index):
        del self.notes[index]
        
    def add(self,note):
        self.notes = self.notes + [note]

    def set(self,note,index):
        self.notes[index] = note

    def get(self,index):
        return self.notes[index]