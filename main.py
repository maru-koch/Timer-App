from kivy import config
from kivy.app import App
import time
from kivy.clock import Clock
from kivy.core import window
from kivy.utils import get_color_from_hex as c


class StopWatchApp(App):
    started = False
    Seconds = 0
    count = 0

    def on_start(self):
        Clock.schedule_interval(self.update_time, 1)

    def update_time(self, nap):
        self.root.ids.time.text = time.strftime("%H : %M : %S")

    def update_counter(self):
        self.started = not self.started
        self.root.ids.start_stop.text =("Stop" if self.started else "Start")
        self.root.ids.start_stop.background_color = (c("#567890") if self.started else c("#454545"))
        Clock.schedule_interval(self.counter, self.count)
    
    def counter(self, count):
        if self.started:
            self.Seconds += count
            Seconds = int(self.Seconds % 60)
            Minutes = int(self.Seconds / 60) 
            MilliSec= int(self.Seconds *100 % 100)
            self.root.ids.counter.text = ("{}: {}: {}".format(Minutes, Seconds, MilliSec))
        else:
            Seconds = 0
            Minutes = 0
            MilliSec = 0
    
    def decrement_counter(self, count):
        self.Seconds -= count
        Seconds = int(self.Seconds %60)
        Minutes = int(self.Seconds / 60)
        MilliSec= int(Seconds * 60 % 60 )
        self.root.ids.counter.text = ("%02d: %02d: [size= 40]%02d[/40]" %(Minutes, Seconds, MilliSec))
    
    def reset(self):
        if self.started:
            self.Seconds = 0
        else:
            self.Seconds = 0
            self.started = False
            self.root.ids.start_stop.text = "Start" 
            self.root.ids.counter.text = ("{}: {}: {}".format(00,00,00))
            

if __name__ == "__main__":
    from kivy.core.window import Window
    
    Window.clearcolor = c("F2F1F3")
    Window.size = (500,300)
    StopWatchApp().run()