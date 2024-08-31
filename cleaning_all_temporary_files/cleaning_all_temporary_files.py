import pyautogui
import time


def run_command(command):
    time.sleep(1)
    pyautogui.hotkey("win", "r")  # opening program
    time.sleep(0.5)
    pyautogui.typewrite(command)  # writing command
    time.sleep(0.2)
    pyautogui.press("enter")  # clicking enter / the file
    time.sleep(0.5)


def delete_all_permanently():
    # selecting all and delete all permanently
    pyautogui.hotkey("ctrl", "a")  # selecting everything
    time.sleep(0.1)
    pyautogui.hotkey("shift", "delete")  # deleting all permanently
    time.sleep(1.5)


def click_try_again():
    # click and enter "Try again"
    pyautogui.press("up")
    time.sleep(0.1)
    pyautogui.press("enter")  # enter for checkBox
    time.sleep(0.2)
    pyautogui.press("down")
    time.sleep(0.1)
    pyautogui.press("enter")  # enter for ok /delete
    time.sleep(2.1)


def click_skip():
    # click and enter "Skip"
    pyautogui.press("up")
    time.sleep(0.1)
    pyautogui.press("enter")  # enter for checkBox
    time.sleep(0.2)
    pyautogui.press("down")
    time.sleep(0.1)
    pyautogui.press("right")
    time.sleep(0.1)
    pyautogui.press("enter")  # enter for ok /delete
    time.sleep(2.1)


def close_active_window():
    pyautogui.hotkey("alt", "f4")  # closing active window
    time.sleep(0.5)


def main():
    run_command("%temp%")
    delete_all_permanently()
    click_try_again()
    click_skip()
    close_active_window()

    # ***************************

    run_command("temp")
    delete_all_permanently()
    click_try_again()
    click_skip()
    close_active_window()

    # ***************************

    pyautogui.hotkey("win", "r")  # opening program
    time.sleep(0.5)
    pyautogui.typewrite("cleanmgr")  # writing command
    time.sleep(0.2)
    pyautogui.press("enter")  # enter for open the program
    time.sleep(0.5)
    pyautogui.press("enter")  # enter for open the program
    time.sleep(0.5)


if __name__ == "__main__":
    main()
