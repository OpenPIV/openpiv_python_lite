from openpiv_python_lite import extended_search_area_piv as piv, random_noise
import numpy as np

frame_a = np.zeros((32, 32))
frame_a = random_noise(frame_a)
frame_b = np.roll(np.roll(frame_a, 3, axis=1), 2, axis=0)


def test_piv():
    """ test of the simplest PIV run 32 x 32 """
    u, v = piv(frame_a, frame_b, window_size=32)
    print(np.max(np.abs(u-3)))
    # assert(np.max(np.abs(u-3)) < 0.2)
    # assert(np.max(np.abs(v+2)) < 0.2)


def test_piv_smaller_window():
    """ test of the search area larger than the window """
    u, v = piv(frame_a, frame_b, window_size=16, search_area_size=32)
    print(np.max(np.abs(u-3)))
    # assert(np.max(np.abs(u+3)) < 0.2)
    # assert(np.max(np.abs(v-2)) < 0.2)


# def test_extended_search_area():
#     """ test of the extended area PIV with larger image """
#     frame_a = np.zeros((64, 64))
#     frame_a = random_noise(frame_a)
#     frame_b = np.roll(np.roll(frame_a, 3, axis=1), 2, axis=0)
#     u,v = piv(frame_a.astype(np.int32), frame_b.astype(np.int32),
#               window_size=16, search_area_size=32, overlap=0)
#     # print u,v
#     assert(np.max(np.abs(u-3)+np.abs(v+2)) <= 0.5)
    
# def test_extended_search_area_sig2noise():
#     """ test of the extended area PIV with sig2peak """
#     frame_a = np.zeros((64,64))
#     frame_a = random_noise(frame_a)
#     frame_b = np.roll(np.roll(frame_a, 3, axis=1), 2, axis=0)
#     u, v, s2n = piv(frame_a, frame_b, window_size=16, search_area_size=32,
#                   sig2noise_method='peak2peak')
#     assert(np.max(np.abs(u-3)+np.abs(v+2)) <= 0.3)