# rl_hausdorff_dimension
Using RL to find the ideal Hausdorff dimension of an image.

--------

This project calculates the Hausdorff dimension of the contents of a .jpg or .png file. It takes in two inputs: an image file (.jpg or .png) and an integer value 0 < x < 255. The integer value is a threshold RGB value by which to grayscale the image. A different threshold will result in a different Hausdorff dimension.  

The purpose of this project is to use reinforcement learning to find an optimal RGB threshold value and an optimal Hausdorff dimension. In other words, to find an optimal input and output. Since there are two moving parts, this project makes use of a deep deterministic policy gradient (DDPG).
