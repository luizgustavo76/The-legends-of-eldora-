import tloemod
tloe = tloemod.main()
class ModAPI:
    def __init__(self):
        self.Global = tloe.get_global_scope()

    def get(self, name):
        return self.Global.get(name)

    def set(self, name, value):
        self.Global[name] = value

    def call(self, func_name, *args, **kwargs):
        if func_name in self.Global and callable(self.Global[func_name]):
            return self.Global[func_name](*args, **kwargs)
class TLOEContext:
    def __init__(self):
        self.game = tloe
        self.player = tloe.dados_jogador
        self.inventory = tloe.salvamento_dados

ctx = TLOEContext()
