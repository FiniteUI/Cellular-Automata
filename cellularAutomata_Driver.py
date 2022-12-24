import cellular_automata_framework
import noise_squirrel5
import random
import os
from pathlib import Path
import time
import tkinter
import datetime
import json
from PIL import ImageGrab
from cellularAutomota_Functions import *

def getNewNoiseGenerator(seed):
    #use the passed seed to create a new noise instance with a new seed
    print(f'Initial Seed: {seed}')
    ns = noise_squirrel5.noise_squirrel5(seed)
    return ns

def getNewNoiseGeneratorRandomSeed():
    seed = random.randint(0x00000000, 0xFFFFFFFF)
    ns = getNewNoiseGenerator(seed)
    return ns, seed

def noiseBoard(width, height):
    #generate a random layout
    n, seed = getNewNoiseGeneratorRandomSeed()

    layout = [[0 for x in range(0, width)] for y in range(0, height)]
    for i in range(0, height):
        for x in range(0, width):
            flip = n.noiseBool2d(i, x)
            if flip:
                layout[i][x] = 1
        
    return layout, seed

def checkerBoard(width, height):
    layout = [[0 for x in range(0, width)] for y in range(0, height)]
    
    next = True
    for i in range(0, len(layout)):
        for j in range(0, len(layout[i])):
            if next:
                layout[i][j] = 1
            next = not next
        
        if layout[i][0] == 1:
            next = False
        else:
            next = True

    return layout

def blankBoard(width, height):
    layout = [[0 for x in range(0, width)] for y in range(0, height)]
    return layout

def saveImage(window, algorithm, seed=-1):
    base = Path(os.path.realpath(__file__)).parent
    path = os.path.join(base, "Data", "Images")
    if not os.path.isdir(path):
        os.makedirs(path)

    date = datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d-%H-%M-%S")

    path = os.path.join(path, f"{algorithm.__name__}_{seed}_{date}.png")

    ImageGrab.grab(bbox=(
        window.winfo_x(),
        window.winfo_y(),
        (window.winfo_x() + window.winfo_width()) * 1.01,
        (window.winfo_y() + window.winfo_height()) * 1.04
    )).save(path)

    return path

def saveBoardTextFile(cellular_automata, algorithm, seed, iterations):
    contents = cellular_automata.getPrintableBoardString()

    base = Path(os.path.realpath(__file__)).parent
    path = os.path.join(base, "Data", "Text Files")
    if not os.path.isdir(path):
        os.makedirs(path)

    path = os.path.join(path, f"{algorithm.__name__}_{seed}_{iterations}.txt")
    with open(path, 'w+') as f:
        f.write(contents)

def getCellularAutomataJSON(ca, seed, iterations, image_path = ''):
    l = {
        'algorithm': ca.function.__name__,
        'seed': seed,
        'width': ca.width,
        'height': ca.height,
        'wraparound': ca.wraparound,
        'boundary': ca.boundary,
        'terminated': ca.terminated,
        'iterations': iterations,
        'iteration': ca.iteration,
        'cycling': ca.cycling,
        'cycle': ca.cycle,
        'image': image_path,
        'previous_states': ca.previous_states,
        'input': ca.input,
        'generation_date': datetime.datetime.now(),
        'board': ca.board,
        'printable_board': ca.getPrintableBoardString()
    }

    l = json.dumps(l, default=str)
    return l

def saveCellularAutomataJSON(ca, seed, iterations, image_path = ''):
    contents = getCellularAutomataJSON(ca, seed, iterations, image_path)

    base = Path(os.path.realpath(__file__)).parent
    path = os.path.join(base, "Data", "JSON")
    if not os.path.isdir(path):
        os.makedirs(path)

    path = os.path.join(path, f"{ca.function.__name__}_wraparound-{ca.wraparound}_{seed}_{iterations}.json")
    with open(path, 'w+') as f:
        f.write(contents)

def drawOnce(board, width, height, scale = 1):
    #load window
    window = tkinter.Tk()

    window.title('Map Layout Generation')
    window.geometry(f'{width * scale}x{height * scale}')

    #canvas to draw layout
    canvas = tkinter.Canvas(height=height * scale, width=width * scale, bg="white")
    canvas.pack()

    #draw and display map
    canvas.delete('all')

    for i in range(len(board)):
        for j in range(len(board[i])):
            x = j * scale
            y = i * scale
            if board[i][j] == 1:
                #canvas.create_rectangle(x, y, x, y, fill = 'black')
                canvas.create_rectangle(x, y, x + scale - 1, y + scale - 1, fill = 'black')

    window.update()

    time.sleep(0.5)

    window.destroy()

def drawConsistent(ca, width, height, scale = 1, window=None, canvas = None, title = 'Cellular Automata Visualizer', delay = 0):
    if window == None:
        #load window
        window = tkinter.Tk()

        window.title(title)
        window.geometry(f'{width * scale}x{height * scale}')

        #canvas to draw layout
        if canvas == None:
            canvas = tkinter.Canvas(height=height * scale, width=width * scale, bg="white")
            canvas.pack()

    #draw and display map
    canvas.delete('all')

    for i in range(ca.height):
        for j in range(ca.width):
            x = j * scale
            y = i * scale
            if ca.getCell(j, i) == 1:
                canvas.create_rectangle(x, y, x + scale - 1, y + scale - 1, fill = 'black')

            '''
            pixel = canvas.find_overlapping(x, y, x, y)
            if ca.getCell(j, i) == 1:
                if pixel == ():
                    canvas.create_rectangle(x, y, x + scale - 1, y + scale - 1, fill = 'black')
            else:
                if pixel != ():
                    canvas.delete(pixel)
            '''

    window.update()

    if delay > 0:
        time.sleep(delay)

    return window, canvas

def closeDrawing(window):
    window.destroy()

def runAutomata(width, height, iterations, algorithm, drawBoard=False, saveBoard=False, printBoard=False, board=None, seed=None, wraparound = False, delay = 0, history = False, check_history = False, save_image = False):
    print(f"Running {algorithm.__name__} cellular automata for {iterations} iterations...")

    if board == None:
        board, seed = noiseBoard(width, height)

    c = cellular_automata_framework.cellular_automata(width, height, algorithm, board, wraparound = wraparound, history=history, check_history=check_history)

    if printBoard:
        c.printBoard()
    
    if drawBoard:
        window, canvas = drawConsistent(c, width, height, 5, title = algorithm.__name__, delay=delay)

    for i in range(0, iterations):
        if c.isComplete():
            break

        c.iterate()

        if drawBoard:
            window, canvas = drawConsistent(c, width, height, 5, window, canvas, delay = delay)

        if printBoard:
            c.printBoard()
    
    if save_image:
        image = saveImage(window, algorithm, seed)

    if saveBoard:
        #saveBoardTextFile(c, algorithm, seed, iterations)
        saveCellularAutomataJSON(c, seed, iterations, image_path=image)
    
    if drawBoard:
        closeDrawing(window)

    print(f'{algorithm.__name__} cellular automata processing complete.')

height = 100
width = 100
iterations = 100  
board, seed = noiseBoard(100, 100)
#board = checkerBoard(100, 100)
#seed = -1
#board = blankBoard(100, 100)
#seed = -1

runAutomata(width, height, iterations, conway, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)

'''
runAutomata(width, height, iterations, fourDirections_fourOrMore, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, fourDirections_threeOrMore, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, fourDirections_twoOrMore, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, conway, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, conway_modified_1, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, conway_modified_2, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, conway_modified_3, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, conway_modified_4, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, conway_modified_5, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, conway_modified_6, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, conway_modified_7, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, conway_modified_8, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, conway_modified_9, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, conway_modified_10, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, conway_modified_11, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, conway_modified_12, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, conway_modified_13, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, conway_modified_14, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, conway_modified_15, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_1, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_2, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_3, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_4, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, scroll_N, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, scroll_NE, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, scroll_E, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, scroll_SE, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, scroll_S, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, scroll_SW, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, scroll_W, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, scroll_NW, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_5, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_6, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_7, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_8, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_9, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_10, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_11, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_12, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_13, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_14, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_15, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_16, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_17, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_18, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_19, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_20, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_21, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_22, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_23, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_24, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_25, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_26, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_27, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_28, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_29, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_30, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_31, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_32, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_33, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_34, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_35, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_36, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_37, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_38, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_39, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_40, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_41, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_42, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_43, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_44, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_45, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_46, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_47, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_48, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_49, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_50, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_51, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_52, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_53, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_54, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_55, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_56, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_57, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_58, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_59, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_60, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_61, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_62, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_63, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_64, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_65, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_66, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_67, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_68, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_69, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_70, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_71, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_72, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_73, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_74, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_75, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_76, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_77, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_78, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_79, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_80, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_81, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_82, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_83, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_84, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_85, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_86, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_87, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_88, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_89, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_90, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_91, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_92, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_93, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_94, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_95, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_96, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_97, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_98, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_99, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_100, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_101, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_102, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_103, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_104, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_105, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_106, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_107, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_108, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_109, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_110, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_111, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_112, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_113, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_114, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_115, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_116, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_117, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_118, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_119, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_120, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_121, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_122, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_123, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_124, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_125, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_126, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_127, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_128, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_129, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_130, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_131, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_132, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_133, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_134, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_135, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_136, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_137, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_138, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_139, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_140, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_141, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_142, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_143, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_144, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_145, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_146, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_147, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_148, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_149, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_150, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_151, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_152, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_153, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_154, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_155, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_156, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_157, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_158, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_159, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_160, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_161, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_162, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_163, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_164, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_165, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_166, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_167, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_168, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_169, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_170, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_171, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_172, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_173, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
#runAutomata(width, height, iterations, custom_174, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
#runAutomata(width, height, iterations, custom_175, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
#runAutomata(width, height, iterations, custom_176, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
#runAutomata(width, height, iterations, custom_177, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
#runAutomata(width, height, iterations, custom_178, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
#runAutomata(width, height, iterations, custom_179, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
#runAutomata(width, height, iterations, custom_180, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
#runAutomata(width, height, iterations, custom_181, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
#runAutomata(width, height, iterations, custom_182, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
#runAutomata(width, height, iterations, custom_183, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
#runAutomata(width, height, iterations, custom_184, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
#runAutomata(width, height, iterations, custom_185, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
#runAutomata(width, height, iterations, custom_186, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
#runAutomata(width, height, iterations, custom_187, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
#runAutomata(width, height, iterations, custom_188, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
#runAutomata(width, height, iterations, custom_189, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
#runAutomata(width, height, iterations, custom_190, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
#runAutomata(width, height, iterations, custom_191, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
#runAutomata(width, height, iterations, custom_192, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
#runAutomata(width, height, iterations, custom_193, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
#runAutomata(width, height, iterations, custom_194, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
#runAutomata(width, height, iterations, custom_195, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
#runAutomata(width, height, iterations, custom_196, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
#runAutomata(width, height, iterations, custom_197, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
#runAutomata(width, height, iterations, custom_198, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
#runAutomata(width, height, iterations, custom_199, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
#runAutomata(width, height, iterations, custom_200, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
#runAutomata(width, height, iterations, custom_201, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
#runAutomata(width, height, iterations, custom_202, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
#runAutomata(width, height, iterations, custom_203, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
#runAutomata(width, height, iterations, custom_204, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
#runAutomata(width, height, iterations, custom_205, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
#runAutomata(width, height, iterations, custom_206, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
#runAutomata(width, height, iterations, custom_207, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
#runAutomata(width, height, iterations, custom_208, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
#runAutomata(width, height, iterations, custom_209, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
#runAutomata(width, height, iterations, custom_210, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
#runAutomata(width, height, iterations, custom_211, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
#runAutomata(width, height, iterations, custom_212, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
#runAutomata(width, height, iterations, custom_213, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
#runAutomata(width, height, iterations, custom_214, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
#runAutomata(width, height, iterations, custom_215, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
#runAutomata(width, height, iterations, custom_216, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
#runAutomata(width, height, iterations, custom_217, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
#runAutomata(width, height, iterations, custom_218, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
#runAutomata(width, height, iterations, custom_219, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
#runAutomata(width, height, iterations, custom_220, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
#runAutomata(width, height, iterations, custom_221, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
#runAutomata(width, height, iterations, custom_222, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
#runAutomata(width, height, iterations, custom_223, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
#runAutomata(width, height, iterations, custom_224, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
#runAutomata(width, height, iterations, custom_225, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
#runAutomata(width, height, iterations, custom_226, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
#runAutomata(width, height, iterations, custom_227, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
#runAutomata(width, height, iterations, custom_228, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_229, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_230, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_231, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_232, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
runAutomata(width, height, iterations, custom_233, saveBoard=True, board=board, seed=seed, drawBoard=True, wraparound=True, history = True, check_history=True, save_image=True)
'''
