import inspect
import os
from pathlib import Path
import imgaug.augmenters as iaa

from text_renderer.effect import *
from text_renderer.corpus import *
from text_renderer.config import (
    RenderCfg,
    NormPerspectiveTransformCfg,
    GeneratorCfg,
    FixedTextColorCfg,
)
from text_renderer.layout.same_line import SameLineLayout
from text_renderer.layout.extra_text_line import ExtraTextLineLayout


CURRENT_DIR = Path(os.path.abspath(os.path.dirname(__file__)))
OUT_DIR = CURRENT_DIR / "output"
DATA_DIR = CURRENT_DIR
BG_DIR = DATA_DIR / "bg"
CHAR_DIR = DATA_DIR / "char"
FONT_DIR = DATA_DIR / "font"
FONT_LIST_DIR = DATA_DIR / "font_list"
TEXT_DIR = DATA_DIR / "text"

font_cfg = dict(
    font_dir=FONT_DIR,
    font_list_file=FONT_LIST_DIR / "font_list.txt",
    font_size=(40, 55),
)

perspective_transform = NormPerspectiveTransformCfg(20, 20, 1.5)


def get_char_corpus():
    return CharCorpus(
        CharCorpusCfg(
            text_paths=[TEXT_DIR / "chn_text.txt", TEXT_DIR / "eng_text.txt"],
            filter_by_chars=True,
            chars_file=CHAR_DIR / "chn.txt",
            length=(5, 10),
            char_spacing=(-0.3, 1.3),
            **font_cfg
        ),
    )


def base_cfg(
    name: str, corpus,  n_image = 10, corpus_effects=None, layout_effects=None, layout=None, gray=True
):
    return GeneratorCfg(
        num_image=n_image,
        save_dir=OUT_DIR / name,
        render_cfg=RenderCfg(
            bg_dir=BG_DIR,
            perspective_transform=perspective_transform,
            gray=gray,
            layout_effects=layout_effects,
            layout=layout,
            corpus=corpus,
            corpus_effects=corpus_effects,
        ),
    )


def rebar_vertical_data():
    return base_cfg(
        name= inspect.currentframe().f_code.co_name,
        n_image = 100,
        corpus=EnumCorpus(
            EnumCorpusCfg(
                text_paths=[TEXT_DIR / "rebar_data.txt"],
                filter_by_chars=True,
               	horizontal = False,
                chars_file=CHAR_DIR / "eng.txt",
                **font_cfg
            ),
        ),
        corpus_effects = Effects(
            [
                Line(p=0.5,line_pos_p=(0.25,0.25,0.25,0.25,0,0,0,0,0,0) ,color_cfg=FixedTextColorCfg()),
                OneOf([DropoutRand(), DropoutVertical()]),
            ]),
    )
    
def rebar_data():
    return base_cfg(
        name= inspect.currentframe().f_code.co_name,
        n_image = 100,
        corpus=EnumCorpus(
            EnumCorpusCfg(
                text_paths=[TEXT_DIR / "rebar_data.txt"],
                filter_by_chars=True,
                chars_file=CHAR_DIR / "eng.txt",
                **font_cfg
            ),
        ),
        corpus_effects = Effects(
            [
                Line(p=0.5,line_pos_p=(0.25,0.25,0.25,0.25,0,0,0,0,0,0) ,color_cfg=FixedTextColorCfg()),
                OneOf([DropoutRand(), DropoutVertical()]),
            ]),
    )



# fmt: off
# The configuration file must have a configs variable
configs = [
    rebar_vertical_data(),
    rebar_data(),
]
# fmt: on
