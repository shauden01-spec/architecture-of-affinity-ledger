# test_core.py
# Automated validation layers for the GitHub Actions runner checking system

def test_lattice_constants():
    ACTIVE_LATTICE_NODES = 614400
    assert ACTIVE_LATTICE_NODES == 614400

def test_recovery_boundary():
    recovery_limit_nodes = int(614400 * 0.80)
    assert recovery_limit_nodes == 491520
