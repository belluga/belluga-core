# import asyncio
# from threading import Thread
# import time

# from belluga.belluga_connection import BellugaConnection


# class ConnectionRequestModel():
#     def __init__(self, start_loop: asyncio.AbstractEventLoop):
#         self.start_loop = start_loop


#     def set_update_loop(self):
#         self.update_loop = asyncio.new_event_loop()
#         self.update_loop.call_soon_threadsafe(self.on_change)
#         t = Thread(target=self.start_loop, args=(self.update_loop))
#         t.start()
#         time.sleep(0.25)

#     def on_change(self):
#         print("have changed")
#         _belluga_connection = BellugaConnection()
        
#         for document in _belluga_connection.connection.watch():
#             print(document)

