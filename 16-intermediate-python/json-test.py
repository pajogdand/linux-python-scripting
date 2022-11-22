import json
mydict ={"output": {"sink": {"path": "stmBufferFiles/fm0_1.bin", "type": "file", "mode": "overwrite", "max_size": 1073741824}, "format": "raw"}, "subsystem_name": "fm0", "type": "snapshot", "name": "asHandlerAuto1_fm0"}

print(json.dumps(mydict))