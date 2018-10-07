'''
#############################
###    GUIDE TO ASYNCIO   ###
#############################


Key concepts:

asynico.get_event_loop()
   Returns an event loop.
   Essentially a while loop that manages executing multiple coroutines/tasks
concurrently. Async objects report their status to the event loop as either
blocked or not blocked or complete in some way. For the programmer, the exact
details are not needed. Just know that the loop is going to try to run
anything that is not waiting for an await statement to complete or manually
blocked in some other way. (Avoid manual blocks if possible!)

asyncio.ensure_future(coroutine)
  This function takes a coroutine and wraps it in a task object, which is
ensured by the event loop to complete before the event loop exits.

Tasks:                https://docs.python.org/3/library/asyncio-task.html
  A task has the following key methods:
  await task
     I'm including this here as the method.
  task.result()
     Returns the result of the task. Invoking the task directly will not give
  you the result! Returns some gibberish if no result yet.
  task.cancel()
     Closes the task and blocks execution.
  task.add_done_callback(callback, *, context=None)
     Calls a function when task is done with * as its arguments.

  There are a few other helper methods for tasks, check them out for ideas on
  how to pretzel up your code to hell by manually managing your
  tasks!
'''
