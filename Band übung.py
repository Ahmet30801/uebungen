band = dict()
band["vocal"] = "Hans Peter"
band["guitar"] = "Jimmy"
band["bass"] = "Lemmy"
band["drum"] = "Stefan"

band["drum"] = "Rod"

band.pop("guitar")
band.pop("bass")

print(band)