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

    left_forward = 1
    left_backward = 0

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

        self.motor_stop()

        try:
            self.pwm_A = GPIO.PWM(Motor.Motor_A_EN, 1000)
            self.pwm_B = GPIO.PWM(Motor.Motor_B_EN, 1000)

        except Exception:
            traceback.print_exc(file=sys.stdout)

    @staticmethod
    def motor_stop():
        GPIO.output(Motor.Motor_A_Pin1, GPIO.LOW)
        GPIO.output(Motor.Motor_A_Pin2, GPIO.LOW)
        GPIO.output(Motor.Motor_B_Pin1, GPIO.LOW)
        GPIO.output(Motor.Motor_B_Pin2, GPIO.LOW)
        GPIO.output(Motor.Motor_A_EN, GPIO.LOW)
        GPIO.output(Motor.Motor_B_EN, GPIO.LOW)

    def motor_side(self, run, direction, speed, pin1, pin2, en):

        if run is False:
            GPIO.output(pin1, GPIO.LOW)
            GPIO.output(pin2, GPIO.LOW)
            GPIO.output(en, GPIO.LOW)
        else:
            if direction == Motor.Dir_backward:
                GPIO.output(pin1, GPIO.HIGH)
                GPIO.output(pin2, GPIO.LOW)
                self.pwm_B.start(100)
                self.pwm_B.ChangeDutyCycle(speed)
            elif direction == Motor.Dir_forward:
                GPIO.output(pin1, GPIO.LOW)
                GPIO.output(pin2, GPIO.HIGH)
                self.pwm_B.start(0)
                self.pwm_B.ChangeDutyCycle(speed)

    def motor_side_left(self, run, direction, speed):
        self.motor_side(run, direction, speed, Motor.Motor_B_Pin1, Motor.Motor_B_Pin2, Motor.Motor_B_EN)

    def motor_side_right(self, run, direction, speed):
        self.motor_side(run, direction, speed, Motor.Motor_A_Pin1, Motor.Motor_A_Pin2, Motor.Motor_A_EN)

    def move(self, speed, direction, turn, radius=0.6):   # 0 < radius <= 1

        if direction == 'forward':
            if turn == 'right':
                self.motor_side_left(run=False, direction=Motor.left_backward, speed=int(speed*radius))
                self.motor_side_right(run=True, direction=Motor.right_forward, speed=speed)
            elif turn == 'left':
                self.motor_side_left(run=True, direction=Motor.left_forward, speed=speed)
                self.motor_side_right(run=False, direction=Motor.right_backward, speed=int(speed*radius))
            else:
                self.motor_side_left(run=True, direction=Motor.left_forward, speed=speed)
                self.motor_side_right(run=True, direction=Motor.right_forward, speed=speed)
        elif direction == 'backward':
            if turn == 'right':
                self.motor_side_left(run=False, direction=Motor.left_forward, speed=int(speed*radius))
                self.motor_side_right(run=True, direction=Motor.right_backward, speed=speed)
            elif turn == 'left':
                self.motor_side_left(run=True, direction=Motor.left_backward, speed=speed)
                self.motor_side_right(run=False, direction=Motor.right_forward, speed=int(speed*radius))
            else:
                self.motor_side_left(run=True, direction=Motor.left_backward, speed=speed)
                self.motor_side_right(run=True, direction=Motor.right_backward, speed=speed)
        elif direction == 'no':
            if turn == 'right':
                self.motor_side_left(run=True, direction=Motor.left_backward, speed=speed)
                self.motor_side_right(run=True, direction=Motor.right_forward, speed=speed)
            elif turn == 'left':
                self.motor_side_left(run=True, direction=Motor.left_forward, speed=speed)
                self.motor_side_right(run=True, direction=Motor.right_backward, speed=speed)
            else:
                self.motor_stop()
        else:
            pass

    def destroy(self):

        self.motor_stop()

        # Release resource
        GPIO.cleanup()


