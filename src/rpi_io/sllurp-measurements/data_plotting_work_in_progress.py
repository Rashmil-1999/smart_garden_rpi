import json
import matplotlib as plt

# top_shelf_data = json.load(open('dry_top_shelf.json'), 'r')
# mid_shelf_data = json.load(open('dry_mid_shelf.json'), 'r')
# bottom_shelf_data = json.load(open('dry_bottom_shelf.json'), 'r')
# 
# top_box_data = json.load(open('dry_boxes_top.json'), 'r')
# mid_box_data = json.load(open('dry_boxes_mid.json'), 'r')
# bottom_box_data = json.load(open('dry_boxes_bottom.json'), 'r')

top_shelf_list = top_shelf_data['rssi_vals']['e280689000000001a33707c4']['peak_rssi'].items()
# top_shelf_list = top_shelf_data['rssi_vals']['e280689000000001a33707c4']['rssi'].items()
mid_shelf_list = mid_shelf_data['rssi_vals']['e280689000000001a33707c4']['peak_rssi'].items()
bot_shelf_list = bottom_shelf_data['rssi_vals']['e280689000000001a33707c4']['peak_rssi'].items()

top_shelf_x, top_shelf_y = zip.(*top_shelf_list)
mid_shelf_x, mid_shelf_y = zip.(*mid_shelf_list)
bot_shelf_x, bot_shelf_y = zip.(*bot_shelf_list)

top_box_list = top_box_data.items()
mid_box_list = mid_box_data.items()
bot_box_list = bot_box_data.items()