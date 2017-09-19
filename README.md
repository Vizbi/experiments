## Experiments with Data

### What does the average country flag look like?

* How many colors does average flag have?
```
4.7962962963
```
* What colors are the most prominent in flags?
```    
    Color
    aqua       1
    yellow     2
    lime       4
    blue       6
    purple    14
    black     21
    maroon    24
    olive     28
    green     29
    navy      29
    teal      42
    gray      50
    orange    51
    silver    62
    white     75
    red       80
    Name: Country, dtype: int64
```
* What country has most colors in its flag?
```                      
                      Country  Color
105                   Comoros     10
106                    Guyana     10
107  Central African Republic     10

```
* What country has least colors in its flag?
```  
  Country  Color
0  Poland      2
1  Monaco      2
2  Latvia      2
```
Raw images are from [flagipedia](http://flagpedia.net/download). The images were parsed with Pillow.
