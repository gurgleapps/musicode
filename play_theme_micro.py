import machine
import time
note_freq = {
  "A4": 440,
  "C5": 523,
  "D5": 587,
  "E5": 659,
  "R": 100
}
tune = [["D5", 0.5], ["C5", 0.5], ["D5", 0.5], ["R", 0.5], ["D5", 0.5], ["C5", 0.5], ["D5", 0.5],
         ["R", 0.5], ["D5", 0.5], ["C5", 0.5], ["A4", 0.5], ["C5", 0.5], ["E5", 0.5], ["C5", 0.5], ["D5", 2]]
speaker = machine.PWM(machine.Pin(2))  
def play_note(note_name, duration):
    frequancy = note_freq[note_name]
    if note_name == "R":
        speaker.duty_u16(0)
    else:
        speaker.duty_u16(int(65535/2))
    
    speaker.freq(frequancy)
    time.sleep(duration)
    

for note in tune:
    play_note(note[0], note[1])
speaker.duty_u16(0)
  