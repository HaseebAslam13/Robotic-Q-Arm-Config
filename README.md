


# 🤖 Autonomous Robotic Arm Control  

A Python-based project for controlling a robotic arm (connected via Raspberry Pi) to perform tasks like picking up objects, identifying target locations, and placing them in designated zones using potentiometer input.  

---

## 🛠️ **Key Features**  
- **Object Pickup**: Automates object grabbing using pre-defined arm movements.  
- **Smart Drop-Off**: Uses potentiometers to identify zones for object placement.  
- **Dynamic Base Rotation**: Adjusts the arm's base based on real-time potentiometer feedback.  
- **Randomized Workflow**: Ensures all containers are used before program termination.
<div>
  <img src = "https://github.com/user-attachments/assets/f6951ff1-812f-4d93-9c52-6224d64123d1" width = "500" height = "200"/>
  <div><strong>Figure 1:</strong> Quansar Simulation</div>
</div>

---

## 🚀 **How to Use**  
1. **Set IP and Project Identifier**:  
   Update the following variables in the script:  
   ```python
   ip_address = 'localhost'  # Enter your IP Address here
