import command
from gigex import Gigex

class Sync():
    def __init__(self, ip):
        self.ip = ip
        self.gx = Gigex(self.ip)

        with self.gx:
            cmd = command.backend_network_set()
            self.gx.spi_query(cmd)

    def rst(self):
        with self.gx:
            cmd = command.CMD_EMPTY
            resp = self.gx.spi_query(cmd)
            return resp == (command.CMD_EMPTY | 0x1)

    def get_status(self):
        with self.gx:
            cmd = command.backend_status(0)
            resp = self.gx.spi_query(cmd)
            return resp == cmd
