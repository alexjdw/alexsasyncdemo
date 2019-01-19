# AsyncIO Demo
My demo for asyncio and aiohttp in python.

This is a small collection of demo files intended to be paired with a short video. I decided I didn't like the sound of my own voice, to the video is going in the vault for now :)

# What's it do, then?

The primary use case for asynchronous code is that it allows the execution of other code while awaiting data from an external source. I included a needtoknow.py file for new users of the library which should cover everything you need to know if you're interested in learning a bit about async in Python.

The project compares a linear implementation of a web scraper to an asynchronous execution of the same code. The linear execution makes HTTP GET requests, waits for them to resolve, and then makes the next request. The async file makes each request up front and then handles the results when they come back. Both functions print some status messages and log the total time it takes them to execute, allowing for a speed comparision. Results vary based on connection, but the async version is approximately n times faster than the synchronous version, where n is the number of requests.
