from rich import print
from rich.pretty import Pretty
from rich.panel import Panel
from rich.pretty import pprint

# pprint(locals())
# pprint(["eggs", "ham"], expand_all=True)
# pprint(locals(), max_length=2)
# pprint("Where there is a Will, there is a Way", max_string=21)


pretty = Pretty(locals())
test = "this is a test"
panel = Panel(test)
print(panel)
