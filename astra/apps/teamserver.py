import time
from ...framework.application import Application
from astra.framework.server import TeamServer


class TeamserverApplication(Application):
    @staticmethod
    def help(parser):
        """
        A team server, from which to launch all operations.
        """

    def run(self):
        self.services.load()
        ts = TeamServer()
        ts.start()

        try:
            while True:
                time.sleep(10)
        except KeyboardInterrupt:
            print('Caught interrupt, exiting...')

        finally:
            ts.stop()

        print('Goodbye.')