from PIL import Image, ImageDraw

# Define Pigpen cipher symbols
TOP_HORIZ_LINE = (2, 2, 26, 4)
BOT_HORIZ_LINE = (2, 24, 26, 26)
LEFT_VERT_LINE = (2, 2, 4, 26)
RIGHT_VERT_LINE = (24, 2, 26, 26)

symbols = {
    'top-right': [LEFT_VERT_LINE, BOT_HORIZ_LINE],
    'top-left': [RIGHT_VERT_LINE, BOT_HORIZ_LINE],
    'bot-right': [LEFT_VERT_LINE, TOP_HORIZ_LINE],
    'bot-left': [RIGHT_VERT_LINE, TOP_HORIZ_LINE],
    'top-u': [LEFT_VERT_LINE, RIGHT_VERT_LINE, BOT_HORIZ_LINE],
    'bot-u': [LEFT_VERT_LINE, RIGHT_VERT_LINE, TOP_HORIZ_LINE],
    'left-u': [TOP_HORIZ_LINE, RIGHT_VERT_LINE, BOT_HORIZ_LINE],
    'right-u': [TOP_HORIZ_LINE, LEFT_VERT_LINE, BOT_HORIZ_LINE],
    'square': [TOP_HORIZ_LINE, BOT_HORIZ_LINE, LEFT_VERT_LINE, RIGHT_VERT_LINE]
}

dots = {
    'single': [(12, 12, 17, 17)],
    'double': [(7, 10, 13, 16), (15, 10, 21, 16)]
}

letters = {
    'A': {'rects': symbols['top-left'], 'dots': []},
    'B': {'rects': symbols['top-left'], 'dots': dots['single']},
    'C': {'rects': symbols['top-left'], 'dots': dots['double']},
    'D': {'rects': symbols['top-u'], 'dots': []},
    'E': {'rects': symbols['top-u'], 'dots': dots['single']},
    'F': {'rects': symbols['top-u'], 'dots': dots['double']},
    'G': {'rects': symbols['top-right'], 'dots': []},
    'H': {'rects': symbols['top-right'], 'dots': dots['single']},
    'I': {'rects': symbols['top-right'], 'dots': dots['double']},
    'J': {'rects': symbols['left-u'], 'dots': []},
    'K': {'rects': symbols['left-u'], 'dots': dots['single']},
    'L': {'rects': symbols['left-u'], 'dots': dots['double']},
    'M': {'rects': symbols['square'], 'dots': []},
    'N': {'rects': symbols['square'], 'dots': dots['single']},
    'O': {'rects': symbols['square'], 'dots': dots['double']},
    'P': {'rects': symbols['right-u'], 'dots': []},
    'Q': {'rects': symbols['right-u'], 'dots': dots['single']},
    'R': {'rects': symbols['right-u'], 'dots': dots['double']},
    'S': {'rects': symbols['bot-left'], 'dots': []},
    'T': {'rects': symbols['bot-left'], 'dots': dots['single']},
    'U': {'rects': symbols['bot-left'], 'dots': dots['double']},
    'V': {'rects': symbols['bot-u'], 'dots': []},
    'W': {'rects': symbols['bot-u'], 'dots': dots['single']},
    'X': {'rects': symbols['bot-u'], 'dots': dots['double']},
    'Y': {'rects': symbols['bot-right'], 'dots': []},
    'Z': {'rects': symbols['bot-right'], 'dots': dots['single']},
    'AA': {'rects': symbols['bot-right'], 'dots': dots['double']},
}

for letter, coordinates in letters.items():
    # Create an image with white background
    img = Image.new('L', (28, 28), color='white')
    draw = ImageDraw.Draw(img)

    # Draw the rects
    rects = coordinates['rects']
    for each_rect in rects:
        draw.rectangle(each_rect, fill='black')

    # Draw the dots
    dots = coordinates['dots']
    for each_dot in dots:
        draw.ellipse(each_dot, fill='black')

    # Save the image
    img.save(f'letters/{letter}/1.png')
