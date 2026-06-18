import pathlib
import logging


logger = logging.getLogger("allure.check_duplicates")
logging.basicConfig(level=logging.INFO)


tests_path = pathlib.Path("tests")


allure_IDS_list = []
allure_IDS_set = set()


for path in tests_path.glob("**/*.py"):
    if "__pycache__" in path.parts:
        continue
    for line in filter(
        lambda x: "allure.id" in x,
        path.read_text("utf-8").splitlines(),
    ):
        if "('')" in line or '("")' in line:
            logger.warning(f"Broken allure ID in file {path}")
        line = line.replace('"', "'").strip()
        allure_IDS_list.append(line)

for allure_id in set(allure_IDS_list):
    if allure_IDS_list.count(allure_id) > 1:
        logger.warning(f"Duplicated allure id: {allure_id}")
