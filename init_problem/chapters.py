
modules = [
    'mechanics',
    'electrodynamics',
    'modern-physics',
    'optics',
    'heat-and-thermodynamics',
]

chapters_mechanics = [
    'kinematics',
    'projectile',
    'laws-of-motion',
    'work-energy-power',
    'circular-motion',
    'rotation',
    'center-of-mass',
    'gravitation',
    'simple-harmonic-motion',
    'elasticity',
    'fluid-mechanics',
]
chapters_electrodynamics = [
    'electrostatics',
    'current-electricity',
    'capacitors',
    'magnetics',
    'electromagnetic-induction',
    'alternating-current',
    'electromagnetic-waves'
]
chapters_optics = [
    'ray-optics',
    'wave-optics',
]
chapters_modern_physics = [
    'atomic-structure',
    'photoelectric-effect',
    'x-rays',
    'nuclear-physics',
    'semiconductors',
    'communiation-system'
]
chapters_heat_and_thermodynamics = [
    'heat',
    'thermodynamics'
]

chapters = [chapters_mechanics, chapters_electrodynamics,
            chapters_modern_physics, chapters_optics, chapters_heat_and_thermodynamics]

chapters_list = chapters_mechanics + chapters_electrodynamics + \
    chapters_modern_physics + chapters_optics + chapters_heat_and_thermodynamics
