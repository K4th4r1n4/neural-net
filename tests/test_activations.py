from neural_net.activations import sigmoid

from math import log


def test_sigmoid():
    """Test `sigmoid` function."""
    assert sigmoid(0.0) == 0.5
    assert sigmoid(-log(3)) == 0.25
    assert sigmoid(log(3)) == 0.75
    