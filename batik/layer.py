from dask.distributed import ActorFuture
import logging


class Layer:
    def __init__(self, layer_args={}, **kwargs): 
        self.layer_args = layer_args
    def _run(self, payload):
        if isinstance(payload, ActorFuture):
            return self.run(payload.result())
        else:
            return self.run(payload)



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
