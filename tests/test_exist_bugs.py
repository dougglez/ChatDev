import os
import tempfile
from chatdev.chat_env import ChatEnv, ChatEnvConfig


def create_env(tmp_path, script):
    cfg = ChatEnvConfig(
        clear_structure=True,
        gui_design=False,
        git_management=False,
        incremental_develop=False,
        background_prompt="",
        with_memory=False,
    )
    env = ChatEnv(cfg)
    env.set_directory(str(tmp_path / "proj"))
    (tmp_path / "proj" / "main.py").write_text(script)
    return env


def test_exist_bugs_success(tmp_path):
    env = create_env(tmp_path, "print('ok')")
    has_bug, info = env.exist_bugs()
    assert has_bug is False
    assert "successfully" in info


def test_exist_bugs_failure(tmp_path):
    env = create_env(tmp_path, "raise ValueError('fail')")
    has_bug, info = env.exist_bugs()
    assert has_bug is True
    assert "Traceback" in info
