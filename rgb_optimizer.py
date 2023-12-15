# class b_tree:
#     class b_node:
#         def __init__(self,data,left=None,right=None):
#             self.data = None
#             self.left = None
#             self.right = None

#     def __init__(self):
#         self.root = b_node(128)

#     def insert(self,value):
#         node = b_node(value)

#         if node.data < self.root.data:


# bt = b_tree()

import random

class RGB_Optimizer:
    def __init__(self):
        self.rgb = 128
        self.h_dim = None
        self.actions = [-1,0,1]

    def make_action(self,filename):
        # Action 1: Terminate
        # Action 2: Divide rgb by 2
        # Action 3: Divide rgb by 2, add quotient to existing rgb

        if A == -1:
            self.rgb = self.rgb/2

        if A == 0:
            return

        if A == 1:
            self.rgb += self.rgb/2

        bw_file = rgb_to_grayscale(filename,self.rgb)
        hdim = hausdorff_dimension(bw_file)
        reward = None # somehow calculate reward

