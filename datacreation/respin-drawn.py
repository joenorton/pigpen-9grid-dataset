import random
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance
import os

def apply_transformations(img, scale_factor, rotation_angle, translation, noise_level, contrast_level=1.0, brightness_level=1.0, seed=None):
    if seed is not None:
        random.seed(seed)
        np.random.seed(seed)

    # Scale the image
    scaled_img = img.resize((int(img.width * scale_factor), int(img.height * scale_factor)), Image.ANTIALIAS)

    # Rotate the image and fill the background
    rotated_img = scaled_img.rotate(rotation_angle, expand=True, fillcolor='white')


    # Create a new image (28x28) for translation and paste the rotated image
    new_img = Image.new('L', (28, 28), 'white')
    paste_x = (28 - rotated_img.width) // 2 + translation[0]
    paste_y = (28 - rotated_img.height) // 2 + translation[1]
    new_img.paste(rotated_img, (paste_x, paste_y))

    if contrast_level != 1.0 or brightness_level != 1.0:
        enhancer = ImageEnhance.Contrast(new_img)
        new_img = enhancer.enhance(contrast_level)
        enhancer = ImageEnhance.Brightness(new_img)
        new_img = enhancer.enhance(brightness_level)

    # Add noise
    if noise_level > 0:
        noise = np.random.normal(0, noise_level, (28, 28))
        noise_img = Image.fromarray(np.array(new_img) + noise).convert('L')
        return noise_img

    return new_img

def randomize_parameters(scale_range, rotation_range, translation_range, noise_range):
    scale_factor = random.uniform(*scale_range)
    rotation_angle = random.uniform(*rotation_range)
    translation = (random.randint(*translation_range), random.randint(*translation_range))
    noise_level = random.uniform(*noise_range)
    return scale_factor, rotation_angle, translation, noise_level

def generate_transformed_images(letters, base_dir, output_dir, scale_range, rotation_range, translation_range, noise_range, contrast_level, brightness_level, seed=None):
    if seed is not None:
        random.seed(seed)

    for letter in letters:
        # Load the base image for the letter
        img_path = os.path.join(base_dir, f'{letter}.png')
        if not os.path.exists(img_path):
            continue
        img = Image.open(img_path)

        # Randomize transformation parameters
        scale_factor, rotation_angle, translation, noise_level = randomize_parameters(
            scale_range, rotation_range, translation_range, noise_range)

        # Apply transformations
        transformed_img = apply_transformations(
            img, scale_factor, rotation_angle, translation, noise_level, contrast_level, brightness_level)

        # Save the transformed image
        output_path = os.path.join(output_dir, f'{letter}/{letter}_drawn_{seed}.png')
        transformed_img.save(output_path)

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'AA']
#letters = ['A']

#train params
easy_params = {
    'scale_range': (0.6, 1.0),
    'rotation_range': (-10, 10),
    'translation_range': (-2, 2),
    'noise_range': (0, 10),
    'contrast_level': 1.5,
    'brightness_level': 0.8
}
#test params - designed to exceed the training parameters in every way
adv_params = {
    'scale_range': (0.6, 1.0),
    'rotation_range': (-12, 12),
    'translation_range': (-3, 3),
    'noise_range': (0, 15),
    'contrast_level': 0.8,
    'brightness_level': 0.7
}

# gen train set
num_samples_gen = range(1, 1001, 1)
for each_num in num_samples_gen:
    generate_transformed_images(
        letters,
        base_dir='drawn',
        output_dir='train',
        scale_range=easy_params['scale_range'],
        rotation_range=easy_params['rotation_range'],
        translation_range=easy_params['translation_range'],
        noise_range=easy_params['noise_range'],
        contrast_level=easy_params['contrast_level'],
        brightness_level=easy_params['brightness_level'],
        seed=each_num
    )

# gen test set
num_test_samples_gen = range(1002, 1252, 1)
for each_num in num_test_samples_gen:
    generate_transformed_images(
        letters,
        base_dir='drawn',
        output_dir='test',
        scale_range=adv_params['scale_range'],
        rotation_range=adv_params['rotation_range'],
        translation_range=adv_params['translation_range'],
        noise_range=adv_params['noise_range'],
        contrast_level=adv_params['contrast_level'],
        brightness_level=adv_params['brightness_level'],
        seed=each_num
    )

# gen valid. set
num_valid_samples_gen = range(2001, 2251, 1)
for each_num in num_valid_samples_gen:
    generate_transformed_images(
        letters,
        base_dir='drawn',
        output_dir='validation',
        scale_range=adv_params['scale_range'],
        rotation_range=adv_params['rotation_range'],
        translation_range=adv_params['translation_range'],
        noise_range=adv_params['noise_range'],
        contrast_level=adv_params['contrast_level'],
        brightness_level=adv_params['brightness_level'],
        seed=each_num
    )
    