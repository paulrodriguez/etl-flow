from .OperatorInterface import OperatorInterface

class Composite(OperatorInterface):
    def __init__(self, jobs=[]):
        self.jobs = jobs

    def execute(self, payload, subject={}):
        for job in self.jobs:
            if not isinstance(job, OperatorInterface):
                raise Exception('job must be instance of OperatorInterface')

            payload = job.execute(payload, subject)

        return payload
