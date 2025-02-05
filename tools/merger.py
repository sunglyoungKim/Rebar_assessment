import json
import pathlib
import shutil

def merge_labels(dst_dataset_folder, import_datset_folder):
        '''
        it will merge all the labels and images into dst_dataset_folder
        '''
        with open(dst_dataset_folder/'labels.json') as rebar_label:
            a = json.load(rebar_label)
        with open(import_datset_folder/'labels.json') as rebar_label:
            b = json.load(rebar_label)
    
        dst_num = a['num-samples']
        move_into_num = b['num-samples']
    
        a['num-samples'] = dst_num + move_into_num
    
        for i in range(move_into_num ):
            new_num= i+dst_num
            a['labels'].update({f'{new_num:09d}':b['labels'][f'{i:09d}']})
            a['sizes'].update({f'{new_num:09d}':b['sizes'][f'{i:09d}']})
    
        for file_name in sorted(pathlib.Path(import_datset_folder/'images/').rglob('*')):
            file_name.replace(dst_dataset_folder/'images'/f'{int(file_name.stem) + int(dst_num):09d}.jpg')
    
        with open(dst_dataset_folder / 'labels.json', "w") as outfile:
            json.dump(a, outfile)
    
    
def merge_all_dataset(output_path, logger):
    '''
    given output path
    it will merge all the dataset into the first dataset
    
    '''
    
    datasets = sorted(pathlib.Path(output_path).glob('*'))
    for data in datasets[1:]:
        merge_labels(datasets[0], data)
        shutil.rmtree(data)

    logger.info(f"Finish Merger")
            