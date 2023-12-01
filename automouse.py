import pyautogui as auto
import keyboard

for i in range(5):
    currPosition = auto.position()  # get position
    auto.moveTo(
        currPosition[0] + 50, currPosition[1], duration=0.2
    )  # move to x+50 in 0.5 second
    currPosition = auto.position()  # get position
    auto.moveTo(
        currPosition[0] - 50, currPosition[1], duration=0.2
    )  # move to x+50 in 0.5 second

    if keyboard.is_pressed(41):
        break
