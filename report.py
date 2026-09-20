"""
SecureScan — report formatting
Author: Annisa Danish (@annisadanish)
"""

import json
from rich.console import Console
from rich.table import Table
from rich.panel import Panel


console = Console()


def print_report(data):
    console.print(Panel.fit(
        f"[bold cyan]SecureScan Report[/bold cyan]\n"
        f"Target: [yellow]{data['target']}[/yellow]\n"
        f"URL: {data['url']}",
    ))

    # Headers
    h = data["headers"]
    if h["error"]:
        console.print(f"[red]Headers check failed:[/red] {h['error']}")
    else:
        console.print(f"\n[bold]HTTP Status:[/bold] {h['status_code']}")
        table = Table(title="Security Headers")
        table.add_column("Header", style="cyan")
        table.add_column("Status", style="bold")
        table.add_column("Value", overflow="fold")

        for name in h["headers_found"]:
            table.add_row(name, "[green]FOUND[/green]", h["headers_found"][name][:80])
        for name in h["headers_missing"]:
            table.add_row(name, "[red]MISSING[/red]", "-")

        console.print(table)

    # SSL
    s = data["ssl"]
    console.print("\n[bold]SSL Certificate[/bold]")
    if s["error"]:
        console.print(f"[red]SSL check failed:[/red] {s['error']}")
    else:
        console.print(f"  Issuer: [cyan]{s['issuer'].get('organizationName', 'N/A')}[/cyan]")
        console.print(f"  Expires: {s['expires']}")
        color = "green" if s["days_left"] and s["days_left"] > 30 else "red"
        console.print(f"  Days left: [{color}]{s['days_left']}[/{color}]")

    # Cookies
    c = data["cookies"]
    console.print("\n[bold]Cookies[/bold]")
    if not c["cookies"]:
        console.print("  [dim]No cookies set[/dim]")
    else:
        ctable = Table()
        ctable.add_column("Name", style="cyan")
        ctable.add_column("Secure")
        ctable.add_column("HttpOnly")
        ctable.add_column("Domain")
        for ck in c["cookies"]:
            ctable.add_row(
                ck["name"],
                "[green]yes[/green]" if ck["secure"] else "[red]no[/red]",
                "[green]yes[/green]" if ck["httponly"] else "[red]no[/red]",
                ck.get("domain") or "-",
            )
        console.print(ctable)

    console.print("\n[dim italic]— SecureScan by @annisadanish —[/dim italic]")


def save_json(data, filename="report.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)
    console.print(f"\n[green]Report saved to {filename}[/green]")
