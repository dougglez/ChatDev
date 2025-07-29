import sys
import types

dummy = types.ModuleType("dummy")
for name in ["openai", "markdown", "tiktoken", "pandas"]:
    if name not in sys.modules:
        sys.modules[name] = dummy
dummy.OpenAI = object
sys.modules.setdefault("colorama", dummy)
dummy.Fore = object
dummy.Style = object
sys.modules.setdefault("faiss", dummy)
sys.modules.setdefault("yaml", dummy)
sys.modules.setdefault("easydict", dummy)
dummy.EasyDict = dict

# Provide minimal Flask stub
if "flask" not in sys.modules:
    flask_stub = types.ModuleType("flask")

    class _Flask:
        def __init__(self, *args, **kwargs):
            import logging
            self.logger = logging.getLogger("dummy")

        def route(self, *args, **kwargs):
            def decorator(fn):
                return fn
            return decorator

    flask_stub.Flask = _Flask
    flask_stub.send_from_directory = lambda *a, **kw: None
    flask_stub.request = object()
    flask_stub.jsonify = lambda *a, **kw: None
    sys.modules["flask"] = flask_stub

# Stub camel package with minimal structure
camel_pkg = types.ModuleType("camel")
camel_messages_pkg = types.ModuleType("camel.messages")
system_messages_pkg = types.ModuleType("camel.messages.system_messages")
system_messages_pkg.SystemMessage = object

sys.modules.setdefault("camel", camel_pkg)
sys.modules.setdefault("camel.messages", camel_messages_pkg)
sys.modules.setdefault("camel.messages.system_messages", system_messages_pkg)

import os
os.environ.setdefault("OPENAI_API_KEY", "test")
