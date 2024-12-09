import RPi.GPIO as GPIO
import sys
import traceback

# motor_EN_A: Pin7        |  motor_EN_B: Pin11
# motor_A:  Pin8,Pin10    |  motor_B: Pin13,Pin12


class Motor:

    Motor_A_EN = 4
    Motor_B_EN = 17

    Motor_A_Pin1 = 26
    Motor_A_Pin2 = 21
    Motor_B_Pin1 = 27
    Motor_B_Pin2 = 18

    Dir_forward = 1
    Dir_backward = 0

    left_forward = 0
    left_backward = 1

    right_forward = 0
    right_backward = 1

    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(Motor.Motor_A_EN, GPIO.OUT)
        GPIO.setup(Motor.Motor_B_EN, GPIO.OUT)
        GPIO.setup(Motor.Motor_A_Pin1, GPIO.OUT)
        GPIO.setup(Motor.Motor_A_Pin2, GPIO.OUT)
        GPIO.setup(Motor.Motor_B_Pin1, GPIO.OUT)
        GPIO.setup(Motor.Motor_B_Pin2, GPIO.OUT)

        self.stop()

        try:
            self.pwm_A = GPIO.PWM(Motor.Motor_A_EN, 1000)
            self.pwm_B = GPIO.PWM(Motor.Motor_B_EN, 1000)

        except Exception:
            traceback.print_exc(file=sys.stdout)

    @staticmethod
    def stop():
        GPIO.output(Motor.Motor_A_Pin1, GPIO.LOW)
        GPIO.output(Motor.Motor_A_Pin2, GPIO.LOW)
        GPIO.output(Motor.Motor_B_Pin1, GPIO.LOW)
        GPIO.output(Motor.Motor_B_Pin2, GPIO.LOW)
        GPIO.output(Motor.Motor_A_EN, GPIO.LOW)
        GPIO.output(Motor.Motor_B_EN, GPIO.LOW)

    @staticmethod
    def motor_side(pwm, run, direction, speed, pin1, pin2, en):

        if run is False:
            GPIO.output(pin1, GPIO.LOW)
            GPIO.output(pin2, GPIO.LOW)
            GPIO.output(en, GPIO.LOW)
        else:
            if direction == Motor.Dir_backward:
                GPIO.output(pin1, GPIO.HIGH)
                GPIO.output(pin2, GPIO.LOW)
                pwm.start(100)
                pwm.ChangeDutyCycle(speed)
            elif direction == Motor.Dir_forward:
                GPIO.output(pin1, GPIO.LOW)
                GPIO.output(pin2, GPIO.HIGH)
                pwm.start(0)
                pwm.ChangeDutyCycle(speed)

    def motor_side_left(self, run, direction, speed):
        self.motor_side(self.pwm_B, run, direction, speed, Motor.Motor_B_Pin1, Motor.Motor_B_Pin2, Motor.Motor_B_EN)

    def motor_side_right(self, run, direction, speed):
        self.motor_side(self.pwm_A, run, direction, speed, Motor.Motor_A_Pin1, Motor.Motor_A_Pin2, Motor.Motor_A_EN)

    def move(self, speed_left, speed_right):

        print(f"speed_left  {speed_left}")
        print(f"speed_right {speed_right}")

        if speed_left >= 0:
            left_direction = Motor.left_forward
        else:
            left_direction = Motor.left_backward

        self.motor_side_left(run=True, direction=left_direction, speed=int(abs(speed_left)))

        if speed_right >= 0:
            right_direction = Motor.right_forward
        else:
            right_direction = Motor.right_backward

        self.motor_side_right(run=True, direction=right_direction, speed=int(abs(speed_right)))

    def forward(self, speed):
        self.move(speed, speed)

    def backward(self, speed):
        self.move(-speed, -speed)

    def turn_forward_left(self, speed, turn_power):
        self.move(speed * (1 - turn_power), speed)

    def turn_forward_right(self, speed, turn_power):
        self.move(speed, speed * (1 - turn_power))

    def turn_backward_left(self, speed, turn_power):
        self.move(-speed * (1 - turn_power), -speed)

    def turn_backward_right(self, speed, turn_power):
        self.move(-speed, -speed * (1 - turn_power))

    def turn_left(self, speed):
        self.move(-speed, speed)

    def turn_right(self, speed):
        self.move(speed, -speed)

    def destroy(self):

        self.stop()

        # Release resource
        GPIO.cleanup()


