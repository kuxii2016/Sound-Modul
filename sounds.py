import pygame.mixer
from pygame.mixer import Sound
from gpiozero import Button
from signal import pause

pygame.mixer.init(44100, 16, 2, 4096)

sound_pins = {
    2: Sound("Dampffiff7.wav"),
    3: Sound("E-Lok-Pfiff6.wav"),
    4: Sound("ICEHorn1.wav"),

    27: Sound("Zugdurchfahrt.Gl.1.wav"),
    22: Sound("Zugdurchfahrt.Gl.2.wav"),
    25: Sound("Zugdurchfahrt.Gl.3.wav"),
     9: Sound("Zugdurchfahrt.Gl.4.wav"),
     6: Sound("Ans.zp9.Gl1.eig.wav"),
    13: Sound("Ans.zp9.Gl2.eig.wav"),
    19: Sound("Ans.zp9.Gl3.eig.wav"),
    26: Sound("Ans.zp9.Gl4.eig.wav"),

}


buttons = [Button(pin) for pin in sound_pins]

for button in buttons:
    sound = sound_pins[button.pin.number]
    button.when_pressed = sound.play

pause()
    
