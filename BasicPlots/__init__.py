import matplotlib.pyplot as plt

def default_size():
    return plt.rcParams["figure.figsize"]

def start_plot(width, height):
    w, h = default_size()
    if width is not None:
        w = width
    if height is not None:
        h = height
    # Start plot
    return plt.subplots(figsize=(w,h))

def barchart(x, y, xlab="x", ylab="y", title="Plot", width=None, height=None):
    "Plots y vs. x as a bar chart."
    fig, ax = start_plot(width, height)
    plt.bar(range(len(x)), y)
    ax.set(xlabel=xlab, ylabel=ylab, title=title)
    ax.set_xticks(range(len(x)), labels=x)
    return fig, ax

def simple_scatter(x, y, xlab="x", ylab="y", title="Plot", width=None, height=None):
    "Just a normal scatterplot with no grouping."
    fig, ax = start_plot(width, height)
    plt.scatter(x, y)
    ax.set(xlabel=xlab, ylabel=ylab, title=title)
    return fig, ax

def scatterplot(x, y, groups=None, xlab="x", ylab="y", title="Plot", width=None, height=None):
    "Scatterplot with points coloured by their respective groups (discrete variable)"
    if groups is None:
        # Don't need colours
        return simple_scatter(x, y, xlab, ylab, title)
    fig, ax = start_plot(width, height)
    # Split the dataset into groups
    groups = dict()
    for x, y, group in zip(x,y,label):
        if group in groups:
            groups[group].append((x,y))
        else:
            groups[group] = [(x,y)]
    # Plot each group along with their labels
    for g in groups:
        xs = [xy[0] for xy in groups[g]]
        ys = [xy[1] for xy in groups[g]]
        plt.scatter(xs, ys, label=g)
    ax.set(xlabel=xlab, ylabel=ylab, title=title)
    # Make legend
    ax.legend()
    return fig, ax

def heatmap(X, row_names=True, col_names=True, 
            row_label="Row", col_label="Column", title="Plot"):
    "Heatmap with legend and automatic sizing."
    rows, cols = X.shape
    width = max(cols / 5 + 2, 4)
    height = max(rows / 5, 4)
    fig, ax = plt.subplots(figsize=(width, height), layout="constrained")
    im = ax.imshow(X, cmap='plasma')
    ax.set(xlabel=col_label, ylabel=row_label, title=title)
    # Label the rows and columns but names weren't provided
    if row_names == True:
        row_names = [str(x) for x in range(rows)]
    if col_names == True:
        col_names = [str(y) for y in range(cols)]
    # Set the axes
    if col_names != False:
        ax.set_xticks(range(len(col_names)), col_names, rotation=90)
    if row_names != False:
        ax.set_yticks(range(len(row_names)), row_names)
    fig.colorbar(im, shrink=0.3)
    return fig, ax

def boxplot(x, x_groups, label_order=None, xlab="x", ylab="y", title="Plot", width=None, height=None):
    "Boxplot of x values where each value belongs to its respective x_groups."
    fig, ax = start_plot(width, height)
    all_data = dict()
    for x, g in zip(x, x_groups):
        if g in all_data:
            all_data[g].append(x)
        else:
            all_data[g] = [x]
    if label_order is None:
        labels = all_data.keys()
    else:
        labels = label_order
    bplot = ax.boxplot([all_data[x] for x in labels],
                       vert=True,  # vertical box alignment
                       #patch_artist=True,  # fill with color
                       labels=labels)  # will be used to label x-ticks
    ax.set(xlabel=xlab, ylabel=ylab, title=title)
    return fig, ax

def hist(x, bins=20, xlab="x", ylab="y", title="Plot", width=None, height=None):
    "Plots distribution of x values as a histogram."
    fig, ax = start_plot(width, height)
    ax.hist(x, bins=bins)
    ax.set(xlabel=xlab, ylabel=ylab, title=title)
    return fig, ax
    
def save_figure(obj, filename):
    "Saves the output plot to a file."
    fig, ax = obj
    fig.savefig(filename)

