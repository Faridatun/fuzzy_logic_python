import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# The universe of variables and membership functions
Xaxis = ctrl.Antecedent(np.arange(-3.5, 7.5, 0.2), 'Xaxis')
Yaxis = ctrl.Antecedent(np.arange(-10.5, 15.5, 0.2), 'Yaxis')
Zaxis = ctrl.Antecedent(np.arange(-15.5, 20.5, 0.2), 'Zaxis')
BrakeLevel = ctrl.Consequent(np.arange(-0.05, 1.05, 0.2), 'BrakeLevel')

# Rules

Xaxis['HardBrake'] = fuzz.trapmf(Xaxis.universe, [-3, -3, -0.5, 1])
Xaxis['NoBrake'] = fuzz.trimf(Xaxis.universe, [-0.5, 1.5, 3.5])
Xaxis['Brake'] = fuzz.trapmf(Xaxis.universe, [2.5, 4, 11.5, 12])

Yaxis['HardBrake'] = fuzz.trapmf(Yaxis.universe, [-10, -10, 3.5, 6.5])
Yaxis['Brake'] = fuzz.trimf(Yaxis.universe, [5, 7.5, 10])
Yaxis['NoBrake'] = fuzz.trapmf(Yaxis.universe, [8.5, 11, 15, 25])

Zaxis['Brake'] = fuzz.trapmf(Zaxis.universe, [-15, -15, 4, 9])
Zaxis['NoBrake'] = fuzz.trimf(Zaxis.universe, [5, 11.5, 18])
Zaxis['HardBrake'] = fuzz.trapmf(Zaxis.universe, [12, 16, 20, 30])

BrakeLevel['NoBrake'] = fuzz.trapmf(BrakeLevel.universe, [0, 0, 0.2, 0.4])
BrakeLevel['Brake'] = fuzz.trimf(BrakeLevel.universe, [0.3, 0.5, 0.7])
BrakeLevel['HardBrake'] = fuzz.trapmf(BrakeLevel.universe, [0.6, 0.8, 1, 1])

Xaxis.view()
Yaxis.view()
Zaxis.view()
BrakeLevel.view()

#The Rules
rule1 = ctrl.Rule(Xaxis['HardBrake'] & Yaxis['HardBrake'] & Zaxis['Brake'], BrakeLevel['HardBrake'])
rule2 = ctrl.Rule(Xaxis['HardBrake'] & Yaxis['HardBrake'] & Zaxis['NoBrake'], BrakeLevel['HardBrake'])
rule3 = ctrl.Rule(Xaxis['HardBrake'] & Yaxis['HardBrake'] & Zaxis['HardBrake'], BrakeLevel['HardBrake'])
rule4 = ctrl.Rule(Xaxis['HardBrake'] & Yaxis['Brake'] & Zaxis['Brake'], BrakeLevel['Brake'])
rule5 = ctrl.Rule(Xaxis['HardBrake'] & Yaxis['Brake'] & Zaxis['NoBrake'], BrakeLevel['Brake'])
rule6 = ctrl.Rule(Xaxis['HardBrake'] & Yaxis['Brake'] & Zaxis['HardBrake'], BrakeLevel['Brake'])
rule7 = ctrl.Rule(Xaxis['HardBrake'] & Yaxis['NoBrake'] & Zaxis['Brake'], BrakeLevel['NoBrake'])
rule8 = ctrl.Rule(Xaxis['HardBrake'] & Yaxis['NoBrake'] & Zaxis['NoBrake'], BrakeLevel['NoBrake'])
rule9 = ctrl.Rule(Xaxis['HardBrake'] & Yaxis['NoBrake'] & Zaxis['HardBrake'], BrakeLevel['NoBrake'])

rule10 = ctrl.Rule(Xaxis['Brake'] & Yaxis['HardBrake'] & Zaxis['Brake'], BrakeLevel['HardBrake'])
rule11 = ctrl.Rule(Xaxis['Brake'] & Yaxis['HardBrake'] & Zaxis['NoBrake'], BrakeLevel['HardBrake'])
rule12 = ctrl.Rule(Xaxis['Brake'] & Yaxis['HardBrake'] & Zaxis['HardBrake'], BrakeLevel['HardBrake'])
rule13 = ctrl.Rule(Xaxis['Brake'] & Yaxis['Brake'] & Zaxis['Brake'], BrakeLevel['Brake'])
rule14 = ctrl.Rule(Xaxis['Brake'] & Yaxis['Brake'] & Zaxis['NoBrake'], BrakeLevel['Brake'])
rule15 = ctrl.Rule(Xaxis['Brake'] & Yaxis['Brake'] & Zaxis['HardBrake'], BrakeLevel['Brake'])
rule16 = ctrl.Rule(Xaxis['Brake'] & Yaxis['NoBrake'] & Zaxis['Brake'], BrakeLevel['NoBrake'])
rule17 = ctrl.Rule(Xaxis['Brake'] & Yaxis['NoBrake'] & Zaxis['NoBrake'], BrakeLevel['NoBrake'])
rule18 = ctrl.Rule(Xaxis['Brake'] & Yaxis['NoBrake'] & Zaxis['HardBrake'], BrakeLevel['NoBrake'])

rule19 = ctrl.Rule(Xaxis['NoBrake'] & Yaxis['HardBrake'] & Zaxis['Brake'], BrakeLevel['HardBrake'])
rule20 = ctrl.Rule(Xaxis['NoBrake'] & Yaxis['HardBrake'] & Zaxis['NoBrake'], BrakeLevel['HardBrake'])
rule21 = ctrl.Rule(Xaxis['NoBrake'] & Yaxis['HardBrake'] & Zaxis['HardBrake'], BrakeLevel['HardBrake'])
rule22 = ctrl.Rule(Xaxis['NoBrake'] & Yaxis['Brake'] & Zaxis['Brake'], BrakeLevel['Brake'])
rule23 = ctrl.Rule(Xaxis['NoBrake'] & Yaxis['Brake'] & Zaxis['NoBrake'], BrakeLevel['Brake'])
rule24 = ctrl.Rule(Xaxis['NoBrake'] & Yaxis['Brake'] & Zaxis['HardBrake'], BrakeLevel['Brake'])
rule25 = ctrl.Rule(Xaxis['NoBrake'] & Yaxis['NoBrake'] & Zaxis['Brake'], BrakeLevel['NoBrake'])
rule26 = ctrl.Rule(Xaxis['NoBrake'] & Yaxis['NoBrake'] & Zaxis['NoBrake'], BrakeLevel['NoBrake'])
rule27 = ctrl.Rule(Xaxis['NoBrake'] & Yaxis['NoBrake'] & Zaxis['HardBrake'], BrakeLevel['NoBrake'])

brake_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18,
     rule19, rule20, rule21, rule22, rule23, rule24, rule25, rule26, rule27])

#simulation
braking = ctrl.ControlSystemSimulation(brake_ctrl)
#example
braking.input['Xaxis'] = 0.344213415
braking.input['Yaxis'] = 4.36003659
braking.input['Zaxis'] = 10.8235996

braking.compute()

print(braking.output['BrakeLevel'])

BrakeLevel.view(sim=braking)

plt.show()
