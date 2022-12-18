# from win10toast import ToastNotifier

# toast = ToastNotifier()

# toast.show_toast("Title", "Message", duration=10)

from winotify import Notification, audio
import os

path_icon = os.path.join(os.getcwd(), "python.png")

toast = Notification(app_id="NeuralNine Script",
                     title="Message Title",
                     msg="Hello World!",
                     duration="long",
                     icon=path_icon)

toast.add_actions(label="Click !", launch="https://www.google.com/")

toast.set_audio(audio.LoopingAlarm, loop=True)

toast.show()