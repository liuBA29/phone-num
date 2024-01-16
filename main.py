import phonenumbers as ph
from phonenumbers import geocoder, carrier
from rich import print
from time import sleep
from rich.console import Console

console = Console()
tasks = [f"{n} задача ча ча ча" for n in range(1, 15)]
with console.status("[bold green] ...doing...[/bold green]") as status:
    while tasks:
        task = tasks.pop(0)
        sleep(1)
        console.log(f"{task} !")
    console.log(f"[bold blue]DONE![/bold blue]")



phone=ph.parse('+353857290422')
is_valid=ph.is_valid_number(phone)
ph_type=ph.number_type(phone)
form_ph=ph.format_number(phone, ph.PhoneNumberFormat.INTERNATIONAL)
geo = geocoder.country_name_for_number(phone, 'en')
desc = geocoder.description_for_number(phone, 'en')
carrier = carrier.name_for_number(phone, 'en')

print(carrier)
print("Hello, [bold magenta] Stupid [/bold magenta] ! :smile:")
