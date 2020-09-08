from prefect.core.task import Task


class Layer(Task):
    def __init__(self, client=None, **kwargs): 
        super().__init__(**kwargs)