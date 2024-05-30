from controller import Robot, Motor

class PIDController:
    def __init__(self, Kp, Ki, Kd, setpoint):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.setpoint = setpoint
        self.prev_error = 0
        self.integral = 0

    def update(self, feedback_value):
        # Функция корректировки
        error = self.setpoint - feedback_value
        self.integral += error
        derivative = error - self.prev_error

        output = self.Kp * error + self.Ki * self.integral + self.Kd * derivative

        self.prev_error = error

        return output

robot = Robot()

# Получение доступа к моторам робота
wheels = []
wheel_names = ["front left wheel", "front right wheel", "back left wheel", "back right wheel"]

for name in wheel_names:
    # Установка начальных параметров колес
    wheel = robot.getDevice(name)
    wheel.setPosition(float('inf'))
    wheel.setVelocity(0)
    wheels.append(wheel)

# Параметры ПИД-регулятора
Kp = 0.5
Ki = 0.2
Kd = 0.1
setpoint_speed = 6  # Желаемая скорость

# Создание экземпляра ПИД-регулятора
pid_controller = PIDController(Kp, Ki, Kd, setpoint_speed)

# Основной цикл управления
timestep = int(robot.getBasicTimeStep())
while robot.step(timestep) != -1:
    # Получение текущей скорости робота
    velocities = []
    for wheel in wheels:
        velocities.append(wheel.getVelocity())
    
    # Вычисление средней скорости всех колес
    wheels_speed = sum(velocities) / len(wheels)

    # Получение корректирующего сигнала от ПИД-регулятора
    control_signal = pid_controller.update(wheels_speed)
    
    # Применение корректировки к моторам
    for wheel in wheels:
        wheel.setVelocity(control_signal)
