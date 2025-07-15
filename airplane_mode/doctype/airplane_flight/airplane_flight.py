from frappe.website.website_generator import WebsiteGenerator

class AirplaneFlight(WebsiteGenerator):
    pass

# Optional: you can specify which field is used to check publication
AirplaneFlight.website = type('Website', (), {"condition_field": "is_published"})
