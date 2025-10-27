import sched
import time
def add(*arg):
    sum=0
    for i in arg:
        sum+=i
    return sum

def shudule_function(event_time,function,*arg):
    s=sched.scheduler(time.time,time.sleep)
    s.enterabs(event_time,1,function,argument=arg)
    print(f"{function.__name__}{arg} shuduled for {time.asctime(time.localtime(event_time))}")
    s.run()

shudule_function(time.time()+1,print,"Rajesh","is a good Person")
shudule_function(time.time()+3,lambda *x:print(f"sum of values for {x} is: ",add(*x)),5,6,7,8,9)

"""
1. add(*arg) Function

What it does: Takes any number of numbers (*arg) and returns their sum.

Logic:

add(5, 6, 7) → 18


Use: Used later to calculate sum dynamically inside a scheduled function.

🔹 2. shudule_function(event_time, function, *arg)

What it does:
Schedules any function to run at a specific absolute time (event_time).

Key parts:

s.enterabs(event_time, 1, function, argument=arg)


enterabs → schedules the task based on an absolute time (not delay).

argument=arg → passes arguments to the function when executed.

Prints schedule info:

print(f"{function.__name__}{arg} scheduled for {time.asctime(...)}")


So you know what is scheduled and when.

🔹 3. Example 1:
shudule_function(time.time()+1, print, "Rajesh", "is a good Person")


Runs print("Rajesh", "is a good Person") after 1 second.

Output:

print('Rajesh', 'is a good Person') scheduled for Mon Oct 27 12:00:01 2025
Rajesh is a good Person

🔹 4. Example 2:
shudule_function(time.time()+3, lambda *x: print(f"sum of values for {x} is: ", add(*x)), 5, 6, 7, 8, 9)


Runs after 3 seconds.

Lambda calls add(5,6,7,8,9) → 35

Output:

sum of values for (5, 6, 7, 8, 9) is: 35

⚙️ 5. Key Takeaways

✅ You can schedule any function to run at a future time.
✅ Uses absolute time (enterabs), not delay-based scheduling.
✅ Great for simple task automation without using threads or async.
"""