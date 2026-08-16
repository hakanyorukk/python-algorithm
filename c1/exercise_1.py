from enum import Enum

class ServerError(Exception):
    pass

class ServerOfflineError(ServerError):
    pass

class AppAlreadyDeployedError(ServerError):
    pass

class AppNotFoundError(ServerError):
    pass

class Status(Enum):
    ONLINE = 1
    OFFLINE = 2

class Server:
    def __init__(self, name):
        self.name = name
        self.status = Status.ONLINE
        self.apps = []

    def __str__(self):
        return f"name: {self.name}, status: {self.status}"

    def deploy(self, app_name):
        if self.status == Status.OFFLINE:
            raise ServerOfflineError(f"{self.name} is offline")
        if app_name in self.apps:
            raise AppAlreadyDeployedError(f"{app_name} already deployed on {self.name}")

        self.apps.append(app_name)

    def remove(self, app_name):
        if app_name in self.apps:
            self.apps.remove(app_name)
        else:
            raise AppNotFoundError(f"{app_name} is not deployed on {self.name}")

    def take_offline(self):
        self.status = Status.OFFLINE

    def bring_online(self):
        self.status = Status.ONLINE

    @property
    def app_count(self):
        return len(self.apps)

    @property
    def is_online(self):
        if self.status == Status.ONLINE:
            return True
        return False

class ServerFleet:

    def __init__(self):
        self.servers = {}

    def add_server(self, server):
        self.servers[server.name] = server

    def deploy_to_all(self,app_name):
        success_count = 0
        for server in self.servers.values():
            if server.status != Status.ONLINE:
                continue
            try:
                server.deploy(app_name)
                success_count+=1
            except AppAlreadyDeployedError:
                continue
        return success_count

    def find_server(self, name):
        return self.servers.get(name)

    def offline_servers(self):
        offline_servers = []
        for server in self.servers.values():
            if not server.is_online:
                offline_servers.append(server.name)
        return offline_servers

    def total_apps(self):
        return sum(s.app_count for s in self.servers.values())

try:
    web1 = Server("web-01")
    web1.deploy("api")
    web1.deploy("api")        # should fail — already deployed
    web1.take_offline()
    web1.deploy("worker")
except AppAlreadyDeployedError as e:
    print(f"expected failure: {e}")
except ServerOfflineError as e:
    print(f"expected failure: {e}")