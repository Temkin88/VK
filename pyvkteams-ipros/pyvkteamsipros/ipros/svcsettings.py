class SvcSettings:
    class Svc:
        def __init__(self):
            self.on_init_async = None
            self.on_shutdown = None

    def __init__(self):
        self.settings = {}

    def __getitem__(self, svcname: str):
        if svcname not in self.settings:
            self.settings[svcname] = self.Svc()
        return self.settings[svcname]

    def __contains__(self, item):
        return item in self.settings
