from setuptools import find_packages, setup

package_name = 'roverrobotics_input_manager'

setup(
    name=package_name,
    version='1.0.2',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Jack Rivera',
    maintainer_email='jack@roverrobotics.com',
    description='Contains Rover provided teleoperation applications',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "joys_manager = roverrobotics_input_manager.joys_manager:main",
        ],
    },
)