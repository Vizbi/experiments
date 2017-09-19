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


### What letters and words are most common in domains?

Alexa published a list of [top one million websites](http://s3.amazonaws.com/alexa-static/top-1m.csv.zip). We analyze that to find out

* What letters are most common in website domains?
* What letters are most common as first letter in website domains?
* What letters are most common as last letter in website domains?

The letter frequency of english is well known.
For example, [this wikipedia](https://en.wikipedia.org/wiki/Letter_frequency) article
tells us that the letter `e` is most common. We compare the domain letter frequency with english letter frequency.

We also compare the [bigram frequency in english langauge] with bigram frequency
 in domain names.
