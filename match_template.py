import os
from typing import List

import numpy as np
import pandas as pd
import click


@click.command()
@click.argument(
    "--template",
    type=str,
    required=True
)
@click.argument(
    "--target",
    type=str,
    required=True
)
@click.argument(
    "--output_dir",
    type=str,
    default="results"
    required=False
)
@click.option(
    "--do_render_figures",
    is_flag=True,
)
def main(
    template: str,
    target: str,
    output_dir: str,
    do_render_figures: bool
):
    pass


if __name__ == "__main__":
    main()
