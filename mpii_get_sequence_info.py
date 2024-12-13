def mpii_get_sequence_info(subject_id, sequence):
    # Initialize default values
    ub_augmentable = False
    lb_augmentable = False
    bg_augmentable = False
    chair_augmentable = False
    fps = 25
    num_frames = 0

    if subject_id == 1:
        if sequence == 1:
            bg_augmentable = True
            chair_augmentable = True
            num_frames = 6416
        elif sequence == 2:
            ub_augmentable = True  # The LB masks are bad, so skip putting textures there and in the BG
            chair_augmentable = True
            num_frames = 12430
            fps = 50

    elif subject_id == 2:
        if sequence == 1:
            bg_augmentable = True
            chair_augmentable = True
            num_frames = 6502
        elif sequence == 2:
            bg_augmentable = True
            chair_augmentable = True
            ub_augmentable = True
            lb_augmentable = True
            num_frames = 6081

    elif subject_id == 3:
        fps = 50
        if sequence == 1:
            bg_augmentable = True
            chair_augmentable = True
            num_frames = 12488
        elif sequence == 2:
            bg_augmentable = True
            chair_augmentable = True
            ub_augmentable = True
            lb_augmentable = True
            num_frames = 12283

    elif subject_id == 4:
        if sequence == 1:
            bg_augmentable = True
            chair_augmentable = True
            num_frames = 6171
        elif sequence == 2:
            chair_augmentable = True  # The LB masks are bad, so skip putting textures there and in the BG
            ub_augmentable = True
            num_frames = 6675

    elif subject_id == 5:
        fps = 50
        if sequence == 1:
            bg_augmentable = True
            chair_augmentable = True
            num_frames = 12820
        elif sequence == 2:
            chair_augmentable = True
            ub_augmentable = True
            bg_augmentable = True
            lb_augmentable = True
            num_frames = 12312

    elif subject_id == 6:
        if sequence == 1:
            bg_augmentable = True
            chair_augmentable = True
            num_frames = 6188
        elif sequence == 2:
            ub_augmentable = True
            lb_augmentable = True
            bg_augmentable = True
            chair_augmentable = True
            num_frames = 6145

    elif subject_id == 7:
        if sequence == 1:
            bg_augmentable = True
            chair_augmentable = True
            ub_augmentable = True
            lb_augmentable = True
            num_frames = 6239
        elif sequence == 2:
            bg_augmentable = True
            chair_augmentable = True
            num_frames = 6320

    elif subject_id == 8:
        if sequence == 1:
            bg_augmentable = True
            chair_augmentable = True
            ub_augmentable = True
            lb_augmentable = True
            num_frames = 6468
        elif sequence == 2:
            bg_augmentable = True
            chair_augmentable = True
            num_frames = 6054

    return bg_augmentable, ub_augmentable, lb_augmentable, chair_augmentable, fps, num_frames
