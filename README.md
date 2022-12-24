# Cellular-Automata
This is a framework for running cellular automata built in python. 

A Cellular Automata is a (typically infinite) grid of cells. Each cell has a state from a set of possible states. Once initialized, the cellular automata iterates,
with the next state of each cell at each iteration being determined by a set of rules, typically based on the current state of the cell and the cells around it.

This should work with any simple (two dimensional, values of 1 or 0) cellular automata.
The script allows you to pass an outside function in to the cellular automata to be used when iterating. This is useful for creating/testing many different cellular
automata. The function need only accept x and y coordinates, as well as the current cellular automata object, and return the next state for that cell.

The following files are included:
1. **cellular_automata_framework.py** - This is the cellular automata class. Create a new cellular automata by creating a new instance of this class. Call the iterate function to iterate it.
2. **cellularAutomata_Functions.py** - This is a collection of rule set functions that I created, as well as the most famous rule set, Conway's Game of Life.
3. **cellularAutomata_Driver.py** - This is a script I created for running and testing different cellular automata. In the script are functions for creating initial boars for the automata, saving the board to a text file, saving the board and related information to a JSON file, displaying the board, and taking a screenshot of the display. 

CellularAutomata_driver.py utilizes my noise_squirrel5 package which can be found here: https://github.com/FiniteUI/Squirrel-Noise-5

I initially was playing around with them as a way to procedurally generate terrain for video games, and tested out over 200 functions. Most of the functions I tested
were created randomly with by looking at different possibilites for a few different parameters. It is very difficult to tell how the automata will actually act from
the ruleset, so I followed the mindset of creating a ton of them without much thought and seeing how they played out. Below are some of the more interesting results. 
The functions for these are the titles displayed at the top of the grid, and can be found in the **cellularAutomata_functions.py** script:

This function generates a maze like structure:

![conway_modified_3_4137997834_2022-12-22-01-26-05](https://user-images.githubusercontent.com/33558498/209419883-bc6314b4-f69d-4732-95f7-f4fd0169dc87.png)

These functions generate splotchy, discrete masses. These could be useful for terrain generation for forests, rocks, hills, water, etc.:

![conway_modified_11_1190056815_2022-12-22-11-40-57](https://user-images.githubusercontent.com/33558498/209419925-a581396f-8031-41f9-9382-f5119fbcf96c.png)
![conway_modified_12_4137997834_2022-12-22-01-27-10](https://user-images.githubusercontent.com/33558498/209419904-8b78a924-2ad8-44e9-8bbb-8fff37e34f92.png)
![conway_modified_13_4137997834_2022-12-22-01-27-23](https://user-images.githubusercontent.com/33558498/209419905-4bae1b1d-c100-4e8c-9452-d8418a74f38c.png)
![conway_modified_14_1190056815_2022-12-22-11-41-45](https://user-images.githubusercontent.com/33558498/209419906-1444ede2-eb7b-4f41-8e8e-dc0562b2288d.png)
![conway_modified_15_4137997834_2022-12-22-01-27-57](https://user-images.githubusercontent.com/33558498/209419907-8db62ad6-5c5c-4a8f-a6a9-e371df5a0285.png)
![custom_34_4137997834_2022-12-22-01-35-18](https://user-images.githubusercontent.com/33558498/209419908-4130e1e7-b701-425c-8416-1183a8091be9.png)
![custom_192_3861191076_2022-12-22-19-08-49](https://user-images.githubusercontent.com/33558498/209419910-65b73213-f6ab-448b-90be-d134887f506b.png)
![custom_174_3809185859_2022-12-22-16-58-51](https://user-images.githubusercontent.com/33558498/209420420-5103e837-ed98-4748-97d6-b3772fc97c4a.png)
![custom_191_2536668112_2022-12-22-17-02-19](https://user-images.githubusercontent.com/33558498/209420421-76e75534-8dae-4eb4-8283-20df5e521513.png)

These functions generates paths:

![custom_48_1190056815_2022-12-22-11-55-05](https://user-images.githubusercontent.com/33558498/209419945-579b43e8-4f00-45d7-87f2-7a6309a94cf3.png)
![custom_49_1190056815_2022-12-22-11-55-37](https://user-images.githubusercontent.com/33558498/209419946-074a5869-e3f2-44ef-b4d0-8e9e1cf4f427.png)
![custom_52_1190056815_2022-12-22-11-57-17](https://user-images.githubusercontent.com/33558498/209419947-e35789d5-37d0-433a-a060-33afb961bc7f.png)
![custom_55_1190056815_2022-12-22-11-58-12](https://user-images.githubusercontent.com/33558498/209419948-0ce24841-be0b-44ca-b264-5d1ed6e52f7d.png)
![custom_71_1190056815_2022-12-22-12-00-54](https://user-images.githubusercontent.com/33558498/209419949-9f971735-3c0e-491a-b2a5-6c823b51ef2d.png)
![custom_36_4137997834_2022-12-22-01-35-49](https://user-images.githubusercontent.com/33558498/209419950-8a3158b4-426d-458f-bd4b-3e4a1cf2879c.png)
![custom_37_1190056815_2022-12-22-11-50-47](https://user-images.githubusercontent.com/33558498/209419951-3e77c75f-ae12-402a-8a65-ae20e11d76da.png)
![custom_38_4137997834_2022-12-22-01-36-57](https://user-images.githubusercontent.com/33558498/209419952-81ffcbb4-91c7-4b10-b867-1de02fb51fc3.png)
![custom_44_1190056815_2022-12-22-11-53-03](https://user-images.githubusercontent.com/33558498/209419953-7565dee4-e1c4-4d5b-b74d-9fa72024a3b3.png)

These functions generate large blocky areas:

![custom_46_1190056815_2022-12-22-11-54-28](https://user-images.githubusercontent.com/33558498/209419961-f1cb5419-250f-4516-b6f0-35570dea9647.png)
![custom_51_1190056815_2022-12-22-11-56-43](https://user-images.githubusercontent.com/33558498/209419962-d9c7b4c5-81fa-4851-85f3-f04e4fa51598.png)
![custom_45_1190056815_2022-12-22-11-53-45](https://user-images.githubusercontent.com/33558498/209419963-a950abe7-75d5-4ebb-bc29-a3e8756901a3.png)

These functions generate competing sections of vertical and horizontal lines:

![custom_81_1190056815_2022-12-22-12-01-52](https://user-images.githubusercontent.com/33558498/209419972-8cf404b2-8005-46e3-8303-a13cb0167077.png)
![custom_89_1190056815_2022-12-22-12-03-01](https://user-images.githubusercontent.com/33558498/209419973-9a2f2753-eff9-4788-86df-444891bb69be.png)
![custom_216_114828706_2022-12-22-21-53-39](https://user-images.githubusercontent.com/33558498/209419974-b3e411a4-8c34-4b6d-85dd-ebf1ba6342c0.png)
![custom_217_114828706_2022-12-22-21-54-28](https://user-images.githubusercontent.com/33558498/209419975-bb3a615c-1747-4ed5-b3cc-7c75f9ba7be0.png)
![custom_221_114828706_2022-12-22-21-55-43](https://user-images.githubusercontent.com/33558498/209419976-5de1f2dd-c069-4d54-8cd2-a62a46382b3f.png)

These functions generate piles of "snakes":

![custom_202_1435913884_2022-12-22-21-24-38](https://user-images.githubusercontent.com/33558498/209420030-613610f0-6554-446d-8a89-cb3a94d770e5.png)
![custom_203_1435913884_2022-12-22-21-25-19](https://user-images.githubusercontent.com/33558498/209420031-77dd9c4b-85fd-43c2-91ce-69848bfeaee8.png)
![custom_204_3537409248_2022-12-22-19-11-35](https://user-images.githubusercontent.com/33558498/209420032-8f8bb260-78d1-4bd2-a5bc-5941412ab56d.png)

This function generates some discrete areas with a distinct pattern:

![custom_220_114828706_2022-12-22-21-55-06](https://user-images.githubusercontent.com/33558498/209420057-baf3fb41-19e3-4309-82dd-cead85e73014.png)

These functions devolve into small cycling blocks:

![custom_225_549904416_2022-12-22-22-03-36](https://user-images.githubusercontent.com/33558498/209420071-09e846de-1786-4867-a9e0-af67e0dd92c8.png)

And here's a few more slightly less interesting ones for good measure:

![custom_171_3442291744_2022-12-22-14-40-28](https://user-images.githubusercontent.com/33558498/209420158-7b5a9b1e-ef8c-4529-be18-2c4b5be27a2a.png)
![custom_229_13505776_2022-12-22-22-05-51](https://user-images.githubusercontent.com/33558498/209420159-d021fa0e-8f99-49d9-804b-593c7b1f4e16.png)
![fourDirections_threeOrMore_1190056815_2022-12-22-11-38-48](https://user-images.githubusercontent.com/33558498/209420160-579264ff-ead0-4850-8690-4e491c02db1a.png)
![custom_10_1190056815_2022-12-22-11-46-45](https://user-images.githubusercontent.com/33558498/209420161-728d5780-b7e7-474a-a0fb-827667f5ba53.png)
![custom_165_3442291744_2022-12-22-14-36-46](https://user-images.githubusercontent.com/33558498/209420162-91b59235-75f4-47f7-be87-9c6000f5f114.png)
![custom_207_1435913884_2022-12-22-21-27-33](https://user-images.githubusercontent.com/33558498/209420291-6322f23f-bad3-47ba-ade4-1b9d277722de.png)
![custom_208_1513686562_2022-12-22-21-47-22](https://user-images.githubusercontent.com/33558498/209420292-c16ebd96-3fb4-4faa-af07-cd9af739963a.png)
![custom_73_1190056815_2022-12-22-12-01-05](https://user-images.githubusercontent.com/33558498/209420437-67a93a21-9e79-4095-9af5-98c4facfc2ab.png)
![custom_75_1190056815_2022-12-22-12-01-09](https://user-images.githubusercontent.com/33558498/209420443-7d2c5c4c-7b35-47b6-bb07-e8d184888ede.png)
![custom_65_1190056815_2022-12-22-11-59-06](https://user-images.githubusercontent.com/33558498/209420460-d41729db-23d9-4047-8261-b0d629c3006c.png)
![custom_53_1190056815_2022-12-22-11-57-28](https://user-images.githubusercontent.com/33558498/209420466-8c49af21-c91e-4007-a1ab-73f26396b7b1.png)

Apart from these, many of them end up in uninteresting cycles or blank voids of black or white. However, while some of them don't produce interesting end points,
many of them actually display interesting movement patters that the screenshots/endpoints don't reflect. Also, I am using a 100 by 100 grid, running them for 100
iterations, and giving completely randomized input. It is very possible that changes in grid size could produce different results. It's also possible that different
types of input (different densities, patterns, etc) could produce different results. Lastly, while some of them terminate in empty grids or simple cycles, they may
show interesting patters earlier in their iterations. Ones that do not terminate but don't show interesting results, may show better results if ran for more iterations.

I will be working on more in the future, utilizing new parameters and different combinations of existing parameters.
