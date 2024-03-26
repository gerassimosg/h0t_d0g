h0t_d0g is a state-of-the-art device that solves a pressing issue in our society: hot dog detection. Using a Raspberry Pi 3B+, a Raspberry Pi HQ camera module and a pretrained convolutional neural network called [YOLOv8](https://github.com/ultralytics/ultralytics/tree/main?tab=readme-ov-file), we have been able to create a device that can tell you if an object is:
  1. A hog dog
  2. NOT a hot dog

The design also features a custom Raspberry Pi hat that includes a button for triggering the camera module, and an OLED screen, LEDs, buzzers and vibrational motors for indication.

Yes, we are aware this device is similar to a bit from [Silicon Valley](https://www.youtube.com/watch?v=ACmydtFDTGs&ab_channel=HBO). Consider this another beautiful example of [simultaneous invention](https://en.wikipedia.org/wiki/Multiple_discovery). A demo of our device can be seen here.

```bash
python3 main.py --option
```
