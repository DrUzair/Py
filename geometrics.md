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
