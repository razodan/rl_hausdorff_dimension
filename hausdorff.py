import numpy as np
import PIL
from PIL import Image
import matplotlib.pyplot as plt
import math
import statistics

def rgb_to_grayscale(image: str, rgb_val: int = 128) -> str:
    '''
    Input: image filename (*.jpg, *.png), integer RGB value to compare against.
        Image filename is a string. This method will save a grayscale version of the image.
        Pixels are set to black or white depending on whether they are smaller or larger rgb_val.
        
    Output: Method saves grayscaled image, and returns name of grayscaled image as a string.
        Name of grayscaled image is "bw_" + name of original image + "_rgb" + rgb value input
    '''
    img = Image.open(image)
    gray = img.convert('L') # I forgot why this is necessary
    bw = gray.point(lambda x: 0 if x<rgb_val else 255, '1')
    bw_image = "bw_rgb" + str(rgb_val) + "_" + image
    bw.save(bw_image)
    return bw_image

def find_nonzero_pixels(image: str) -> tuple:
    '''
    Input: image filename (*.jpg, *.png)
        Image filename is a string. This method finds all nonzero pixels in the image.
    Output: nparray of nonzero pixels.
    '''
    img = Image.open(image)
    img = np.asarray(img)
    pixels=[] # Code is much faster if pixels is a list

    # If a pixel has a nonzero value, add it to pixels
    # i.e. this is a position that contains a white pixel
    for i,j in np.ndindex(img.shape):
        if img[i][j] > 0:
            pixels.append((i,j))
        # Note: I tried this with nested for-loops, lambda expressions, and np.insert
        
    return (np.array(pixels),img.shape)

def slope(x: np.ndarray, y: np.ndarray) -> float:
    '''
    Simple method  to calculate slope given two arrays of points.
    '''
    xs = np.flip(x)
    ys = np.flip(y)
    slope=[]
    
    for i in range(len(x)):
        sub_x = xs[i] - xs[i-1]
        sub_y = ys[i] - ys[i-1]
        slope.append(sub_y/sub_x)
        
    return statistics.mean(slope)

def hausdorff_dimension(image: str):
    '''
    Outputs four objects:
        1. Array of x-values
        2. Array of y-values
        3. Tuple of slope and y-interecept
        4. Hausdorff dimension
    '''

    pixels,shape = find_nonzero_pixels(image)
    # x_shape,y_shape = shape
    # I don't remember which is correct, the above or below one
    y_shape,x_shape = shape

    # Use logspace instead of linspace because of the logarithmic nature of Hausdorff dimension
    log_results = np.logspace(start=0.001,stop=1,num=100,endpoint=False,base=math.e)
    res=[]
    
    # Calculate multidimensional histogram of the pixels
        # It's kind of like box-counting, but counting x-lines and y-lines
        # np.arange from - to x_shape/y_shape, count by each log_result value
    for log in log_results:
        hist = np.histogramdd(sample=pixels,bins=(np.arange(0,x_shape,log),
                                        np.arange(0,y_shape,log)))[0]
        # append the first histogram element to y-values
        result = np.sum(hist>0)
        res.append(result)
    
    # Take the log of x-values and y-values
    log_results = np.log(log_results)
    res = np.log(res)
    
#     def slope(x,y):
#         xs = np.flip(x)
#         ys = np.flip(y)
#         slope=[]
#         for i in range(len(x)):
#             sub_x = xs[i] - xs[i-1]
#             sub_y = ys[i] - ys[i-1]
#             slope.append(sub_y/sub_x)

#         return statistics.mean(slope)

    # get the slope
    ret=slope(log_results,res)
    hausdorff=-ret
    print(f'Hausdorff dimension of {image}:\n{hausdorff}')
    
    # return (log_results,res,hausdorff)

    slopes = np.polyfit(log_results,res,1)
    # print(f'Hausdorff dimension with np.polyfit():\n{hausdorff}')
    
    return (log_results,res,slopes,hausdorff)
        
            
        

def plot_regression(xs: np.ndarray, ys: np.ndarray, slopes: np.ndarray):
    '''
    Use matplotlib.pyplot to plot the regression line given x-array, y-array, and slopes
    '''
    plt.plot(xs,ys, 'o', mfc='none')
    plt.plot(xs, np.polyval(slopes,xs))
    plt.xlabel('log $\epsilon$')
    plt.ylabel('log N')
    plt.show()
    
    
    
    
    
# Consider OOP approach?
class Hausdorff_Measure():
    def __init__(self, h_dim: float=0.0, xs: np.ndarray=None, ys: np.ndarray=None):
        self.hausdorff_dimension = h_dim
        self.x_array = xs
        self.y_array = ys
        self.slopes = None
    
    