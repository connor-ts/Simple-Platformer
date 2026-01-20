# Simple Platformer

## Basics

The game consists of the “player/cube” jumping from one platform to another to gain score.
There isn't much more than that, other than the kind of customization of the cat sprite.

### Score

The cube/player moves right onto the oncoming platforms, and as the cube is moved in the positive x-axis direction, the score should be increased.

* Score shouldn't be tracked if you move backwards or fall backwards.

### Cat/Player

The cat is just the cube which the player controls; the naming “cat.png” is simple, as you can use whatever image you want as long as it's named “cat.png” and is in the adjacent folder with the platformer PyGame file.

* The image I provided is only a placeholder, not the exact one you need to use.

#### Ai & Comments

Degrees of artificial intelligence were used to understand certain PyGame logic and to fulfill my ideas, which i didn’t know how to completely execute. All AI usage is well documented and clearly marked off to provide a clear understanding of the difference between my code and the LLM
All or most of the written code should be commented with what each part does, or rather, where the information came from, being listed down below in the Sources Section.

##### AI PROMPTS

-  How would I add recursively adding platforms to “this code”

& “This code” was my code at the time,

&& I had tried to use information instead of just copy and pasting but it wouldnt work numerous times.

-  How do I make my player class collide with another rect?

& Then it asked to see my code, again i tried to do it manually but it wouldnt connect correctly.

###### Notes

Currently, there are a couple of bugs that are hard to find, so I'll be trying to fix that instead of creating new ideas, but topics such as:

* double jumps
* harder jumps
* levels
may come soon, depending if I can fix the current issues

# Sources

Pygame docs:

* https://www.pygame.org/docs/ref/font.html
* https://www.pygame.org/docs/ref/rect.html
* https://www.pygame.org/docs/ref/math.html
* https://www.pygame.org/docs/ref/mouse.html

Other:

* https://share.google/MfMsRKfAFmBtraru6

* I had googled: “Does Python have a try similar to java” and got the response below in the AI summary. Although I have not used the command yet, I may use it later.
~~~
  Yes, Python has a mechanism for exception handling very similar to Java's, using the try keyword. 
The key difference in syntax is that Java uses catch, while Python uses except. Both languages also support finally blocks for cleanup code that must always run, and Python additionally has an else block which executes only if no exception occurred in the try block. 
Comparison of Syntax
Feature  Python Syntax Java Syntax Description
Try block try: try { ... } Contains the code that might cause an error.
Exception Handling except ExceptionType: catch (ExceptionType e) { ... } Catches and handles specific errors.
No Exception else: (No direct equivalent) Executes only if no exception was raised in the try block.
Cleanup finally: finally { ... } Executes regardless of whether an exception occurred or was handled.
Python Example
Here is an example demonstrating the full structure in Python:
python
try:
    # Code that might raise an exception
    result = 10 / 0
except ZeroDivisionError as e:
    # Handle a specific error
    print(f"An error occurred: {e}")
except Exception:
    # Handle any other exceptions
    print("Some other exception occurred")
else:
    # Code to run if the try block finishes without error
    print(f"Division successful, result is: {result}")
finally:
    # Code that will always execute (e.g., closing a file)
    print("Execution of try-except block is complete")

You can find more examples and details in the official Python documentation on errors and exceptions. 
Key Differences
Syntax: The main difference is the use of except in Python instead of catch in Java.
Checked Exceptions: Java has "checked exceptions," which must be explicitly caught or declared in the method signature, a feature Python does not have.
else block: Python includes an else block (executed only upon successful completion of the try block), which Java lacks a direct equivalent for.
try-with-resources: Java has a specific try-with-resources statement for automatically closing resources like files, a pattern handled differently (often using context managers) in Python.
~~~
