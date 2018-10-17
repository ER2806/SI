import unittest

from polyline import encode


class ConvertToPolyline(unittest.TestCase):
    def test_convert(self):
        self.test_points = [[(11, -1.2), (4.7, -0.95), (3.252, -123)],
               [(52.841, 334.26), (76.382, 615.08), (55.03, 3.362), (74.721, 3.808)],
               [(-4.39, -2.52), (-41.074, -1.598), (-4.38, -2.087), (-9.048, -2.16991)]]
        self.test_polyline = ['_mcbA~jiF~mme@oyo@~xyGn{|gV', 'gooaI_ddw~@gztnC_t~pt@~hiaCndstsBw{dwBobvA',
                 'nlxY~dkN~y{~EoasDox}~Efo~A~un[deO']
        for i in range(len(self.test_points)):
            print("testtest")
            #print(encode(test_points[i]))
            self.assertEqual(encode(self.test_points[i]), self.test_polyline[i])
