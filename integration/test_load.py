from click.testing import CliRunner
from dundie.cli import main, load
import pytest
from .constants import PEOPLE_FILE


cmd = CliRunner()

@pytest.mark.integration
@pytest.mark.medium
def test_load_positive_call_load_command():
    out = cmd.invoke(load, PEOPLE_FILE)
    assert "Dunder" in out.output

@pytest.mark.integration
@pytest.mark.medium
@pytest.mark.parametrize("wrong_commnand", ["loady", "carrega", "start"])
def test_load_negative_call_load_command_with_wrong_params(wrong_commnand):
    out = cmd.invoke(main, wrong_commnand, PEOPLE_FILE)
    assert out.exit_code != 0
    assert f"No such command '{wrong_commnand}'." in out.output
