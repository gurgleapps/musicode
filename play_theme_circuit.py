import time
import board
import pwmio

note_freq = {
  "A4": 440,
  "C5": 523,
  "D5": 587,
  "E5": 659,
  "R": 100
}

speaker = pwmio.PWMOut(board.GP2, frequency=440, duty_cycle=int(35565/2), variable_frequency=True)

tune = [["D5", 0.5], ["C5", 0.5], ["D5", 0.5], ["R", 0.5], ["D5", 0.5], ["C5", 0.5], ["D5", 0.5],
         ["R", 0.5], ["D5", 0.5], ["C5", 0.5], ["A4", 0.5], ["C5", 0.5], ["E5", 0.5], ["C5", 0.5], ["D5", 2]]

def play_note(note_name, duration):
    frequency = note_freq[note_name]
    if note_name == "R":
        speaker.duty_cycle=int(0)
    else:
        speaker.duty_cycle=int(35565/2)
    speaker.frequency=frequency
    time.sleep(duration)
    speaker.duty_cycle=0

for note in tune:
    play_note(note[0], note[1])
