##### SUBSCRIPTIONS #####
IRRIGATION_TIME_SUBSCRIPTION: str = """
  subscription irrigation_time_subscription($u_uuid: uuid!) {
    irrigation_timings(where: {u_uuid: {_eq: $u_uuid}}) {
        channel_1
        channel_2
        channel_3
        channel_4
        schedule
    }
  }
"""


MANUAL_CONTROL_SUBSCRIPTION: str = """
  subscription irrigation_mode($u_uuid: uuid!) {
      irrigation_mode(where: {u_uuid: {_eq: $u_uuid}}) {
          ch_1
          ch_2
          ch_3
          ch_4
          ch_5
          ch_6
          ch_7
          ch_8
      }
  }
"""

MANUAL_SUBSCRIPTION: str = """
  subscription irrigation_mode($u_uuid: uuid!) {
      irrigation_mode(where: {u_uuid: {_eq: $u_uuid}}) {
          manual
          u_uuid
      }
  }
"""

PLANT_MAPPING_SUBSCRIPTION: str = """
  subscription plant_sensor_mapping_subscription($u_uuid: uuid!) {
    plant_sensor_mapping(where: {plant: {u_uuid: {_eq: $u_uuid}}, is_valid: {_eq: true}}) {
      p_uuid
      sensor_mapping {
        alias
        pin_num
        temp_sensor
      }
    }
  }
"""

##### MUTATIONS #####
IRRIGATION_LOG_MUTATION: str = """
  mutation IrrigationMutation($u_uuid: uuid!,$time: timestamptz!, $mode: String!) {
      insert_irrigation_log(objects: {u_uuid: $u_uuid,time: $time, mode: $mode}) {
          affected_rows
      }
  }
"""

SENSOR_DATA_MUTATION: str = """
  mutation insert_multiple_data_points($objects: [sensor_data_insert_input!]!) {
    insert_sensor_data(objects: $objects) {
      affected_rows
    }
  }
"""
