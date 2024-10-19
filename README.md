# Useful Theory
This is an overview of basic math, electronics, physics, and some other science stuff that a Software/Computer Engineer 
may require.

## Contents
- [Calculus](calculus/README.md)
- [Linear Algebra](linear-algebra/README.md)
- [Machine Learning](machine-learning/README.md)
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
manim -tipql <filename> MyScene
```
- Render and save a video _(high quality)_:
```bash
manim -tpqk <filename> MyScene
```
