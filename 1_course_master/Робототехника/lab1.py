from ev3dev2.motor import LargeMotor, SpeedDPS, OUTPUT_B, OUTPUT_C

import time


class PIDController:
    def __init__(self, Kp, Ki, Kd, target_speed):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.target_speed = target_speed
        self.old_err = 0
        self.integral = 0
        
        
    # Корректировка скорости
    def update(self, feedback_speed):
        new_err = self.target_speed - feedback_speed
        self.integral += new_err
        derivative = new_err - self.old_err

        output_speed = self.Kp * new_err + self.Ki * self.integral + self.Kd * derivative
        self.old_err = new_err

        return output_speed

# Инициализация моторов
left_motor = LargeMotor(OUTPUT_B)
right_motor = LargeMotor(OUTPUT_C)

# Коэффициенты ПИД
Kp = 0.1
Ki = 0.2
Kd = 1

# Целевая скорость
target_speed = 300

pid = PIDController(Kp, Ki, Kd, target_speed)

start_time = time.time()
while int(time.time() - start_time) < 10:
    # Получение текущей средней скорости
    current_left_speed = left_motor.speed
    current_right_speed = right_motor.speed
    avg_speed = (current_left_speed + current_right_speed) / 2
    print(avg_speed)
    
    # Корректировка скорости
    update_speed = pid.update(avg_speed)
    left_motor.on(SpeedDPS(update_speed))
    right_motor.on(SpeedDPS(update_speed))
    
    time.sleep(0.01)

left_motor.off()
right_motor.off()
