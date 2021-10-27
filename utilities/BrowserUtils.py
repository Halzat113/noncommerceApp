from utilities.readProperties import get_project_root


def takeScreenshot(driver, name):
    driver.save_screenshot(get_project_root() + f"\\Screenshots\\{name}.png")