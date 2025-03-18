from part_1.conf import settings
from part_1.utils.__pycache__ import create_url

result = create_url.create_url(settings.NAME, settings.MAIN_URL)
print(result)
