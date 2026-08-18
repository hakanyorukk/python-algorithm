from enum import Enum

from c1.exercise_1 import web1


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

    def deploy(self, app_name):
        if self.status is Status.OFFLINE:
            raise ServerOfflineError("Server is offline!")
        if app_name in self.apps:
            raise AppAlreadyDeployedError(f"{app_name} already deployed on {self.name}")
        self.apps.append(app_name)

    def remove(self, app_name):
        if not app_name in self.apps:
            raise AppNotFoundError(f"{app_name} not in the {self.name} server")
        self.apps.remove(app_name)

    def take_offline(self):
        self.status = Status.OFFLINE

    def bring_online(self):
        self.status = Status.ONLINE

    @property
    def app_count(self):
        return len(self.apps)

    def __str__(self):
        return f"Server {self.name} has {self.app_count} servers."

class ServerFleet:

    def __init__(self):
        self.servers = {}
    def add_server(self, server):
        self.servers[server.name] = server

    def deploy_to_all(self, app_name):
        success_count = 0
        for server in self.servers.values():
            if server.status is not Status.ONLINE:
                continue
            try:
                server.deploy(app_name)
                success_count+=1
            except AppAlreadyDeployedError:
                continue

    def find_server(self,name):
        for server in self.servers.values():
            if server.name == name:
                return server
        return None

    def offline_servers(self):
        offline_servers = []
        for server in self.servers:
            if server.status == Status.OFFLINE:
                offline_servers.append(server.name)
        return offline_servers

    def total_apps(self):
        return sum(c.app_count for c in self.servers.values())

try:
    fleet = ServerFleet()
    web1 = Server("web-01")
    web1.deploy("api")
 #   web1.deploy("api")        # should fail — already deployed
   # web1.take_offline()
    web1.deploy("worker")
    fleet.add_server(web1)
    fleet.deploy_to_all("build")
    print(fleet.total_apps())
except AppAlreadyDeployedError as e:
    print(f"expected failure: {e}")
except ServerOfflineError as e:
    print(f"expected failure: {e}")

