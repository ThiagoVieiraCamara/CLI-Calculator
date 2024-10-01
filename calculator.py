import typer
from rich import print as println
from typing_extensions import Annotated

def calculator(a: Annotated[float, typer.Argument(help="1st value", show_default=False)],
                b: Annotated[float, typer.Argument(help="2nd value", show_default=False)],
                minus: Annotated[bool, typer.Option("-m", "--minus",help="Subtraction operation", show_default=False)] = False, 
                times: Annotated[bool, typer.Option("-mt", "--mult",help="Multiplication operation", show_default=False)] = False, 
                divide:Annotated[bool, typer.Option("-dv", "--divide",help="Division operation", show_default=False)] = False) -> float:
    """
    Simple mafs, just enter two values (a and b), default is sum.
    """
    if minus:
        subtract = a - b
        return println(f"[green]{subtract}[green]")
    elif times:
        multiplication = a * b
        return println(f"[blue]{multiplication}[blue]")
    elif divide:
        divided = a / b
        return println(f"[red]{divided}[red]")
    else:
        sum = a+b
        return println(f"[yellow]{sum}[yellow]")

if __name__ == "__main__":
    typer.run(calculator)
