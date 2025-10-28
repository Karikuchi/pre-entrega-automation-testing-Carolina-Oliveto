import pytest
from utils import iniciar_driver

@pytest.fixture
def driver():
    driver = iniciar_driver()
    yield driver
    driver.quit()
