ip_address = 'localhost' # Enter your IP Address here
project_identifier = 'P2B' # Enter the project identifier i.e. P2A or P2B
#--------------------------------------------------------------------------------
import sys
sys.path.append('../')
from Common.simulation_project_library import *

hardware = False
QLabs = configure_environment(project_identifier, ip_address, hardware).QLabs
arm = qarm(project_identifier,ip_address,QLabs,hardware)
potentiometer = potentiometer_interface()
#--------------------------------------------------------------------------------
# STUDENT CODE BEGINS
#---------------------------------------------------------------------------------
def pickup():
    arm.rotate_base(5)
    time.sleep(2)
    arm.rotate_elbow(-14)
    time.sleep(2)
    arm.rotate_shoulder(57)
    time.sleep(2)
    arm.control_gripper(45)
    time.sleep(2)
    arm.rotate_shoulder(-57)
    time.sleep(2)
    arm.rotate_elbow(14)
    time.sleep(1)
    arm.rotate_base(-5)

def drop_off():
    arm.activate_autoclaves()
    if potentiometer.left()== 0.20 and potentiometer.right() == 0.95:
        time.sleep(1)
        arm.rotate_elbow(-25)
        time.sleep(2)
        arm.rotate_shoulder(47)
        time.sleep(2)
        arm.control_gripper(-45)
        time.sleep(2)
        arm.rotate_shoulder(-47)
        arm.rotate_elbow(20)
        arm.home()

    elif potentiometer.left()== 0.20 and potentiometer.right() != 0.95:
        time.sleep(1)
        arm.rotate_elbow(-20)
        time.sleep(2)
        arm.rotate_shoulder(42)
        time.sleep(2)
        arm.control_gripper(-45)
        time.sleep(2)
        arm.rotate_shoulder(-42)
        arm.rotate_elbow(20)
        arm.home()
    elif potentiometer.left()== 0.6:
        arm.open_autoclave("red")
        arm.rotate_shoulder(-25)
        time.sleep(1)
        arm.rotate_elbow(25)
        time.sleep(1)
        arm.rotate_shoulder(45)
        time.sleep(1)
        arm.control_gripper(-45)
        time.sleep(1)
        arm.rotate_shoulder(-10)
        time.sleep(2)
        arm.home()

        arm.open_autoclave("red",False)
    elif potentiometer.left() == 0.8:
        arm.open_autoclave("green")
        arm.rotate_shoulder(-25)
        time.sleep(1)
        arm.rotate_elbow(25)
        time.sleep(1)
        arm.rotate_shoulder(45)
        time.sleep(1)
        arm.control_gripper(-45)
        time.sleep(1)
        arm.rotate_shoulder(-10)
        time.sleep(2)
        arm.open_autoclave("green",False)
        arm.home()
    elif potentiometer.left() == 1.0:
        arm.open_autoclave("blue")
        arm.rotate_shoulder(-25)
        time.sleep(1)
        arm.rotate_elbow(20)
        time.sleep(1)
        arm.rotate_shoulder(50)
        time.sleep(1)
        arm.control_gripper(-45)
        time.sleep(1)
        arm.rotate_shoulder(-10)
        time.sleep(2)
        arm.open_autoclave("blue",False)
        arm.home()

    arm.deactivate_autoclaves()

def rotate_base():
    old_angle = 0.5
    while True:
        new_angle = potentiometer.right()
        angle = new_angle - old_angle
        angle = angle*350
        arm.rotate_base(angle)
        old_angle = new_angle
        if potentiometer.left() == 0.20:
            drop_off()
            break
        elif potentiometer.left() == 0.6 and potentiometer.right()== 0.25:
            drop_off()
            break
        elif potentiometer.left() == 0.8 and potentiometer.right()== 0.75:
            drop_off()
            break
        elif potentiometer.left() == 1.0 and potentiometer.right()== 0.95:
            drop_off()
            break

def main():
    import random
    container_ids_used = []
    while True:
        if potentiometer.left() == 0.5 and potentiometer.right() == 0.5:
            container_ids = random.randint(1,6)
            if container_ids not in container_ids_used:
                container_ids_used.append(container_ids)
                arm.spawn_cage(container_ids)
                time.sleep(1)
                pickup()
                time.sleep(1)
                rotate_base()
            elif len(container_ids_used) == 6:
                break

    print("The program has ended")
                
    
        













#---------------------------------------------------------------------------------
# STUDENT CODE ENDS
#---------------------------------------------------------------------------------
    

    

