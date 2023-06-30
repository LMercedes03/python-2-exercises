from dataclasses import dataclass
from pprint import pprint


@dataclass(frozen=False, order=True)
class Invoice:
    invoice_id: str
    user_id: str
    amount: str
    paid: str


data = [
    "1, 2322, 10.00, False",
    "2, 5435, 60.30, True",
    "3, 3433, 15.63, False",
    "4, 8439, 12.77, False",
    "5, 3424, 11.34, False",
]
invoices = []
for item in data:
    invoice_data = item.split(", ")
    invoice = Invoice(*invoice_data)
    invoices.append(invoice)

pprint(invoices)
