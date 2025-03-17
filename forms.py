def get_contact_message_model():
    # Delay model import until it is needed
    from django.apps import apps
    return apps.get_model('main', 'ContactMessage')

# Usage example:
# ContactMessage = get_contact_message_model()

