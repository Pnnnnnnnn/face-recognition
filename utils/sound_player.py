from playsound import playsound
import threading

def play_sound_thread_function(sound_path):
    playsound(sound_path)

def play_sound(sound_path):
    sound_thread = threading.Thread(target=play_sound_thread_function, kwargs={'sound_path':sound_path})
    sound_thread.start()