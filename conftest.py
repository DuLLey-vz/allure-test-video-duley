import pathlib
import allure
import pytest
# from playwright.sync_api import sync_playwright



@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_teardown(item, nextitem):
    yield

    try:
        # Get the output directory for the test
        artifacts_dir = item.funcargs.get("output_path")
        if artifacts_dir:
            artifacts_dir_path = pathlib.Path(artifacts_dir)

            if artifacts_dir_path.is_dir():
                for file in artifacts_dir_path.iterdir():
                    # Find the video file and attach it to Allure Report
                    if file.is_file() and file.suffix == ".webm":
                        allure.attach.file(
                            file,
                            name=file.name,
                            attachment_type=allure.attachment_type.WEBM,
                        )

    except Exception as e:
        print(f"Error attaching video: {e}")

# @pytest.fixture
# def page():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)
#         context = browser.new_context()
#         page = context.new_page()
#         yield page
#         browser.close()