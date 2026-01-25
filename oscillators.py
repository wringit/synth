import math

def sin_oscillation(freq, amp, phi=0, sample_rate=44100):
    om = math.tau*freq # tau=2pi
    phi = phi/360.0*math.tau
    theta = 0.0
    while True:
        yield amp*math.sin(theta+phi)
        theta += om/sample_rate


def triangle_oscillation(freq, amp, phi=0, sample_rate=44100):
    om = math.tau * freq
    phi = phi / 360.0 * math.tau
    theta = 0.0
    while True:
        normalized = (theta + phi) % math.tau
        if normalized < math.pi:
            yield amp * (4 * normalized / math.tau - 1)
        else:
            yield amp * (3 - 4 * normalized / math.tau)
        theta += om / sample_rate


def square_oscillation(freq, amp, phi=0, sample_rate=44100):
    om = math.tau * freq
    phi = phi / 360.0 * math.tau
    theta = 0.0
    while True:
        normalized = (theta + phi) % math.tau
        yield amp if normalized < math.pi else -amp
        theta += om / sample_rate


def sawtooth_oscillation(freq, amp, phi=0, sample_rate=44100):
    om = math.tau * freq
    phi = phi / 360.0 * math.tau
    theta = 0.0
    while True:
        normalized = (theta + phi) % math.tau
        yield amp * (2 * normalized / math.tau - 1)
        theta += om / sample_rate