import pytest
from pathlib import Path
import numpy as np
import pandas as pd
from datetime import timedelta

from models.ScenarioGeneration import ScenarioGenerator
from models.CVaRtargets import get_cvar_targets
from models.CVaRmodel import cvar_model


TEST_DIR = Path(__file__).parent


@pytest.fixture(scope="module")
def n_simulations_target():
    return 250


@pytest.fixture()
def cvar_target_data(start_test_date, weekly_returns, scgen, n_simulations_target, request):
    start_of_test_dataset = str(start_test_date + timedelta(days=1))
    targets, benchmark_port_val = get_cvar_targets(
        test_date=start_of_test_dataset,
        benchmark=request.getfixturevalue(request.param),  # MSCI World benchmark
        budget=100,
        cvar_alpha=0.05,
        data=weekly_returns,
        scgen=scgen,
        n_simulations=n_simulations_target
    )
    return targets, benchmark_port_val


@pytest.mark.parametrize(
        "cvar_target_data, label", 
        [("benchmark_isin_1", "1"), ("benchmark_isin_2", "2")], 
        indirect=["cvar_target_data"]
    )
def test_get_cvar_targets(cvar_target_data, label):
    expected_targets = pd.read_csv(f"tests/cvar/targets_{label}_BASE.csv", index_col=0)
    expected_benchmark_port_val = pd.read_csv(f"tests/cvar/benchmark_port_val_{label}_BASE.csv", index_col=0, parse_dates=True)

    targets, benchmark_port_val = cvar_target_data

    #targets.to_csv(f"tests/cvar/targets_{label}_ACTUAL.csv")
    #benchmark_port_val.to_csv(f"tests/cvar/benchmark_port_val_{label}_ACTUAL.csv")
    pd.testing.assert_frame_equal(targets, expected_targets)
    pd.testing.assert_frame_equal(benchmark_port_val, expected_benchmark_port_val)


@pytest.mark.parametrize("cvar_target_data", ["benchmark_isin_2"], indirect=True)
def test_cvar_model(test_narrow_dataset, mc_scenarios, cvar_target_data):
    expected_port_allocation = pd.read_csv("tests/cvar/port_allocation_BASE.csv", index_col=0)
    expected_port_value = pd.read_csv("tests/cvar/port_value_BASE.csv", index_col=0, parse_dates=True)
    expected_port_cvar = pd.read_csv("tests/cvar/port_cvar_BASE.csv", index_col=0)

    targets, _ = cvar_target_data
    
    port_allocation, port_value, port_cvar = cvar_model(
        test_ret=test_narrow_dataset,   
        scenarios=mc_scenarios,  # Scenarios
        targets=targets,  # Target
        budget=100,
        cvar_alpha=0.05,
        trans_cost=0.001,
        max_weight=1,
        solver="GLPK"
    )

    #port_allocation.to_csv("tests/cvar/port_allocation_ACTUAL.csv")
    #port_value.to_csv("tests/cvar/port_value_ACTUAL.csv")
    #port_cvar.to_csv("tests/cvar/port_cvar_ACTUAL.csv")

    active_constraints = (targets.to_numpy() - port_cvar.to_numpy()) < 1e-5
    pd.testing.assert_frame_equal(port_allocation, expected_port_allocation, atol=1e-5)
    pd.testing.assert_frame_equal(port_value, expected_port_value)
    pd.testing.assert_frame_equal(port_cvar[active_constraints], expected_port_cvar[active_constraints])
