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
"""Constants for KBot V2."""

from etils import epath

from mujoco_playground._src import mjx_env

ROOT_PATH = mjx_env.ROOT_PATH / "locomotion" / "kbot_v2"
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
    "KB_D_501L_L_LEG_FOOT_site",
    "KB_D_501R_R_LEG_FOOT_site",
]

HAND_SITES = [
    "KB_C_501X_Bayonet_Adapter_Hard_Stop_2_site",
    "KB_C_501X_Bayonet_Adapter_Hard_Stop_site",
]

LEFT_FEET_GEOMS = ["KB_D_501L_L_LEG_FOOT_collision_box"]
RIGHT_FEET_GEOMS = ["KB_D_501R_R_LEG_FOOT_collision_box"]
FEET_GEOMS = LEFT_FEET_GEOMS + RIGHT_FEET_GEOMS

ROOT_BODY = "KB_B_102B_TORSO_BOTTOM"

GRAVITY_SENSOR = "upvector"
GLOBAL_LINVEL_SENSOR = "base_link_vel"
GLOBAL_ANGVEL_SENSOR = "base_link_ang_vel"
LOCAL_LINVEL_SENSOR = "base_link_vel"
ACCELEROMETER_SENSOR = "imu_acc"
GYRO_SENSOR = "imu_gyro"

RESTRICTED_JOINT_RANGE = (
    # Right shoulder
    (-2.617994, 2.094395),  # right_shoulder_pitch_03
    (-0.488692, 1.658063),  # right_shoulder_roll_03
    (-1.745329, 1.745329),  # right_shoulder_yaw_02
    (0, 2.530727),          # right_elbow_02
    (-1.745329, 1.745329),  # right_wrist_02
    
    # Left shoulder
    (-2.094395, 2.617994),  # left_shoulder_pitch_03
    (-1.658063, 0.488692),  # left_shoulder_roll_03
    (-1.745329, 1.745329),  # left_shoulder_yaw_02
    (-2.530727, 0),         # left_elbow_02
    (-1.745329, 1.745329),  # left_wrist_02
    
    # Right leg
    (-1.919862, 1.570796),  # right_hip_pitch_04
    (0, 2.268928),          # right_hip_roll_03
    (-1.570796, 1.570796),  # right_hip_yaw_03
    (-2.705260, 0),         # right_knee_04
    (-0.296706, 0.785398),  # right_ankle_02
    
    # Left leg
    (-1.570796, 1.919862),  # left_hip_pitch_04
    (-2.268928, 0),         # left_hip_roll_03
    (-1.570796, 1.570796),  # left_hip_yaw_03
    (0, 2.705260),          # left_knee_04
    (-0.785398, 0.296706),  # left_ankle_02
)
