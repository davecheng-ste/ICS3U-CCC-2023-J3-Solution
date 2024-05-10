# CCC 2023 - Problem J3: Special Event

You are trying to schedule a special event on one of five possible days.
Your job is to determine on which day you should schedule the event, so that the largest number of interested people are able to attend.

### Input Specification
The first line of input will contain a positive integer `N`, representing the number of people interested in attending your event. The next `N` lines will each contain one person’s availability using one character for each of Day 1, Day 2, Day 3, Day 4, and Day 5 (in that order).

The character `Y` means the person is able to attend and a period (`.`) means the person is not able to attend.

### Output Specification
The output will consist of one line listing the day number(s) on which the largest number of interested people are able to attend.

If there is more than one day on which the largest number of people are able to attend, output all of these day numbers in increasing order and separated by commas (without spaces).

#### Sample Input 1
```
3
YY.Y.
...Y.
.YYY.
```

#### Output for Sample Input 1
```
4
```

#### Explanation of Output for Sample Input 1
All three people are able to attend on Day 4, and they are not all available on any other day.

<br><br>

#### Sample Input 2
```
5
YY..Y
.YY.Y
.Y.Y.
.YY.Y
Y...Y
```

#### Output for Sample Input 2
```
2,5
```

#### Explanation of Output for Sample Input 2
There is no day on which all five people are able to attend. Four people are able to attend on both Day 2 and Day 5.

<br><br>

## Additional Test Cases
#### Sample Input 3
```
1
.Y...
```
#### Expected Output 3
```
2
```

<br><br>

#### Sample Input 4
```
3
Y....
Y....
Y....
```
#### Expected Output 4
```
1
```

<br><br>


#### Sample Input 5
```
12
Y.YY.
.YYY.
Y.Y.Y
.YYY.
Y.YY.
.YYY.
.....
.YY..
Y.YY.
.YYY.
Y.Y.Y
.YY..
```
#### Expected Output 5
```
3
```

<br><br>


#### Sample Input 6
```
1
Y..YY
```
#### Expected Output 6
```
1,4,5
```

<br><br>


#### Sample Input 7
```
5
YYYYY
.....
YYYYY
YYYYY
.....
```
#### Expected Output 7
```
1,2,3,4,5
```
