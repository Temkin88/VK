import base64
import json

# FILTER_BY_SUITE = [{"id": "cfv.-5", "value": [61903], "label": ["CritWay_CheckList"], "type": "longArray"}]
FILTER_BY_SUITE = []
FILTER_BY_SUITE_BASE64 = base64.b64encode(json.dumps(FILTER_BY_SUITE).encode(encoding='utf-8')).decode(encoding='utf-8')
