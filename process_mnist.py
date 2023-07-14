import matplotlib.pyplot as plt

def get_image(data):
    img = data.copy()

    fig, ax = plt.subplots()
    ax.imshow(img, cmap="gray")

    plt.show()
