IRRIGATION_TIME_SUBSCRIPTION = """
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
