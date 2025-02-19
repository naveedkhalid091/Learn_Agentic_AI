from crewai.flow.flow import Flow , start , listen
import time

def function1():
    print("Hello World")



class SimpleFlow(Flow):

        @start()    # Indicates the starting function/tool.
        def function1(self):
            print("step1...!")
            time.sleep(3)   # This is just to show that the function will run afer 3 seconds of start.

        @listen(function1)   # Wait for the function1 to finish and then start this function.
        def function2(self):
            print("step2...!")
            time.sleep(3)   # This is just to show that the function will run afer 3 seconds of function1.

        @listen(function2)   # Wait for the function2 to finish and then start this function.
        def function3(self):
            print("step3...!")
            time.sleep(3)  # This is just to show that the function will run afer 3 seconds of function2.


def chain():
    obj=SimpleFlow()
    obj.kickoff()  ## Where kickoff is the inherent method is Flow parameter which we placed in SimplFlow()

