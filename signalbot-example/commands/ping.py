import scores as scores
from signalbot import Command, Context
ans = scores.fun()
class PingCommand(Command):
    def describe(self) -> str:
        return "Prints Cricket Info\nAvailable Commands are: cricinfo list"

    async def handle(self, c: Context):
        command = c.message.text
        if command == "cricinfo" or command == "cricinfo help":
            await c.send(self.describe())
            return

        if command == "cricinfo list":
            await c.send(ans)
            return
    

