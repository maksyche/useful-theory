# Useful Theory
This is my cheatsheet for math, electronics, physics, and some other science stuff that a software/hardware engineer may require.

## Contents
- [Calculus](calculus/README.md)
- [Linear Algebra](linear-algebra/README.md)
- [Neural Networks](neural-networks/README.md)
- [Digital Signal Processing](dsp/README.md)
- [Electronics](/electronics/README.md)

### Generate Contents Table
```bash
python3 toc_generator.py
```

## Graphics
I use [Manim CE](https://github.com/ManimCommunity/manim) to generate images and videos.

- Render and save an image _(last frame of the scene)_:
```bash
manim -spqk <filename> MyScene
```
- Render and save a gif _(low quality)_:
```bash
manim -ipql <filename> MyScene
```
- Render and save a video _(high quality)_:
```bash
manim -pqk <filename> MyScene
```
