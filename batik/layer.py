from dask.distributed import ActorFuture
import logging
import os

# TODO: Log results to rabbitmq if present!

class Layer:
    def __init__(self, layer_args={}, **kwargs): 
        self.layer_args = layer_args
    def _run(self, payload):
        if isinstance(payload, ActorFuture):
            res = self.run(payload.result())
        else:
            res = self.run(payload)
        
        return res
        



class Actor:
    def __init__(self, layer_args={}, **kwargs): 
        self.layer_args = layer_args
    def _run(self, payload):
        try: 
            if isinstance(payload, ActorFuture):
                return self.run(payload.result())
            else:
                return self.run(payload)
        except Exception as e:
            logging.exception('')
