def mpii_get_camera_set(camera_set_name):
    if camera_set_name == 'regular':
        camera_set = list(range(14))  # Cameras with regular lenses, not fisheye
    elif camera_set_name == 'relevant':
        camera_set = list(range(11))  # All cameras except the ceiling mounted ones
    elif camera_set_name == 'ceiling':
        camera_set = list(range(11, 14))  # Top down views
    elif camera_set_name == 'vnect':
        camera_set = [0, 1, 2, 4, 5, 6, 7, 8]  # Chest high, knee high and 2 cameras angled down. Use for VNect @ SIGGRAPH 17
    elif camera_set_name == 'mm3d_chest':
        camera_set = [0, 2, 4, 7, 8]  # Subset of chest high, used in "Monocular 3D Human Pose Estimation in-the-wild Using Improved CNN supervision"
    else:
        camera_set = []

    return camera_set
