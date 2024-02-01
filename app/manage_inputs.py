import click
from flask.cli import with_appcontext
from flask import current_app

def register_commands(app, db):
    @app.cli.command("add_guest")
    @click.argument("name")
    @click.argument("balance", type=float)
    @with_appcontext
    def add_guest(name, balance):
        from .models import Guest
        guest = Guest(name=name, balance=balance)
        db.session.add(guest)
        db.session.commit()
        click.echo(f"Added guest {name} with balance {balance}")


    @app.cli.command("add_drink")
    @click.argument("name")
    @click.argument("price", type=float)
    @with_appcontext
    def add_drink(name, price):
        from .models import Drink
        drink = Drink(name=name, price=price)
        db.session.add(drink)
        db.session.commit()
        click.echo(f"Added drink {name} with price {price}")

    @app.cli.command("add_activity")
    @click.argument("name")
    @click.argument("payoff", type=float)
    @with_appcontext
    def add_activity(name, payoff):
        from .models import Activity
        activity = Activity(name=name, payoff=payoff)
        db.session.add(activity)
        db.session.commit()
        click.echo(f"Added activity {name} with payoff {payoff}")

    @app.cli.command("add_transaction")
    @click.argument("guest_id", type=int)
    @click.argument("incoming", type=bool)
    @click.argument("amount", type=float)
    @with_appcontext
    def add_transaction(guest_id, incoming, amount):
        from .models import Transaction
        transaction = Transaction(guest_id=guest_id, incoming=incoming, amount=amount)
        db.session.add(transaction)
        db.session.commit()
        click.echo(f"Added transaction for guest_id {guest_id} with amount {amount} {'earned' if incoming else 'spent'}")
