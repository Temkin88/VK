from typing import Union

from web.project.db import Account_Pydantic


def account_dict_modify(
        account: Account_Pydantic
) -> dict[str, Union[str, int, None]]:
    account_dict = account.dict()
    account_dict['account_id'] = account_dict['id']
    account_dict['sms_code'] = account_dict['code']
    return account_dict
