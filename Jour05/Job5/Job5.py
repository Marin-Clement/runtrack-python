def calc_meter(steps, height):
    final = (((steps * 2) * height) / 100) * 7
    print("Pour", steps, "marches de", height, "cm le gardien parcours", final,"m par semaine" )


calc_meter(20, 100)
