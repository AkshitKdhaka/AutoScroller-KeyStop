# AutoScroller-KeyStop 🖱️📜

A simple Python script that automatically scrolls the screen smoothly until the user stops it by pressing the `q` key. Useful for reading long documents, monitoring dashboards, or relaxing automation.

---

## 🚀 Features

- Smooth continuous scrolling
- Adjustable scroll speed and step size
- Graceful exit with the `q` key
- Cross-platform support with `pyautogui` and `keyboard`

---

## 🛠️ Requirements

- Python 3.x
- [pyautogui](https://pypi.org/project/pyautogui/)
- [keyboard](https://pypi.org/project/keyboard/)
- [pillow](https://pypi.org/project/Pillow/) *(pyautogui dependency)*

Install the dependencies using:

```bash
pip install pyautogui keyboard pillow
```

## Run the Script
After installing all the library run the script:
```bash
python scroll.py
```

You can tweak the scroll speed and amount inside scroll.py:
scroll_amount = -100  # Negative for scrolling down
scroll_speed = 0.8    # Delay in seconds between scrolls
