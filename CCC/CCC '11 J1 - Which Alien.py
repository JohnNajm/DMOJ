"""
Canadian Computing Competition: 2011 Stage 1, Junior #1

Canada Cosmos Control has received a report of another incident. They believe that an alien has illegally entered our space. A person who witnessed the appearance of the alien has come forward to describe the alien's appearance. It is your role within the CCC to determine which alien has arrived. There are only 3 alien species that we are aware of, described below:

    TroyMartian, who has at least 3(x>=3) antennae and at most 4 eyes(x<=4);
    VladSaturnian, who has at most 6 antennae and at least 2 eyes;
    GraemeMercurian, who has at most 2 antennae and at most 3 eyes.

Input Specification

The first line will contain the number of antennae that the witness claimed to have seen on the alien.

The second line will contain the number of eyes seen on the alien.
Output Specification

The output will be the list of aliens who match the possible description given by the witness. If no aliens match the description, there is no output.
"""

myList = [int(input()), int(input())]

if myList[0] >= 3 and myList[1] <= 4:
    print("TroyMartian")

if myList[0] <= 6 and myList[1] >= 2:
    print("VladSaturnian")

if myList[0] <= 2 and myList[1] <= 3:
    print("GraemeMercurian")
