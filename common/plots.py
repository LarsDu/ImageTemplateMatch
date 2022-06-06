from typing import Optional
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def plot_template_match(
    template: np.ndarray,
    target: np.ndarray,
    match: np.ndarray,
    rect: Rectangle,
    save_path: Optional[str] = None
) -> plt.Axes:
    """ Plot template, target, match and a rectagle
    indicating the location of the match on the target image
    """
    fig, ax = plt.subplots(1,3)
    fig.set_size_inches(30,7)

    ax[0].set_title('template')
    ax[0].imshow(template)

    ax[1].imshow(target)
    ax[1].set_title('target')
    ax[1].add_patch(rect)

    ax[2].imshow(match)
    ax[2].set_title('`match_template`\nresult')
    ax[2].autoscale(False)
    ax[2].plot(rect.get_x(), rect.get_y(), 'o', markeredgecolor='r', markerfacecolor='none', markersize=10)
    if(save_path):
        fig.savefig(save_path +'.png', format="png")
    return ax