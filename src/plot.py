import matplotlib.pyplot as plt
import matplotlib.patches as patches


def get_data(output_path="../out.txt"):
    with open(output_path) as f:
        data = f.readlines()
    data = [i.split(' ') for i in data]
    for i, line in enumerate(data):
        data[i] = [float(j) for j in line]
    data = data[1:]
    data = [i for i in data if not i[2] == -1]
    return data


def data_to_rectangles(data):
    rectangles = []
    for rect in data:
        x, y = rect[2], rect[3]
        if  not rect[-1]:
            w, h = rect[0], rect[1]
        else:
            w, h = rect[1], rect[0]
        rectangles.append(patches.Rectangle((x, y), w, h, lw=1))

    return rectangles


def plot_rectangles(rectangles, x=2800, y=2070):
    fig2 = plt.figure()
    ax2 = fig2.add_subplot(111, aspect='equal')
    ax2.set_xlim([0, x])
    ax2.set_ylim([0, y])
    ax2.invert_yaxis()
    for rect in rectangles:
        ax2.add_patch(rect)
    fig2.savefig('rect2.png', dpi=250, bbox_inches='tight')


def main():
    data = get_data()
    rects = data_to_rectangles(data)
    plot_rectangles(rects)


if __name__ == "__main__":
    main()
