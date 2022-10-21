# python-project

This is an outline for my python project.

This programme takes multiple inputs from the user concerning details about a swimming event. They have three options for what they can do.
[1] They can calculate their average pace.
[2] They can check if they qualify for their future competition.
[3] They can convert their time to either a 25m or 50m time.

[1] Is performed by calculating the number of lengths in their event: distance/25, then we divide the time by the number of lengths.
[2] Calculates the difference between their time and qualifying time. A decision as to whether or not they're qualified is determined by whether this difference is above or below zero. A different message it outputted depending on the outcome.
[3] The user inputs whether the time they entered was achieved in a 25m or 50m pool. Depending on this, the time will either be multiplied by 1.04 (25m --> 50m) or divided by 1.04 (50m --> 25m).

Future developments:

Add in an additional while loop or functionality so that the user has the option to revisit options i.e. convert time before entering a new event.
