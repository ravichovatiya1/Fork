# Meme Generator Tool

## Overview
The `Meme Generator Web Tool` is a Django-based web application that allows users to generate memes based on their own images or a predefined library of images. With this tool, users can add up to three text captions to the selected image, customize the caption colors and positions, and generate a meme image with the applied modifications. The tool leverages HTML canvas for text input and manipulation, and the Pillow library (`PIL`) for image processing and overlaying the captions.

## Features
- Upload an image or choose from a library of meme images.
- Add up to three text captions to the selected image.
- Customize the font color and background color of the captions.
- Adjust the position of the captions on the image (top, bottom, or center).
- Generate and display the meme image with the applied modifications.
- Download the generated meme image for further use or sharing.

## Prerequisites

- Python version: 3.10.0
- Database: SQLite

## Getting Started

1. Clone the repository:

```bash
git clone https://github.com/ravichovatiya1/Fork.git

```

2. Create a virtual environment:

```bash
python -m venv venv

```

3. Activate the virtual environment:

- For Windows

```bash
venv\Scripts\activate
```

- For Linux/macOS
```bash
source venv/bin/activate

```

4. Install requirements.txt file


```bash
pip install -r requirements.txt 
```


5. Make Migrations and migrate:

- Use below command to create the migrations file

```bash
python manage.py makemigrations
```

- Use Below command to reflect the changes to database of migrations.
```bash
python manage.py migrate

```

6. Runserver:

```bash
python manage.py runserver 0.0.0.0:8000
```














