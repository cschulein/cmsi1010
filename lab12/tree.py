from math import radians
from Tree.core import Tree
from PIL import Image

background_color = (200, 240, 250)
leaf_color = (30, 160, 30)
trunk_width = 30
base_trunk_color = (50, 40, 0)
small_branch_color = (180, 130, 30)
branch_gradient = (*base_trunk_color, *small_branch_color)

trunk_length = 200
first_branch_line = (0, 0, 0, -trunk_length)
scales_and_angles = [(0.7, radians(-30)),
                     (0.7, radians(2)), (0.7, radians(30))]
background_color = (18, 12, 48)
leaf_color = (40, 200, 120)
trunk_width = 18
base_trunk_color = (35, 20, 10)
small_branch_color = (200, 150, 70)
branch_gradient = (*base_trunk_color, *small_branch_color)
trunk_length = 260
first_branch_line = (0, 0, 0, -trunk_length)
scales_and_angles = [(0.8, radians(-40)),
                     (0.65, radians(12)), (0.72, radians(50))]
age = 12

tree = Tree(pos=first_branch_line, branches=scales_and_angles)
tree.grow(age)
tree.move_in_rectangle()
image = Image.new("RGB", tree.get_size(), background_color)
tree.draw_on(image, branch_gradient, leaf_color, trunk_width)
image.show()
