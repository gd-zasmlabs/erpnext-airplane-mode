import frappe

def get_context(context):
    context.items = frappe.get_all(
        "Airplane Flight",
        filters={"is_published": 1},
        fields=[
            "name",
            "route",
            "source_airport",
            "destination_airport",
            "date_of_departure",
            "departure_time",
            "duration"
        ],
        order_by="date_of_departure asc"
    )
    return context
