import matplotlib.pyplot as plt

def get_image(data):
    img = data[1:].copy()
    img = img.reshape((28, 28))

    fig, ax = plt.subplots()
    ax.imshow(img, cmap="gray")

    plt.show()
