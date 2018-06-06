# Rectangle intersection/overlap

```py
def bbox_overlap(bbox1, bbox2):
    if (
        (bbox1['right_max'] >= bbox2['left_min'] ) and
        (bbox1['left_min'] <= bbox2['right_max'] ) and
        (bbox1['bottom_max'] >= bbox2['top_min'] ) and
        (bbox1['top_min'] <= bbox2['bottom_max'] ) 
    ):
        return True
    return False

bbox1 = {
        'left_min':1,
        'right_max':5,
        'top_min':-1,
        'bottom_max':15        
     }

bbox2 = {
        'left_min':1,
        'right_max':50,
        'top_min':15,
        'bottom_max':50        
     }

print(bbox_overlap(bbox1, bbox2))
```
# overlap area coordinates
```py
def bbox_overlap_area(bbox1, bbox2):
    overlap = dict()
    if (bbox1['right_max'] > bbox2['right_max']):
        overlap['right_max'] = bbox2['right_max']
    else:
        overlap['right_max'] = bbox1['right_max']
    
    if (bbox1['bottom_max'] > bbox2['bottom_max']):
        overlap['bottom_max'] = bbox2['bottom_max']
    else:
        overlap['bottom_max'] = bbox1['bottom_max']
        
    if (bbox1['left_min'] < bbox2['left_min']):
        overlap['left_min'] = bbox2['left_min']
    else:
        overlap['left_min'] = bbox1['left_min']
        
    if (bbox1['top_min'] > bbox2['top_min']):
        overlap['top_min'] = bbox1['top_min']
    else:
        overlap['top_min'] = bbox2['top_min']
    return overlap  
    
        
bbox1 = {
        'left_min':4,
        'right_max':6,
        'top_min':4,
        'bottom_max':6        
     }

bbox2 = {
        'left_min':5,
        'right_max':7,
        'top_min':5,
        'bottom_max':7        
     }
print(bbox_overlap_area(bbox1, bbox2))
```
