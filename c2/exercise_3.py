def always_pass():
    return True

def always_fail():
    return False

class PipelineStage:

    def __init__(self, name, action):
        self.name = name
        self.action = action

    def run(self):
        return self.action()

class Pipeline:
    def __init__(self):
        self.stages = []
        self.failed_stage = None
        self.has_run = False
        self.executed = []

    def add_stage(self, stage):
        self.stages.append(stage)

    def run(self):
        self.has_run = True
        for stage in self.stages:
            if stage.run():
                self.executed.append(stage.name)
            else:
                self.failed_stage = stage.name
                break

    @property
    def status(self):
        if self.failed_stage is None:
            return "success"
        if not self.has_run:
            return "not run"
        return "failed"

    @property
    def last_failed_stage(self):
        return self.failed_stage

p = Pipeline()
p.add_stage(PipelineStage("build", always_pass))
p.add_stage(PipelineStage("test", always_fail))
p.add_stage(PipelineStage("deploy", always_pass))
p.run()
print(p.status)
print(p.last_failed_stage)