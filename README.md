## Experiments with Data

### What does the average country flag look like?

* How many colors does average flag have?
```
4.7962962963
```
* What colors are the most prominent in flags?
```
Color
red       80
white     75
silver    45
orange    45
gray      32
teal      29
navy      28
green     28
black     21
olive     18
maroon    12
purple    10
lime       4
blue       3
yellow     2
Name: Country, dtype: int64


```
* What country has most colors in its flag?
```
Country                 Color
Guyana                      9
Jordan                      8
Central African Republic    8


```
* What country has least colors in its flag?
```
Country                                   Color
Poland                                        2
Bangladesh                                    2
Qatar                                         2
Japan                                         2
Palau                                         2
China                                         2
Monaco                                        2
Mauritania                                    2
Somalia                                       2
Latvia                                        2
Albania                                       2

```

Raw images are from [flagipedia](http://flagpedia.net/download). The images were parsed with Pillow.


### What letters and words are most common in domains?

Alexa published a list of [top one million websites](http://s3.amazonaws.com/alexa-static/top-1m.csv.zip). We analyze that to find out

```
   letters   index  percentage
11       _       8    0.000080
10       9   10136    0.101488
7        6   10265    0.102779
8        7   10328    0.103410
6        5   11094    0.111080
9        8   12281    0.122965
4        3   16343    0.163636
5        4   17613    0.176352
1        0   20200    0.202254
28       q   21100    0.211266
3        2   24964    0.249954
2        1   26262    0.262951
21       j   54969    0.550382
35       x   66742    0.668260
37       z   67172    0.672565
34       w  117703    1.178511
0        -  128508    1.286697
33       v  136310    1.364815
36       y  166119    1.663281
17       f  166133    1.663421
22       k  190263    1.905024
13       b  227699    2.279856
18       g  239338    2.396392
19       h  256478    2.568008
27       p  290144    2.905091
32       u  322071    3.224763
15       d  325458    3.258676
24       m  339264    3.396910
14       c  387198    3.876853
23       l  462582    4.631642
31       t  607965    6.087301
25       n  609680    6.104473
29       r  640267    6.410728
30       s  646953    6.477672
26       o  726197    7.271109
20       i  734139    7.350629
12       a  934509    9.356851
16       e  962976    9.641879

```
* What letters are most common in website domains?
```
e    9.641879%
```
* What letters are most common as first letter in website domains?
```
s    9.0259%
```
* What letters are most common as last letter in website domains?
```
s    14.3566%
```

The letter frequency of english is well known.
For example, [this wikipedia](https://en.wikipedia.org/wiki/Letter_frequency) article
tells us that the letter `e` is most common. We compare the domain letter frequency with english letter frequency.

We also compare the [bigram frequency in english langauge] with bigram frequency
 in domain names.
