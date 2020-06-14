from openpiv_python_lite import extended_search_area_piv, get_coordinates

import imageio 

def test_piv():
    """
    Simplest PIV run on the pair of images using default settings

    piv(im1,im2) will create a tmp.vec file with the vector filed in pix/dt (dt=1) from 
    two images, im1,im2 provided as full path filenames (TIF is preferable, whatever imageio can read)

    """


    # if im1 is None and im2 is None:
    im1 = ('./test/img/frame_a.tif')
    im2 = ('./test/img/frame_b.tif')

    frame_a = imageio.imread(im1)
    frame_b = imageio.imread(im2)
    
    frame_a[0:32, 512-32:] = 255

    print(frame_a[0,0])

    u, v = extended_search_area_piv(frame_a,frame_b,
                                    window_size=32,overlap=16)
    x, y = get_coordinates(image_size = frame_a.shape, 
                           window_size=32, overlap=16)

    print(x[0], y[0], u[0], v[0])

    return x, y, u, v
    