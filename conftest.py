#All the Basic Configuration
from datetime import datetime
from pathlib import Path
import pytest
from selenium import webdriver

BaseUrl = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
Username="Admin"
Password="admin123"

@pytest.fixture(scope="class",autouse=True)
def browser_setup(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    request.cls.driver = driver  # ✅ attach driver to test class
    yield driver
    driver.quit()


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    # Create folder name with today's date (e.g., 20250902)
    today = datetime.now()
    report_dir = Path("hrmreports", today.strftime("%Y%m%d"))
    report_dir.mkdir(parents=True, exist_ok=True)
    # Create report file with timestamp in name
    report_file = report_dir / f"Report_{today.strftime('%Y%m%d%H%M')}.html"
    # Configure pytest-html
    config.option.htmlpath = str(report_file)
    config.option.self_contained_html = True

def pytest_html_report_title(report):
    report.title = "HRM Test Report"