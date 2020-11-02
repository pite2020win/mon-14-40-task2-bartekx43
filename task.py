#
#Flight simulator. 
#Write a code in python that simulates the tilt correction of the plane (angle between plane wings and earth). 
#The program should print out current orientation, and applied tilt correction.
# (Tilt is "Roll" in this diagram https://www.novatel.com/assets/Web-Phase-2-2012/Solution-Pages/AttitudePlane.png)
#The program should run in infinite loop, until user breaks the loop.
#Assume that plane orientation in every new simulation step is changing with random angle with gaussian distribution (the planes is experiencing "turbuence"). 
# Hint: "random.gauss(0, 2*rate_of_correction)"
#With every simulation step the orentation should be corrected, correction should be applied and printed out.
#Try to expand your implementation as best as you can. 
#Think of as many features as you can, and try implementing them.
#
#Try to expand your implementation as best as you can. 
#Think of as many features as you can, and try implementing them.
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)
#Delete these comments before commit!
#
#Good luck.
import random

class Airplane:
  def __init__(self, roll, pitch, yaw):
    self.expected_roll = roll
    self.expected_pitch = pitch
    self.expected_yaw = yaw
    self.roll = roll
    self.pitch = pitch
    self.yaw = yaw

  def update_parameters (self, d_roll, d_pitch, d_yaw):
    self.roll += d_roll
    self.pitch += d_pitch
    self.yaw += d_yaw

  def correct_parameters (self, rate_of_correction):
    self.roll -= rate_of_correction*(self.expected_roll-self.roll)
    self.pitch -= rate_of_correction*(self.expected_pitch-self.pitch)
    self.yaw -= rate_of_correction*(self.expected_yaw-self.yaw)
    

airplane = Airplane(0, 0, 0)

while True:
  roll_turbulance = random.random()
  pitch_turbulance = random.random()
  yaw_turbulance = random.random()

  airplane.update_parameters(roll_turbulance, pitch_turbulance, yaw_turbulance)
  print("Current parameters:\nroll: {} (expected: {})\npitch: {} (expected: {})\nyaw: {} (expected: {})\n".format(
    airplane.roll, airplane.expected_roll, airplane.pitch, airplane.expected_pitch, airplane.yaw, airplane.expected_yaw
  ))

  rate_of_correction = random.random()
  airplane.correct_parameters(rate_of_correction)
  print ("Correction done\n")

  if (airplane.pitch > 5):
    print ("Plane crashed")
    break

  
  
    


    

