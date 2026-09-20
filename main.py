import sys
import json
from rich.console import Console
from rich.panel import Panel
from rich.align import Align

from scanner import scan
from report import print_report, save_json


console = Console()

BANNER = r"""
   _____                     _____                 
  / ____|                   / ____|                
 | (___   ___  ___ _   _ _ __| (___   ___ __ _ _ __  
  \___ \ / _ \/ __| | | | '__|\___ \ / __/ _` | '_ \ 
  ____) |  __/ (__| |_| | |   ____) | (_| (_| | | | |
 |_____/ \___|\___|\__,_|_|  |_____/ \___\__,_|_| |_|
                                                     
        [ by @annisadanish — scan responsibly ]
"""


def print_banner():
    console.print(Align.center(f"[bold cyan]{BANNER}[/bold cyan]"))


def main():
    print_banner()

    if len(sys.argv) < 2:
        console.print("[yellow]Usage:[/yellow] python main.py <domain> [--json]")
        console.print("[dim]Example: python main.py example.com --json[/dim]")
        sys.exit(1)

    target = sys.argv[1]
    console.print(f"\n[bold]Scanning[/bold] [yellow]{target}[/yellow] ...\n")

    data = scan(target)
    print_report(data)

    # Watermark
    console.print(
        "\n[dim]─────────────────────────────────────────────[/dim]"
    )
    console.print(
        "[dim]SecureScan v1.0 • Built by[/dim] [bold cyan]@annisadanish[/bold cyan]"
    )
    console.print(
        "[dim]GitHub: github.com/annisadanish/securescan[/dim]"
    )
    console.print(
        "[dim]─────────────────────────────────────────────[/dim]\n"
    )

    if "--json" in sys.argv:
        save_json(data)


if __name__ == "__main__":
    main()
