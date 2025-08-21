from .models import Inputs


def get_last_input_id() -> int:
    """Get last input field ID"""

    last_entry_id = Inputs.objects.values("id").last()
    return 1 if last_entry_id is None else last_entry_id["id"]


def create_input(data: dict) -> None:
    """Create new entry to Inputs table"""

    Inputs.objects.create(input_field=data)
