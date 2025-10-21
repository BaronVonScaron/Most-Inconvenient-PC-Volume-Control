from tkinter import *
import math
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from pycaw.api.endpointvolume import IAudioEndpointVolume
from comtypes import CLSCTX_ALL

# settings
main_screen = Tk()
main_screen.geometry('300x200')
main_screen.title('Most stupidest calculator EVAA')
main_screen.config(background='blue')
final_answer = 0
# photo
icon = PhotoImage(file='test.png')
main_screen.iconphoto(True, icon)

# MAIN
def calc():
    try:
        global final_answer
        number = float(entry.get())  # get number from Entry and convert to float
        answer = math.sqrt(number)
        integer = int(answer)
        final_answer = integer / 10 # FINAL ANSWER
        express_volume = integer * 10
        print(integer)# calculate square root
        result_label.config(text=f"Square root: {final_answer}, your volume is now {express_volume}")  # display result
        volume_control()
    except ValueError:
        result_label.config(text="Please enter a valid number")

def volume_control():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = interface.QueryInterface(IAudioEndpointVolume)

    # Make sure the value stays between 0.0 and 1.0
    level = max(0.0, min(final_answer, 1))

    # Set master volume (0.0 = mute, 1.0 = full)
    volume.SetMasterVolumeLevelScalar(level, None)
    print(f"System volume set to {int(level * 100)}%")


# GUI
label = Label(main_screen,
              text='Put number. Number sqr is volume. OK',
              highlightcolor='yellow',
              font=('Arial', 10, 'bold'),
              image=icon,
              compound='bottom')
label.pack()

entry = Entry(main_screen,
              font=('Arial', 10, 'bold'))
entry.pack(side="bottom")

calculation_button = Button(main_screen,
                            text='Calculate',
                            command=calc,
                            highlightcolor='yellow',
                            font=('Arial', 10, 'bold'))
calculation_button.pack(side="bottom")

result_label = Label(main_screen,
                     text='',
                     font=('Arial', 12, 'bold'),
                     bg='blue',
                     fg='white')
result_label.pack(side="bottom")

main_screen.mainloop()
