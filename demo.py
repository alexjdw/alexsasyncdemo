import aiohttp
import asyncio
import re
import time

# This code is for demonstration of the following:
# async def
# async with
# asnyc for
# async generators

# There are better ways to organize this code!
# For instance, task.add_done_callback() would allow me to schedule
# the regex directly after the HTTP get finishes. This would save a lot of
# lines and probably be a bit faster. The point of the demo is to show the
# speed gains and provide an example of the task/event loop model, so I
# elected not to dive too deep.

pages = [
    "https://www.wuxiaworld.com/novel/against-the-gods",
    "https://www.wuxiaworld.com/novel/demon-hunter",
    "https://www.wuxiaworld.com/novel/martial-god-asura",
    "https://www.wuxiaworld.com/novel/monarch-of-evernight",
    ]

# Takes an iterator and wraps it in another async iterator.
# This is for example only and is awful, don't do this.
async def iter_to_aiter(i):
    while True:
        try:
            yield(next(i))
        except StopIteration:
            break


# Coroutine that gets a webpage. Note the use of "async with", which can handle
# the future object created by session.get to properly close the connection.
async def get_webpage(session, page):
    async with session.get(page) as response:
        print("Getting " + str(response.url))

        # Await a response before returning.
        return await response.text()


# Coroutine that handles our regular expression search.
async def get_chapters(task):
    result = []
    expr = r'<span>((\w|[\-\*\.\?\:]|\s)*)</span>'

    # Immediately stop execution and await our task.
    await task
    print("Scrape completed, begining RegEx...")

    async for match in iter_to_aiter(re.finditer(expr, task.result())):
        result.append(match.group(1))

    return result


# This is the main code that will queue up all of the task objects,
# then it will await their results from our little get_webpage > get_chapters
# pipeline we've set up, then print a little sample of the results
# to show it's working.
async def wuxia_scrape_chapters(pagelist):
    async with aiohttp.ClientSession() as session:
        pagetasks = []
        for page in pagelist:
            pagetasks.append(
                    asyncio.ensure_future(get_webpage(session, page))
                    )
        print("Pages are being scraped...")

        # Make more tasks to handle the result of the above tasks!
        # This is executing concurrently while we're waiting for the pages
        # to be scraped!
        chapters = []
        for task in pagetasks:
            chapters.append(
                    asyncio.ensure_future(get_chapters(task))
                    )
        print("Chapter routine initialized...")

        for ch in chapters:
            await ch
            print("Next Book: ")
            print(ch.result()[0:2])  # prints the first few chapters


# Enter the event loop
loop = asyncio.get_event_loop()
print("Loop created...")
t = time.clock()
loop.run_until_complete(wuxia_scrape_chapters(pages))
print(time.clock() - t)
