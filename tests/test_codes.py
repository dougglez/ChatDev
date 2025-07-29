import os
import sys
import types

# Stub heavy dependencies for chatdev.utils imported by chatdev.codes
camel = types.ModuleType('camel')
camel.messages = types.ModuleType('camel.messages')
camel.messages.system_messages = types.ModuleType('camel.messages.system_messages')
class SystemMessage:
    pass
camel.messages.system_messages.SystemMessage = SystemMessage
sys.modules['camel'] = camel
sys.modules['camel.messages'] = camel.messages
sys.modules['camel.messages.system_messages'] = camel.messages.system_messages

visualizer_app = types.ModuleType('visualizer.app')
def send_msg(role, content):
    pass
visualizer_app.send_msg = send_msg
sys.modules['visualizer.app'] = visualizer_app

ROOT = os.path.dirname(os.path.dirname(__file__))
sys.path.append(ROOT)

from chatdev.codes import Codes


def test_format_code_removes_empty_lines():
    c = Codes()
    formatted = c._format_code("line1\n\nline2\n")
    assert formatted == "line1\nline2"


def test_load_from_hardware(tmp_path):
    file = tmp_path / "sample.py"
    file.write_text("print('hi')\n\n")
    codes = Codes()
    codes._load_from_hardware(str(tmp_path))
    assert "sample.py" in codes.codebooks
    assert codes.codebooks["sample.py"] == "print('hi')"


def test_get_codes_single_file():
    codes = Codes()
    codes.codebooks["a.py"] = "print('a')"
    expected = "a.py\n```python\nprint('a')\n```\n\n"
    assert codes._get_codes() == expected
