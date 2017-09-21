## Experiments with Data

### What does the average country flag look like?

* How many colors does average flag have?
```
4.0
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
          count  percentage  eng_freq
letters                              
-        128508    1.286697       NaN
0         20200    0.202254       NaN
1         26262    0.262951       NaN
2         24964    0.249954       NaN
3         16343    0.163636       NaN
4         17613    0.176352       NaN
5         11094    0.111080       NaN
6         10265    0.102779       NaN
7         10328    0.103410       NaN
8         12281    0.122965       NaN
9         10136    0.101488       NaN
_             8    0.000080       NaN
a        934509    9.356851     8.167
b        227699    2.279856     1.492
c        387198    3.876853     2.782
d        325458    3.258676     4.253
e        962976    9.641879    12.702
f        166133    1.663421     2.228
g        239338    2.396392     2.015
h        256478    2.568008     6.094
i        734139    7.350629     6.966
j         54969    0.550382     0.153
k        190263    1.905024     0.772
l        462582    4.631642     4.025
m        339264    3.396910     2.406
n        609680    6.104473     6.749
o        726197    7.271109     7.507
p        290144    2.905091     1.929
q         21100    0.211266     0.095
r        640267    6.410728     5.987
s        646953    6.477672     6.327
t        607965    6.087301     9.056
u        322071    3.224763     2.758
v        136310    1.364815     0.978
w        117703    1.178511     2.360
x         66742    0.668260     0.150
y        166119    1.663281     1.974
z         67172    0.672565     0.074
```
* What letters are most common in website domains?
```
        Domain  English Language
e    9.641879%           12.702%
```
* What letters are most common as first letter in website domains?
```
      Domain    English Language
s    9.0259%              6.327%
```
* What letters are most common as last letter in website domains?
```
       Domain   English Language
s    14.3566%             6.327%
```

###Bar graph for Monogram
![English VS Domain Names Letter](https://github.com/Vizbi/experiments/blob/master/domains/monogram_analytics.png "English VS Domain Names Letter Frequency")

###Bar graph for Bigram
![English VS Domain Names Bigram](https://github.com/Vizbi/experiments/blob/master/domains/bigram_analytics.png "English VS Domain Names Bigram")

The letter frequency of english is well known.
For example, [this wikipedia](https://en.wikipedia.org/wiki/Letter_frequency) article
tells us that the letter `e` is most common. We compare the domain letter frequency with english letter frequency.

We also compare the [bigram frequency in english langauge] with bigram frequency
 in domain names.
