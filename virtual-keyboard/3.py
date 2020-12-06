from pynput import keyboard

def on_press(key):
    try:
        print('press{0}'.format(key.char))
    except AttributeError:
        print('pressspecial{0}'.format(key))

def on_release(key):
    print('{0}release'.format(key))
    if key==keyboard.Key.esc:
        return False

while True:
    with keyboard.Listener(
        on_press = on_press,
        on_release = on_release) as listener:
        listener.join()