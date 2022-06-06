from typing import List
import os
import hashlib

import numpy as np
import pandas as pd
import cv2 as cv
import click
import matplotlib.pyplot as plt

from common.plots import plot_template_match
from common.io import load_image

@click.command()
@click.option(
    "--template",
    type=str,
    required=True
)
@click.option(
    "--target",
    type=str,
    required=True
)
@click.option(
    "--template_downscale_factor",
    type=int,
    required=False,
    default=5,
    show_default=True
)
@click.option(
    "--output_dir",
    type=str,
    default="results",
    required=False
)
@click.option(
    "--do_render_figures",
    is_flag=True,
)
def main(
    template: str,
    target: str,
    template_downscale_factor: int,
    output_dir: str,
    do_render_figures: bool
):
    template_img: np.ndarray = load_image(template, downscale_factor=template_downscale_factor)
    target_img: np.ndarray = load_image(target, downscale_factor=1)
    
    match_img: np.ndarray = cv.matchTemplate(target_img, template_img, cv.TM_CCOEFF_NORMED)

    # Extract lower left corner
    y, x = np.unravel_index(np.argmax(match_img), match_img.shape)

    # Create rectangle indicating best guess location of template on target
    rect = plt.Rectangle((x, y), template_img.shape[1], template_img.shape[0], edgecolor='b', facecolor='none')

    # Print rect bounds to stdout
    print(rect.get_x(), rect.get_y(), template_img.shape[1], template_img.shape[0])

    # Save a figure if specified
    if(do_render_figures):
        fig_name = hashlib.md5(match_img.astype("uint8")).hexdigest()
        save_path = os.path.join(output_dir, fig_name)
        if not os.path.isdir(output_dir):
            os.makedirs(output_dir)
        plot_template_match(template_img, target_img, match_img, rect, save_path)

if __name__ == "__main__":
    main()
