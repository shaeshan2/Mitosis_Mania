import random

cell_phases = ["Interphase", "Prophase", "Metaphase", "Anaphase", "Telophase", "Cytokinesis"]
cell_phases2 = ["Interphase", "Prophase", "Metaphase", "Anaphase", "Telophase", "Cytokinesis"]
random.shuffle(cell_phases)

current_phase = 0
score = 0
button_width = 100
button_height = 50
game_over = False

#create button class
class Button:
    def __init__(self, x, y, width, height, phase):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.phase = phase

    def display(self):
        fill(255)
        rect(self.x, self.y, self.width, self.height)
        fill(0)
        text(self.phase, self.x + self.width/2, self.y + self.height/2)

def setup():
    global img1, img2, img3, img4, img5, img6
    size(600, 600)
    background(255)
    textAlign(CENTER, CENTER)
    textSize(17)
    img1 = loadImage("Mitosis1.png")
    img2 = loadImage("Mitosis2.png")
    img3 = loadImage("Mitosis3.png")
    img4 = loadImage("Mitosis4.png")
    img5 = loadImage("Mitosis5.png")
    img6 = loadImage("Mitosis6.png")

def draw():
    global img1, img2, img3, img4, img5, img6, game_over, score
    background(255)
    fill(0)

    # Display the name "Mitosis Mania"
    fill(150, 0, 0)
    text("Mitosis Mania", width/2, 50)

    if game_over:
        if score == 6:
            # Display winner screen
            winnerScreen()
        else:
            # Display game over screen
            gameOverScreen()
    else:
        # Display the current phase animation
        displayPhaseAnimation()

        # Display the score
        text("Score: " + str(score), width/2, height - 100)

        # Display the phase buttons
        displayPhaseButtons()

def displayPhaseAnimation():
    global img1, img2, img3, img4, img5, img6, current_phase
    phase = cell_phases[current_phase]
    # Display the animation for the current phase
    if phase == "Interphase":
        # Animation for Interphase
        image(img1, width/2 - img1.width/2, height/2 - img1.height/2)
    elif phase == "Prophase":
        # Animation for Prophase
        image(img2, width/2 - img2.width/2, height/2 - img2.height/2)
    elif phase == "Metaphase":
        # Animation for Metaphase
        image(img3, width/2 - img3.width/2, height/2 - img3.height/2)
    elif phase == "Anaphase":
        # Animation for Anaphase
        image(img4, width/2 - img4.width/2, height/2 - img4.height/2)
    elif phase == "Telophase":
        # Animation for Telophase
        image(img5, width/2 - img5.width/2, height/2 - img5.height/2)
    elif phase == "Cytokinesis":
        # Animation for Cytokinesis
        image(img6, width/2 - img6.width/2, height/2 - img6.height/2)

def displayPhaseButtons():
    phase_buttons = []
    for i, phase in enumerate(cell_phases2):
        button_x = i * button_width
        button_y = height - button_height
        phase_button = Button(button_x, button_y, button_width, button_height, phase)
        phase_buttons.append(phase_button)
        phase_button.display()

    return phase_buttons

def mousePressed():
    global current_phase, score, game_over

    if game_over:
        # Reset the game if it's already over and the mouse is clicked
        resetGame()
    else:
        phase_buttons = displayPhaseButtons()
        for button in phase_buttons:
            if button.x <= mouseX <= button.x + button.width and button.y <= mouseY <= button.y + button.height:
                selected_phase = button.phase

                # Check if the selected phase is correct
                if selected_phase == cell_phases[current_phase]:
                    score += 1

                # Move to the next phase if it is within the valid range
                if current_phase < len(cell_phases) - 1:
                    current_phase += 1
                else:
                    game_over = True

def resetGame():
    global current_phase, score, game_over
    current_phase = 0
    score = 0
    game_over = False

def gameOverScreen():
    background(255)
    fill(255, 0, 0)
    textSize(30)
    text("Game Over", width/2, height/2 - 30)
    textSize(20)
    text("Final Score: " + str(score), width/2, height/2 + 30)
    textSize(16)
    text("Click to play again", width/2, height/2 + 60)

def winnerScreen():
    background(255)
    fill(0, 255, 0)
    textSize(30)
    text("Congratulations, You Won!", width/2, height/2 - 30)
    textSize(20)
    text("Final Score: " + str(score), width/2, height/2 + 30)
    textSize(16)
    text("Click to play again", width/2, height/2 + 60)
