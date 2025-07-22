# Copyright 2025 DeepMind Technologies Limited
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Constants for K-Bot."""

from etils import epath

from mujoco_playground._src import mjx_env

ROOT_PATH = mjx_env.ROOT_PATH / "locomotion" / "kbot"
FEET_ONLY_FLAT_TERRAIN_XML = (
    ROOT_PATH / "xmls" / "scene_mjx_feetonly_flat_terrain.xml"
)
FEET_ONLY_ROUGH_TERRAIN_XML = (
    ROOT_PATH / "xmls" / "scene_mjx_feetonly_rough_terrain.xml"
)


def task_to_xml(task_name: str) -> epath.Path:
  return {
      "flat_terrain": FEET_ONLY_FLAT_TERRAIN_XML,
      "rough_terrain": FEET_ONLY_ROUGH_TERRAIN_XML,
  }[task_name]


FEET_SITES = [
    "left_foot",
    "right_foot",
]

HAND_SITES: list[str] = []

LEFT_FEET_GEOMS = ["left_foot"]
RIGHT_FEET_GEOMS = ["right_foot"]
FEET_GEOMS = LEFT_FEET_GEOMS + RIGHT_FEET_GEOMS

ROOT_BODY = "Torso_Side_Right"

GRAVITY_SENSOR = "upvector_imu"
GLOBAL_LINVEL_SENSOR = "base_site_linvel"
GLOBAL_ANGVEL_SENSOR = "base_site_angvel"
LOCAL_LINVEL_SENSOR = "imu_site_linvel"
ACCELEROMETER_SENSOR = "imu_acc"
GYRO_SENSOR = "imu_gyro"

RESTRICTED_JOINT_RANGE = (
    # Right arm
    (-3.141593, 1.396263),   # dof_right_shoulder_pitch_03
    (-1.658063, 0.349066),   # dof_right_shoulder_roll_03
    (-1.658063, 1.658063),   # dof_right_shoulder_yaw_02
    (0, 2.478368),           # dof_right_elbow_02
    (-1.745329, 1.745329),   # dof_right_wrist_00
    # Left arm
    (-1.396263, 3.141593),   # dof_left_shoulder_pitch_03
    (-0.349066, 1.658063),   # dof_left_shoulder_roll_03
    (-1.658063, 1.658063),   # dof_left_shoulder_yaw_02
    (-2.478368, 0),          # dof_left_elbow_02
    (-1.745329, 1.745329),   # dof_left_wrist_00
    # Right leg
    (-2.216568, 1.047198),   # dof_right_hip_pitch_04
    (-2.268928, 0.209440),   # dof_right_hip_roll_03
    (-1.570796, 1.570796),   # dof_right_hip_yaw_03
    (-2.705260, 0),          # dof_right_knee_04
    (-0.226893, 1.256637),   # dof_right_ankle_02
    # Left leg
    (-1.047198, 2.216568),   # dof_left_hip_pitch_04
    (-0.209440, 2.268928),   # dof_left_hip_roll_03
    (-1.570796, 1.570796),   # dof_left_hip_yaw_03
    (0, 2.705260),           # dof_left_knee_04
    (-1.256637, 0.226893),   # dof_left_ankle_02
)
