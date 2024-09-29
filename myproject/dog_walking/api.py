from ninja import NinjaAPI

from dog_walking.models import Strolls
from dog_walking.schemes import WalkData
from datetime import date

api = NinjaAPI()


@api.post("/new_strolls/")
def create_walk_data(request, data: WalkData):
    existing_count = Strolls.objects.filter(day=data.day, time_in_day=data.time_in_day).count()
    if existing_count >= 2:
        return {"detail": "Выберите другую дату или время"}
    else:
        walk_data = Strolls.objects.create(
            apartment_number=data.apartment_number,
            animal_name=data.animal_name,
            day=data.day,
            time_in_day=data.time_in_day

        )
        return {"id": walk_data.id,
                "apartment_number": data.apartment_number,
                "animal_name": data.animal_name,
                "day": data.day,
                "time_in_day": data.time_in_day}


@api.get("/strolls/")
def get_strolls(request, day: date):
    strolls_in_day = Strolls.objects.filter(day=day)
    strolls_list = []
    for strol in strolls_in_day:
        strol_in_day = WalkData(
            apartment_number=strol.apartment_number,
            animal_name=strol.animal_name,
            day=strol.day,
            time_in_day=strol.time_in_day
        )
        strolls_list.append(strol_in_day)
    return strolls_list
