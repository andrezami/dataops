import requests
from config import configs_work

for key in configs_work:
        response = requests.get(configs_work[key]["endpoint"])
        assert response.status_code == 200