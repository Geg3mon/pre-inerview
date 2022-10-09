import typer
from typing import Optional, List

from task_2 import __app_name__, __version__
from task_2.solution import Todo


app = typer.Typer()


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()


@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    )
) -> None:
    return


@app.command(name="add_task")
def add_task(description: str = typer.Argument(...),) -> None:
    """Add a new task with a DESCRIPTION."""
    response = Todo.add_task(Todo(description))
    if response:
        typer.secho(
            f"""to-do: "{description}" was added """,
            fg=typer.colors.GREEN,
        )
    else:
        typer.secho(
            f"""to-do: "{description}" already exists """,
            fg=typer.colors.RED,
        )


@app.command(name="add_tasks")
def add_tasks(description: str = typer.Argument(...),) -> None:
    """Add tasks with DESCRIPTION.\n
    - EXAMPLE:\n
    - python3 -m task_2 add_tasks "buy","some"\n
    - You shoul add tasks in "" and separate them with comma (without spaces)"""
    args = description.split(',')
    response = Todo.add_tasks(*args)
    if response:
        typer.secho(
            f"""to-do: "{args}" was added """,
            fg=typer.colors.GREEN,
        )
    else:
        typer.secho(
            f"""to-do: "{args}" already exists """,
            fg=typer.colors.RED,
        )


@app.command(name="mark_done")
def mark_done(description: str = typer.Argument(...),) -> None:
    """Mark task completed successfully"""
    response = Todo.done_task(Todo(description))
    if response:
        typer.secho(
            f"""Task "{description}" completed successfully""",
            fg=typer.colors.GREEN,
        )
    else:
        typer.secho(
            f"""There is no task "{description}" in todo list, add task
You can add task with command <python3 -m task_2 add_task "{description}"> """,
            fg=typer.colors.RED,
        )


@app.command(name="mark_tasks_done")
def mark_tasks_done(description: str = typer.Argument(...),) -> None:
    """Mark tasks completed successfully"""
    args = description.split(',')
    for task in args:
        mark_done(task)

@app.command(name="remove_task")
def remove_task(description: str = typer.Argument(...),) -> None:
    """Remove task from list"""
    response = Todo.remove_task(Todo(description))
    if response:
        typer.secho(
            f"""to-do: "{description}" was removed """,
            fg=typer.colors.GREEN,
        )
    else:
        typer.secho(
            f"""There is no task: "{description}" """,
            fg=typer.colors.RED,
        )


@app.command(name="remove_tasks")
def remove_tasks(description: str = typer.Argument(...),) -> None:
    """Remove tasks from list"""
    args = description.split(',')
    for task in args:
        remove_task(task)


@app.command(name="todo_list")
def todo_list() -> None:
    """Show todo list"""
    response = Todo.show_todo()


@app.command(name="done_list")
def done_list() -> None:
    """Show list of done tasks"""
    response = Todo.show_done()
