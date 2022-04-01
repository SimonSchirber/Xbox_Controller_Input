# Xbox_Controller_Input
This is meant to be able to check all inputs of the Xbox series X and Xbox series S controller using python and pygame. It can be used to control various systems as desired.

How to use:
Connect your xbox controller via bluetooth. As you press each button there should be the correct button and joystick movents accordingly.

Installations:
pip install pygame


# Joystick Filtering Notes
I did add filtering to make sure the averaged last three values are in the correct direction for the joysticks, as I observed a lot of jitter in the positional arguments for my joytick. I had a total of eight possible directions to detect for each joystick (up, up-left, left, down-left, down, down-right, right, up-right).

# Joystick Chart From my observations
As you can see below from my observations, each joystick appears to have two "buttons" assciated with it that would seemingly randomly trigger. The value for each "button" I found were oriented diffrently, and one button had a range from 1 to -1 and as my diagram shows each value means it could be in one of two places if you have only one buttons information. If you have both buttons value you can deduce only one possible direction, so I set a range using these orientations as shown below for eight directions. You will note this does not associate any value for intensity of the joystick movement.

![Test Image 1](/joystick_diagram/joystick.jpg)

## Need to Do
- Add relative strength of joystick direction (currently only have the relative direction, I did not determine the strength and direction based on the charts I made)
- Add relative strength of triggers (currently only binary)
- Update Joystick chart: Please if anyone has a better understanding please comment and let me know 


