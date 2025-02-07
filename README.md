# Rebar_assessment
Rebar_Assessment

* I have added Report.txt file for detail readme


This repo is made for Rebar assessment:

The repo is based on https://github.com/oh-my-ocr/text_renderer.git


how to install

please use conda with environment.yml

 $conda env create -f enviornment.yml


Example of usage:

 $python main.py --config rebar_gen/rebar.py --num_processes 3 --log_period 10
 
 The data is generated in the rebar_gen/output directory. A labels.json file contains all annotations in follow format:
    
    {
     "labels": {
        "000000000": "test",
        "000000001": "text2"
     },
     "sizes": {
        "000000000": [width, height],
        "000000001": [width, height],
     }
     "num-samples": 2,
     }

check this link: https://github.com/Topdu/OpenOCR/blob/main/tools/create_lmdb_dataset.py

* Inside of rebar_gen/bg has background images: I have cropped engineering drawings from given asset. If we have a goood image detector to find where the floor plans are from PDF file, we can automate this pipeline, too

* To extract PDF files, please use PDF_convertor.py file

Example of usage:
 $python PDF_convertor.py --PDF_path /pdf/directory/path --dst_path /dst/pdf/image/path

* I have made random Engineering Drawing text generator
*  Please use generate_text_candidate jupyter notebook to generate text.
*  I can add more categories once I know more Engineering Drawing text type




