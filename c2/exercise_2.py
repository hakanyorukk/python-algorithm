def always_ran():
    return True

def always_fail():
    return False

class PipelineStage:

    def __init__(self,name, action):
        self.name = name
        self.action = action

    def run(self):
        return self.action()

class Pipline:

    def __init__(self):
        self.stages = []
        self.executed = []
        self.has_run = False
        self.last_failed = None

    def add_stage(self, stage):
        self.stages.append(stage)

    def run(self):
        self.has_run = True
        for stage in self.stages:
            if stage.run():
                self.executed.append(stage.name)
            else:
                self.last_failed = stage.name
                break

    @property
    def last_failed_stage(self):
        return self.last_failed

    @property
    def status(self):
        if not self.has_run:
            return "not run"
        elif self.last_failed is None:
            return "failed"
        return "success"

p = Pipline()
p.add_stage(PipelineStage("build", always_ran))
p.add_stage(PipelineStage("test", always_ran))
p.add_stage(PipelineStage("deploy", always_fail))
p.run()

print(p.last_failed_stage)