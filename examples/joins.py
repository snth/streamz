from streamz import Stream, union, combine_latest, zip_latest, zip
import asyncio
from tornado.platform.asyncio import AsyncIOMainLoop
AsyncIOMainLoop().install()


s1 = Stream()
s1.rate_limit(1.0).map(lambda x: x+1).sink(s1.emit)
s2 = Stream()
s2.rate_limit(1.5).map(lambda x: x+1).sink(s2.emit)

#s3 = union(s1, s2)
#s3 = combine_latest(s1, s2)
#s3 = zip_latest(s1, s2)
s3 = zip(s1, s2)
s3.sink(print)

s1.emit(0)                          # seed with initial values
s2.emit(100)                          # seed with initial values


def run_asyncio_loop():
    loop = asyncio.get_event_loop()
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        loop.close()

run_asyncio_loop()
