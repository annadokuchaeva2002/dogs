from pydantic import BaseModel, Field
from datetime import date


class WalkData(BaseModel):
    apartment_number: int
    animal_name: str
    day: date
    time_in_day: str = Field(
        default="hh:mm",
        pattern=r'^(0[7-9]|1\d|2[0-2]):(00|30)|(23 : 00)'
    )

