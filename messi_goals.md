## Calculate the total number of goals

### Description
Use variables to find the sum of the goals Messi scored in 3 competitions

### Behavior Driven Development

The function should return the total goals 

| Input             |  Output      |
| ------------------| ------------ |
| laliga goals eg 5 |   sum        |
| uefa goals eg 10  |    22        |  
| copa del rey eg 7 |              |

### Pseudocode

> **Define** function to perform calculate the total number of goals 

>  declare a variable  to accept input and  store the number of laliga goals

>  declare a variable to accept input and store the number of uefa goals

>  declare a variable to accept input and store the number of copa del rey goals 

>  calculate the total goals and store the value in a variable 


> **Return**  Total number of goals as a string

### Python Code

```text
#Check out this program
def messi_goals():
    laliga = int(input('Enter laliga goals\n'))
    uefa = int(input('Enter Uefa goals\n'))
    copa = int(input('Enter Copa goals\n'))

    sum = laliga + uefa + copa 
    print(f'Messi total goals are {sum}')
messi_goals()    
```
### Kata Link
[View Kata](https://www.codewars.com/kata/55ca77fa094a2af31f00002a/train/python).