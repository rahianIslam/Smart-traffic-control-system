import pandas
import splitfolders


# Split val/test with a fixed number of items, e.g. `(100, 100)`, for each set.
# To only split into training and validation set, use a single number to `fixed`, i.e., `10`.
# Set 3 values, e.g. `(300, 100, 100)`, to limit the number of training values.



# Split with a ratio.
# To only split into training and validation set, set a tuple to `ratio`, i.e, `(.8, .2)`.
# splitfolders.ratio(input_folder, output="C:\Users\sadma\Lab2\Final Project\Highway_Dataset",
#     seed=1337, ratio=(.7, .2, .1), group_prefix=2, move=False) # default values
# splitfolders.fixed("input_folder", output="output",
#     seed=1337, fixed=(100, 100), oversample=False, group_prefix=None, move=False)

input_folder = r"C:\Users\sadma\Lab2\Final Project\Highway_Dataset\Traffic Data"
splitfolders.ratio(input_folder, output=r"C:\Users\sadma\Lab2\Final Project\Highway_Dataset", seed=1337, ratio=(.7, .2, .1), group_prefix=2, move=False)
print('res')


images = pandas.r