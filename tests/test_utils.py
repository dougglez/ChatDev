import os
import sys
import types

# Prepare dummy modules so chatdev.utils can be imported without heavy deps
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

from chatdev.utils import convert_to_markdown_table, escape_string


def test_convert_to_markdown_table():
    table = convert_to_markdown_table([('a', '1'), ('b', '2')])
    assert table == "| Parameter | Value |\n| --- | --- |\n| **a** | 1 |\n| **b** | 2 |"


def test_escape_string_html():
    assert escape_string('<b>hi</b>\nnew') == 'hi new'
