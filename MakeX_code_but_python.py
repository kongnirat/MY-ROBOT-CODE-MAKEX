import novapi
from mbuild import power_expand_board
from mbuild.encoder_motor import encoder_motor_class
from mbuild.smartservo import smartservo_class
from mbuild.ranging_sensor import ranging_sensor_class
from mbuild.smart_camera import smart_camera_class
from mbuild import power_manage_module
from mbuild import gamepad
import mbuild, math
import time

# initialize variables
Position = 0
press = 0
Ranging_distance = 0
Power = 0
Power__ = 0
Turn_power = 0
Turn_power__ = 0
Slide = 0
Slide__ = 0
ps = 0
_2 = 0
_3 = 0
Finish = 0
d_ranging = 0
base_speed = 0
motor_speed = 0
Max_speed = 0
left_speed = 0
right_speed = 0
block = 0
phrase1_finish = 0
speed_ = 0
speed_2 = 0
M4_3EM1_speed = 0
different_speed = 0
miss = 0
left = 0
right = 0
click = 0


# new class
encoder_motor_M1 = encoder_motor_class("M1", "INDEX1")
encoder_motor_M4 = encoder_motor_class("M4", "INDEX1")
encoder_motor_M3 = encoder_motor_class("M3", "INDEX1")
encoder_motor_M2 = encoder_motor_class("M2", "INDEX1")
encoder_motor_M6 = encoder_motor_class("M6", "INDEX1")
smartservo_1 = smartservo_class("M5", "INDEX1")
smartservo_2 = smartservo_class("M5", "INDEX2")
smartservo_3 = smartservo_class("M5", "INDEX3")
ranging_sensor_1 = ranging_sensor_class("PORT5", "INDEX1")
ranging_sensor_2 = ranging_sensor_class("PORT5", "INDEX2")
ranging_sensor_3 = ranging_sensor_class("PORT5", "INDEX3")
smart_camera_1 = smart_camera_class("PORT2", "INDEX1")
encoder_motor_M5 = encoder_motor_class("M5", "INDEX1")

def Anyblock2_N(startfrom):
    global Position, press, Ranging_distance, Power, Power__, Turn_power, Turn_power__, Slide, Slide__, ps, _2, _3, Finish, d_ranging, base_speed, motor_speed, Max_speed, left_speed, right_speed, block, phrase1_finish, speed_, speed_2, M4_3EM1_speed, different_speed, miss, left, right, click, miki
    smart_camera_1.open_light()
    Forward2_N(60)
    time.sleep(0.5)
    Forward2_N(200)
    while not ranging_sensor_1.get_distance() < 50:
      # DO SOMETHING
      pass

    Stopdrivetrain()
    Rotate_N_N_time_speed(1.2, 100)
    Slide2_N_right____left___(-150)
    while not (ranging_sensor_2.get_distance() < 14 and ranging_sensor_3.get_distance() < (14 + 2.2)):
      # DO SOMETHING
      pass

    Stopdrivetrain()
    while not (phrase1_finish == 6):
        time.sleep(0.001)
        if phrase1_finish > 0:
          Slide2_N_right____left___(-150)
          while not (ranging_sensor_2.get_distance() < 14 and ranging_sensor_3.get_distance() < (14 + 2.2)):
            # DO SOMETHING
            pass

          Stopdrivetrain()

        if smart_camera_1.detect_sign(1) or smart_camera_1.detect_sign(2):
          if smart_camera_1.get_sign_wide(1) > smart_camera_1.get_sign_wide(2) or smart_camera_1.get_sign_wide(1) == smart_camera_1.get_sign_wide(2):
            if smart_camera_1.get_sign_x(1) > 137:
              Forward2_N(60)
              while not (smart_camera_1.is_lock_sign(1, "x", 137) or not smart_camera_1.detect_sign(1)):
                # DO SOMETHING
                pass

              Stopdrivetrain()

            else:
              if smart_camera_1.get_sign_x(1) < 137:
                Forward2_N(-60)
                while not (smart_camera_1.is_lock_sign(1, "x", 137) or not smart_camera_1.detect_sign(1)):
                  # DO SOMETHING
                  pass

                Stopdrivetrain()

            claw_getblock_N(startfrom)
            phrase1_finish = phrase1_finish + 1

          else:
            if smart_camera_1.get_sign_wide(1) < smart_camera_1.get_sign_wide(2):
              if smart_camera_1.get_sign_x(2) > 137:
                Forward2_N(60)
                while not (smart_camera_1.is_lock_sign(2, "x", 137) or not smart_camera_1.detect_sign(2)):
                  # DO SOMETHING
                  pass

                Stopdrivetrain()

              else:
                if smart_camera_1.get_sign_x(2) < 137:
                  Forward2_N(-60)
                  while not (smart_camera_1.is_lock_sign(2, "x", 137) or not smart_camera_1.detect_sign(2)):
                    # DO SOMETHING
                    pass

                  Stopdrivetrain()

              claw_getblock_N(startfrom)
              phrase1_finish = phrase1_finish + 1

        else:
          if not smart_camera_1.detect_sign(1) and not smart_camera_1.detect_sign(2):
            Slide2_N_right____left___(150)
            time.sleep(0.6)
            Forward2_N(startfrom * 200)
            time.sleep(0.2)
            Stopdrivetrain()
            phrase1_finish = phrase1_finish + 1

def Anyblock_just_fastest_N(startfrom):
    global Position, press, Ranging_distance, Power, Power__, Turn_power, Turn_power__, Slide, Slide__, ps, _2, _3, Finish, d_ranging, base_speed, motor_speed, Max_speed, left_speed, right_speed, block, phrase1_finish, speed_, speed_2, M4_3EM1_speed, different_speed, miss, left, right, click, miki
    Forward2_N(60)
    time.sleep(0.5)
    Forward2_N(200)
    while not ranging_sensor_1.get_distance() < 50:
      # DO SOMETHING
      pass

    Stopdrivetrain()
    Rotate_N_N_time_speed(1.2, 100)
    Slide_distance_3_N_N_speed_distance(-130, 14)
    while not (phrase1_finish == 7):
        time.sleep(0.001)
        if phrase1_finish > 0:
          Forward2_N(startfrom * 200)
          time.sleep(0.3)
          Stopdrivetrain()
          Slide2_N_right____left___(-130)
          while not (ranging_sensor_2.get_distance() < 12 and ranging_sensor_3.get_distance() < (12 + 2.2)):
            # DO SOMETHING
            pass

          Stopdrivetrain()

        if phrase1_finish == 1 or phrase1_finish == 4 or not smart_camera_1.detect_sign(1) or not smart_camera_1.detect_sign(2) and phrase1_finish > 1:
          Slide2_N_right____left___(150)
          time.sleep(0.7)
          Stopdrivetrain()
          phrase1_finish = phrase1_finish + 1

        if smart_camera_1.detect_sign(1):
          if smart_camera_1.get_sign_x(1) > 137:
            Forward2_N(60)
            while not (smart_camera_1.is_lock_sign(1, "x", 137) or not smart_camera_1.detect_sign(1)):
              # DO SOMETHING
              pass

            Stopdrivetrain()

          else:
            if smart_camera_1.get_sign_x(1) < 137:
              Forward2_N(-60)
              while not (smart_camera_1.is_lock_sign(1, "x", 137) or not smart_camera_1.detect_sign(1)):
                # DO SOMETHING
                pass

              Stopdrivetrain()

          claw_getblock_N(1)
          phrase1_finish = phrase1_finish + 1

        else:
          if smart_camera_1.detect_sign(2) and phrase1_finish > 1:
            if smart_camera_1.get_sign_x(2) > 137:
              Forward2_N(60)
              while not (smart_camera_1.is_lock_sign(2, "x", 137) or not smart_camera_1.detect_sign(2)):
                # DO SOMETHING
                pass

              Stopdrivetrain()

            else:
              if smart_camera_1.get_sign_x(2) < 137:
                Forward2_N(-60)
                while not (smart_camera_1.is_lock_sign(2, "x", 137) or not smart_camera_1.detect_sign(2)):
                  # DO SOMETHING
                  pass

                Stopdrivetrain()

            claw_getblock_N(1)
            phrase1_finish = phrase1_finish + 1

def onlyGreen_auto__N(startfrom):
    global Position, press, Ranging_distance, Power, Power__, Turn_power, Turn_power__, Slide, Slide__, ps, _2, _3, Finish, d_ranging, base_speed, motor_speed, Max_speed, left_speed, right_speed, block, phrase1_finish, speed_, speed_2, M4_3EM1_speed, different_speed, miss, left, right, click, miki
    Forward2_N(60)
    time.sleep(0.5)
    Forward2_N(200)
    while not ranging_sensor_1.get_distance() < 50:
      # DO SOMETHING
      pass

    Stopdrivetrain()
    Rotate_N_N_time_speed(1.2, 100)
    Slide_distance_3_N_N_speed_distance(-130, 14)
    while not (phrase1_finish == 6):
        time.sleep(0.001)
        if phrase1_finish > 0:
          Forward2_N(startfrom * 200)
          time.sleep(0.5)
          Stopdrivetrain()
          Slide2_N_right____left___(-130)
          while not (ranging_sensor_2.get_distance() < 12 and ranging_sensor_3.get_distance() < 12):
            # DO SOMETHING
            pass

          Stopdrivetrain()

        if smart_camera_1.detect_sign(1):
          if smart_camera_1.get_sign_x(1) > 137:
            Forward2_N(60)
            while not (smart_camera_1.is_lock_sign(1, "x", 137) or not smart_camera_1.detect_sign(1)):
              # DO SOMETHING
              pass

            Stopdrivetrain()

          else:
            if smart_camera_1.get_sign_x(1) < 137:
              Forward2_N(-60)
              while not (smart_camera_1.is_lock_sign(1, "x", 137) or not smart_camera_1.detect_sign(1)):
                # DO SOMETHING
                pass

              Stopdrivetrain()

          claw_getblock_N(startfrom)
          phrase1_finish = phrase1_finish + 1

        else:
          if not smart_camera_1.detect_sign(1):
            Slide2_N_right____left___(150)
            time.sleep(0.6)
            Stopdrivetrain()
            phrase1_finish = phrase1_finish + 1

def claw_getblock_N(startfrom):
    global Position, press, Ranging_distance, Power, Power__, Turn_power, Turn_power__, Slide, Slide__, ps, _2, _3, Finish, d_ranging, base_speed, motor_speed, Max_speed, left_speed, right_speed, block, phrase1_finish, speed_, speed_2, M4_3EM1_speed, different_speed, miss, left, right, click, miki
    Arm_down_N(1)
    claw_N___1__unclaw___1__claw(-1)
    power_expand_board.set_power("DC4", -100)
    time.sleep(0.5)
    _E0_B9_80_E0_B8_89_E0_B8_B5_E0_B8_A2_E0_B8_87_E0_B8_82_E0_B8_A7_E0_B8_B2_N(200)
    if startfrom == left:
      _E0_B9_80_E0_B8_89_E0_B8_B5_E0_B8_A2_E0_B8_87_E0_B8_82_E0_B8_A7_E0_B8_B2_N(200)

    else:
      _E0_B9_80_E0_B8_89_E0_B8_B5_E0_B8_A2_E0_B8_87_E0_B8_8B_E0_B9_89_E0_B8_B2_E0_B8_A2_N(-200)

    time.sleep(0.7)
    Stopdrivetrain()
    Rotate_N_N_time_speed(0.6, startfrom * -200)
    power_expand_board.stop("DC4")
    power_expand_board.set_power("DC4", -100)
    claw_N___1__unclaw___1__claw(1)
    Rotate_N_N_time_speed(0.8, startfrom * 200)
    time.sleep(0.2)
    power_expand_board.stop("DC4")

def Slide_distance_3_N_N_speed_distance(speed, distance):
    global Position, press, Ranging_distance, Power, Power__, Turn_power, Turn_power__, Slide, Slide__, ps, _2, _3, Finish, d_ranging, base_speed, motor_speed, Max_speed, left_speed, right_speed, block, phrase1_finish, speed_, speed_2, M4_3EM1_speed, different_speed, miss, left, right, click, miki
    speed_ = speed
    speed_2 = -1 * speed
    different_speed = math.fabs((encoder_motor_M1.get_value("speed") - encoder_motor_M4.get_value("speed")))
    encoder_motor_M4.set_speed(speed_)
    encoder_motor_M1.set_speed(speed_)
    encoder_motor_M3.set_speed(speed_2)
    encoder_motor_M2.set_speed(speed_2)
    while not (ranging_sensor_2.get_distance() < distance and ranging_sensor_3.get_distance() < distance):
        time.sleep(0.001)
        if encoder_motor_M4.get_value("speed") > encoder_motor_M1.get_value("speed"):
          encoder_motor_M1.set_speed((speed_ + different_speed))
          encoder_motor_M3.set_speed((speed_2 - different_speed))

        else:
          if encoder_motor_M4.get_value("speed") < encoder_motor_M1.get_value("speed"):
            encoder_motor_M4.set_speed((speed_ + different_speed))
            encoder_motor_M2.set_speed((speed_2 - different_speed))

          else:
            if encoder_motor_M4.get_value("speed") == encoder_motor_M1.get_value("speed"):
              encoder_motor_M4.set_speed(speed_)
              encoder_motor_M1.set_speed(speed_)
              encoder_motor_M3.set_speed(speed_2)
              encoder_motor_M2.set_speed(speed_2)

    Stopdrivetrain()

def shooting_Auto__N(startfrom):
    global Position, press, Ranging_distance, Power, Power__, Turn_power, Turn_power__, Slide, Slide__, ps, _2, _3, Finish, d_ranging, base_speed, motor_speed, Max_speed, left_speed, right_speed, block, phrase1_finish, speed_, speed_2, M4_3EM1_speed, different_speed, miss, left, right, click, miki
    Forward2_N(60)
    time.sleep(0.5)
    if startfrom == left:
      _E0_B9_80_E0_B8_89_E0_B8_B5_E0_B8_A2_E0_B8_87_E0_B8_82_E0_B8_A7_E0_B8_B2_N(160)

    else:
      _E0_B9_80_E0_B8_89_E0_B8_B5_E0_B8_A2_E0_B8_87_E0_B8_8B_E0_B9_89_E0_B8_B2_E0_B8_A2_N(150)

    time.sleep(1.5)
    if startfrom == left:
      rotate_N_right____left___(-50)

    else:
      rotate_N_right____left___(50)

    time.sleep(0.7)
    Loadball_N(1)
    Forward2_N(50)
    while not ranging_sensor_1.get_distance() < 40:
      # DO SOMETHING
      pass

    Forward2_N(-60)
    time.sleep(1)
    if startfrom == left:
      rotate_N_right____left___(40)

    else:
      rotate_N_right____left___(-40)

    time.sleep(1)
    Forward2_N(-40)
    Stopdrivetrain()
    brushless_N_N(3, 80)
    time.sleep(0.3)
    while not (Finish == 6):
        time.sleep(0.001)
        Shoot()
        time.sleep(0.5)
        Rotate_N_N_time_speed(0.2, startfrom * 40)
        time.sleep(0.7)
        power_expand_board.stop("DC3")
        Finish = Finish + 1

    power_expand_board.stop("BL1")
    power_expand_board.stop("BL2")
    encoder_motor_M6.set_speed(0)

def _E0_B9_80_E0_B8_89_E0_B8_B5_E0_B8_A2_E0_B8_87_E0_B8_82_E0_B8_A7_E0_B8_B2_N(speed):
    global Position, press, Ranging_distance, Power, Power__, Turn_power, Turn_power__, Slide, Slide__, ps, _2, _3, Finish, d_ranging, base_speed, motor_speed, Max_speed, left_speed, right_speed, block, phrase1_finish, speed_, speed_2, M4_3EM1_speed, different_speed, miss, left, right, click, miki
    encoder_motor_M4.set_speed(0)
    encoder_motor_M3.set_speed((0 - speed))
    encoder_motor_M2.set_speed(speed)
    encoder_motor_M1.set_speed(0)

def _E0_B9_80_E0_B8_89_E0_B8_B5_E0_B8_A2_E0_B8_87_E0_B8_8B_E0_B9_89_E0_B8_B2_E0_B8_A2_N(speed):
    global Position, press, Ranging_distance, Power, Power__, Turn_power, Turn_power__, Slide, Slide__, ps, _2, _3, Finish, d_ranging, base_speed, motor_speed, Max_speed, left_speed, right_speed, block, phrase1_finish, speed_, speed_2, M4_3EM1_speed, different_speed, miss, left, right, click, miki
    encoder_motor_M4.set_speed((0 - speed))
    encoder_motor_M3.set_speed(0)
    encoder_motor_M2.set_speed(0)
    encoder_motor_M1.set_speed(speed)

def Forward2_N(speed):
    global Position, press, Ranging_distance, Power, Power__, Turn_power, Turn_power__, Slide, Slide__, ps, _2, _3, Finish, d_ranging, base_speed, motor_speed, Max_speed, left_speed, right_speed, block, phrase1_finish, speed_, speed_2, M4_3EM1_speed, different_speed, miss, left, right, click, miki
    encoder_motor_M2.set_speed((0 - speed))
    encoder_motor_M1.set_speed(speed)
    encoder_motor_M4.set_speed((0 - speed))
    encoder_motor_M3.set_speed(speed)

def Manual():
    global Position, press, Ranging_distance, Power, Power__, Turn_power, Turn_power__, Slide, Slide__, ps, _2, _3, Finish, d_ranging, base_speed, motor_speed, Max_speed, left_speed, right_speed, block, phrase1_finish, speed_, speed_2, M4_3EM1_speed, different_speed, miss, left, right, click, miki
    # DO SOMETHING
    pass

def Aungpao_N(speed):
    global Position, press, Ranging_distance, Power, Power__, Turn_power, Turn_power__, Slide, Slide__, ps, _2, _3, Finish, d_ranging, base_speed, motor_speed, Max_speed, left_speed, right_speed, block, phrase1_finish, speed_, speed_2, M4_3EM1_speed, different_speed, miss, left, right, click, miki
    encoder_motor_M2.set_speed((0 - speed))
    encoder_motor_M3.set_speed(speed)
    encoder_motor_M4.set_speed((0 - speed))

def Auto():
    global Position, press, Ranging_distance, Power, Power__, Turn_power, Turn_power__, Slide, Slide__, ps, _2, _3, Finish, d_ranging, base_speed, motor_speed, Max_speed, left_speed, right_speed, block, phrase1_finish, speed_, speed_2, M4_3EM1_speed, different_speed, miss, left, right, click, miki
    # DO SOMETHING
    pass

def Rotate_N_N_time_speed(Time_s_, Speed):
    global Position, press, Ranging_distance, Power, Power__, Turn_power, Turn_power__, Slide, Slide__, ps, _2, _3, Finish, d_ranging, base_speed, motor_speed, Max_speed, left_speed, right_speed, block, phrase1_finish, speed_, speed_2, M4_3EM1_speed, different_speed, miss, left, right, click, miki
    if Time_s_ > 0:
      encoder_motor_M2.set_speed(Speed)
      encoder_motor_M1.set_speed(Speed)
      encoder_motor_M4.set_speed(Speed)
      encoder_motor_M3.set_speed(Speed)
      time.sleep(float(Time_s_))
      Stopdrivetrain()

    else:
      if Time_s_ == 0:
        encoder_motor_M2.set_speed(Speed)
        encoder_motor_M1.set_speed(Speed)
        encoder_motor_M4.set_speed(Speed)
        encoder_motor_M3.set_speed(Speed)

def claw_N___1__unclaw___1__claw(direction):
    global Position, press, Ranging_distance, Power, Power__, Turn_power, Turn_power__, Slide, Slide__, ps, _2, _3, Finish, d_ranging, base_speed, motor_speed, Max_speed, left_speed, right_speed, block, phrase1_finish, speed_, speed_2, M4_3EM1_speed, different_speed, miss, left, right, click, miki
    if direction == 1:
      smartservo_2.move_to(55, 30)

    else:
      if direction == -1:
        smartservo_2.move_to(16, 30)
        time.sleep(0.3)
        if not smartservo_2.get_value("current") == 16:
          smartservo_2.set_power(-8)

def Arm_up_N(time_s_):
    global Position, press, Ranging_distance, Power, Power__, Turn_power, Turn_power__, Slide, Slide__, ps, _2, _3, Finish, d_ranging, base_speed, motor_speed, Max_speed, left_speed, right_speed, block, phrase1_finish, speed_, speed_2, M4_3EM1_speed, different_speed, miss, left, right, click, miki
    power_expand_board.set_power("DC4", -100)
    time.sleep(float(time_s_))
    power_expand_board.set_power("DC4", 2)

def Manual():
    global Position, press, Ranging_distance, Power, Power__, Turn_power, Turn_power__, Slide, Slide__, ps, _2, _3, Finish, d_ranging, base_speed, motor_speed, Max_speed, left_speed, right_speed, block, phrase1_finish, speed_, speed_2, M4_3EM1_speed, different_speed, miss, left, right, click, miki
    Power = gamepad.get_joystick("Ry") * 0.8
    Power__ = gamepad.get_joystick("Ry") * -0.8
    Turn_power = gamepad.get_joystick("Rx") * 0.6
    Turn_power__ = gamepad.get_joystick("Rx") * -0.6
    Slide = gamepad.get_joystick("Lx") * 0.7
    Slide__ = gamepad.get_joystick("Lx") * -0.7
    encoder_motor_M2.set_power((Power__ + ((Turn_power__ + Slide__))))
    encoder_motor_M1.set_power((Power + ((Turn_power__ + Slide__))))
    encoder_motor_M4.set_power((Power__ + ((Turn_power__ + Slide))))
    encoder_motor_M3.set_power((Power + ((Turn_power__ + Slide))))
    if gamepad.is_key_pressed("N1"):
      power_expand_board.set_power("DC6", 100)

    else:
      if gamepad.is_key_pressed("N4"):
        power_expand_board.set_power("DC6", -60)

      else:
        power_expand_board.stop("DC6")

    if gamepad.is_key_pressed("L1"):
      power_expand_board.set_power("DC3", 100)

    else:
      if gamepad.is_key_pressed("R1"):
        power_expand_board.set_power("DC3", -100)

      else:
        power_expand_board.stop("DC3")

    if gamepad.is_key_pressed("N2"):
      power_expand_board.set_power("DC4", -100)

    else:
      if gamepad.is_key_pressed("N3"):
        power_expand_board.set_power("DC4", 100)

      else:
        power_expand_board.set_power("DC4", 0)

    if gamepad.is_key_pressed("R2"):
      power_expand_board.set_power("DC2", 100)
      power_expand_board.set_power("DC5", 100)

    else:
      if gamepad.is_key_pressed("L2"):
        power_expand_board.set_power("DC2", -100)
        power_expand_board.set_power("DC5", -100)

      else:
        # DO SOMETHING
        pass

    if gamepad.is_key_pressed("Right"):
      brushless_N_N(90, 50)

    if gamepad.is_key_pressed("Down"):
      brushless_N_N(35, 50)

    if gamepad.is_key_pressed("Left"):
      Stop_DC()
      smart_camera_1.close_light()
      power_expand_board.stop("BL1")
      power_expand_board.stop("BL2")
      Stopdrivetrain()
      brushless_N_N(0, 0)
      Stop_loadball()
      encoder_motor_M5.set_power(0)
      encoder_motor_M6.set_power(0)

    if gamepad.is_key_pressed("Up"):
      brushless_N_N(95, 50)

    if gamepad.is_key_pressed("L_Thumb"):
      encoder_motor_M5.set_power(200)
      encoder_motor_M6.set_power(-200)

def Arm_down_N(time_s_):
    global Position, press, Ranging_distance, Power, Power__, Turn_power, Turn_power__, Slide, Slide__, ps, _2, _3, Finish, d_ranging, base_speed, motor_speed, Max_speed, left_speed, right_speed, block, phrase1_finish, speed_, speed_2, M4_3EM1_speed, different_speed, miss, left, right, click, miki
    power_expand_board.set_power("DC4", 100)
    time.sleep(float(time_s_))
    power_expand_board.set_power("DC4", 2)

def ROTATE3_BETA__N_N_R____L___(degee, speed):
    global Position, press, Ranging_distance, Power, Power__, Turn_power, Turn_power__, Slide, Slide__, ps, _2, _3, Finish, d_ranging, base_speed, motor_speed, Max_speed, left_speed, right_speed, block, phrase1_finish, speed_, speed_2, M4_3EM1_speed, different_speed, miss, left, right, click, miki
    encoder_motor_M1.move_to(encoder_motor_M1.get_value("angle") < 50, speed)
    encoder_motor_M2.move_to(encoder_motor_M2.get_value("angle") < 50, speed)
    encoder_motor_M3.move_to(encoder_motor_M3.get_value("angle") < 50, speed)
    encoder_motor_M4.move_to(encoder_motor_M4.get_value("angle") < 50, speed)

def Stop_DC():
    global Position, press, Ranging_distance, Power, Power__, Turn_power, Turn_power__, Slide, Slide__, ps, _2, _3, Finish, d_ranging, base_speed, motor_speed, Max_speed, left_speed, right_speed, block, phrase1_finish, speed_, speed_2, M4_3EM1_speed, different_speed, miss, left, right, click, miki
    power_expand_board.stop("DC2")
    power_expand_board.stop("DC3")
    power_expand_board.stop("DC4")
    power_expand_board.stop("DC5")
    power_expand_board.stop("DC6")

def Stopdrivetrain():
    global Position, press, Ranging_distance, Power, Power__, Turn_power, Turn_power__, Slide, Slide__, ps, _2, _3, Finish, d_ranging, base_speed, motor_speed, Max_speed, left_speed, right_speed, block, phrase1_finish, speed_, speed_2, M4_3EM1_speed, different_speed, miss, left, right, click, miki
    encoder_motor_M2.set_speed(0)
    encoder_motor_M1.set_speed(0)
    encoder_motor_M4.set_speed(0)
    encoder_motor_M3.set_speed(0)
    encoder_motor_M5.set_speed(0)
    encoder_motor_M6.set_speed(0)

def Stop_loadball():
    global Position, press, Ranging_distance, Power, Power__, Turn_power, Turn_power__, Slide, Slide__, ps, _2, _3, Finish, d_ranging, base_speed, motor_speed, Max_speed, left_speed, right_speed, block, phrase1_finish, speed_, speed_2, M4_3EM1_speed, different_speed, miss, left, right, click, miki
    power_expand_board.stop("DC2")
    power_expand_board.stop("DC5")

def Slide_N_N_right____left___(degree, speed):
    global Position, press, Ranging_distance, Power, Power__, Turn_power, Turn_power__, Slide, Slide__, ps, _2, _3, Finish, d_ranging, base_speed, motor_speed, Max_speed, left_speed, right_speed, block, phrase1_finish, speed_, speed_2, M4_3EM1_speed, different_speed, miss, left, right, click, miki
    encoder_motor_M1.move(degree, speed)
    encoder_motor_M2.move((0 - degree), speed)
    encoder_motor_M4.move(degree, speed)
    encoder_motor_M3.move((0 - degree), speed)

def Slide2_N_right____left___(speed):
    global Position, press, Ranging_distance, Power, Power__, Turn_power, Turn_power__, Slide, Slide__, ps, _2, _3, Finish, d_ranging, base_speed, motor_speed, Max_speed, left_speed, right_speed, block, phrase1_finish, speed_, speed_2, M4_3EM1_speed, different_speed, miss, left, right, click, miki
    encoder_motor_M1.set_speed((0 - speed))
    encoder_motor_M2.set_speed((0 - speed))
    encoder_motor_M4.set_speed(speed)
    encoder_motor_M3.set_speed(speed)

def auto_right_():
    global Position, press, Ranging_distance, Power, Power__, Turn_power, Turn_power__, Slide, Slide__, ps, _2, _3, Finish, d_ranging, base_speed, motor_speed, Max_speed, left_speed, right_speed, block, phrase1_finish, speed_, speed_2, M4_3EM1_speed, different_speed, miss, left, right, click, miki
    # DO SOMETHING
    pass

def auto_def_():
    global Position, press, Ranging_distance, Power, Power__, Turn_power, Turn_power__, Slide, Slide__, ps, _2, _3, Finish, d_ranging, base_speed, motor_speed, Max_speed, left_speed, right_speed, block, phrase1_finish, speed_, speed_2, M4_3EM1_speed, different_speed, miss, left, right, click, miki
    Slide2_N_right____left___(120)
    time.sleep(1)
    Forward2_N(-200)
    time.sleep(2)
    rotate_N_right____left___(-80)
    time.sleep(0.2)
    Forward2_N(70)
    time.sleep(0.1)
    Slide2_N_right____left___(120)
    time.sleep(0.5)
    _E0_B8_84_E0_B8_B5_E0_B8_9B_but_DC_N(-70)
    time.sleep(1)
    Forward2_N(-120)
    time.sleep(1)
    Stopdrivetrain()
    Stop_DC()
    Stop_loadball()

def GetMakeX_N(Startfrom):
    global Position, press, Ranging_distance, Power, Power__, Turn_power, Turn_power__, Slide, Slide__, ps, _2, _3, Finish, d_ranging, base_speed, motor_speed, Max_speed, left_speed, right_speed, block, phrase1_finish, speed_, speed_2, M4_3EM1_speed, different_speed, miss, left, right, click, miki
    # DO SOMETHING
    pass

def auto_blox_():
    global Position, press, Ranging_distance, Power, Power__, Turn_power, Turn_power__, Slide, Slide__, ps, _2, _3, Finish, d_ranging, base_speed, motor_speed, Max_speed, left_speed, right_speed, block, phrase1_finish, speed_, speed_2, M4_3EM1_speed, different_speed, miss, left, right, click, miki
    Loadball_N(1)
    Forward2_N(200)
    while not ranging_sensor_2.get_distance() < 30:
      # DO SOMETHING
      pass

    rotate_N_right____left___(90)
    time.sleep(1.5)
    _E0_B8_9B_E0_B8_B1_E0_B9_88_E0_B8_99_E0_B8_81_E0_B8_A5_E0_B9_88_E0_B8_AD_E0_B8_87()
    Forward2_N(-120)
    time.sleep(1)
    Slide2_N_right____left___(120)
    time.sleep(1.5)
    for i in range(4):
        encoder_motor_M2.set_speed(-120)
        encoder_motor_M3.set_speed(120)
        encoder_motor_M4.set_speed(-120)
        encoder_motor_M1.set_speed(90)
        time.sleep(3)
        if ranging_sensor_1.get_distance() < 9 and ranging_sensor_2.get_distance() < 9:
          Forward2_N(-70)
          time.sleep(0.3)
          rotate_N_right____left___(90)
          time.sleep(1.5)
          Slide2_N_right____left___(70)
          while not ranging_sensor_3.get_distance() < 9:
            # DO SOMETHING
            pass

        else:
          if ranging_sensor_1.get_distance() > 30 and ranging_sensor_2.get_distance() > 30:
            Slide2_N_right____left___(70)
            while not ranging_sensor_3.get_distance() < 9:
              # DO SOMETHING
              pass

    encoder_motor_M2.set_speed(120)
    encoder_motor_M3.set_speed(-90)
    encoder_motor_M4.set_speed(120)
    encoder_motor_M1.set_speed(-120)
    time.sleep(4)
    Stop_DC()
    Stop_loadball()
    Stopdrivetrain()

def rotate_N_right____left___(speed):
    global Position, press, Ranging_distance, Power, Power__, Turn_power, Turn_power__, Slide, Slide__, ps, _2, _3, Finish, d_ranging, base_speed, motor_speed, Max_speed, left_speed, right_speed, block, phrase1_finish, speed_, speed_2, M4_3EM1_speed, different_speed, miss, left, right, click, miki
    encoder_motor_M2.set_speed(speed)
    encoder_motor_M1.set_speed(speed)
    encoder_motor_M4.set_speed(speed)
    encoder_motor_M3.set_speed(speed)

def Loadball_N(Direction):
    global Position, press, Ranging_distance, Power, Power__, Turn_power, Turn_power__, Slide, Slide__, ps, _2, _3, Finish, d_ranging, base_speed, motor_speed, Max_speed, left_speed, right_speed, block, phrase1_finish, speed_, speed_2, M4_3EM1_speed, different_speed, miss, left, right, click, miki
    if Direction == 1:
      power_expand_board.set_power("DC2", 100)

    else:
      if Direction == -1:
        power_expand_board.set_power("DC2", -100)

def Forward_N_N(Degree, Speed):
    global Position, press, Ranging_distance, Power, Power__, Turn_power, Turn_power__, Slide, Slide__, ps, _2, _3, Finish, d_ranging, base_speed, motor_speed, Max_speed, left_speed, right_speed, block, phrase1_finish, speed_, speed_2, M4_3EM1_speed, different_speed, miss, left, right, click, miki
    encoder_motor_M2.move((0 - Degree), Speed)
    encoder_motor_M4.move((0 - Degree), Speed)
    encoder_motor_M1.move(Degree, Speed)
    encoder_motor_M3.move(Degree, Speed)

def Shoot():
    global Position, press, Ranging_distance, Power, Power__, Turn_power, Turn_power__, Slide, Slide__, ps, _2, _3, Finish, d_ranging, base_speed, motor_speed, Max_speed, left_speed, right_speed, block, phrase1_finish, speed_, speed_2, M4_3EM1_speed, different_speed, miss, left, right, click, miki
    power_expand_board.set_power("DC3", -80)

def brushless_N_N(level, power):
    global Position, press, Ranging_distance, Power, Power__, Turn_power, Turn_power__, Slide, Slide__, ps, _2, _3, Finish, d_ranging, base_speed, motor_speed, Max_speed, left_speed, right_speed, block, phrase1_finish, speed_, speed_2, M4_3EM1_speed, different_speed, miss, left, right, click, miki
    if power < 100 or power == 100:
      smartservo_2.move_to(level, 30)
      power_expand_board.set_power("BL1", power)
      power_expand_board.set_power("BL2", power)

def _E0_B8_9B_E0_B8_B1_E0_B9_88_E0_B8_99_E0_B8_81_E0_B8_A5_E0_B9_88_E0_B8_AD_E0_B8_87():
    global Position, press, Ranging_distance, Power, Power__, Turn_power, Turn_power__, Slide, Slide__, ps, _2, _3, Finish, d_ranging, base_speed, motor_speed, Max_speed, left_speed, right_speed, block, phrase1_finish, speed_, speed_2, M4_3EM1_speed, different_speed, miss, left, right, click, miki
    encoder_motor_M5.set_power(200)
    encoder_motor_M6.set_power(-200)

def _E0_B8_84_E0_B8_B5_E0_B8_9B_but_DC_N(speed):
    global Position, press, Ranging_distance, Power, Power__, Turn_power, Turn_power__, Slide, Slide__, ps, _2, _3, Finish, d_ranging, base_speed, motor_speed, Max_speed, left_speed, right_speed, block, phrase1_finish, speed_, speed_2, M4_3EM1_speed, different_speed, miss, left, right, click, miki
    power_expand_board.set_power("DC6", speed)

left = 1
right = -1
smart_camera_1.set_mode("color")
phrase1_finish = 0
if power_manage_module.is_auto_mode():
  auto_def_()

else:
  while True:
      time.sleep(0.001)
      Manual()

