import unittest
import fcpxml_reader


class test_get_frames_from_time(unittest.TestCase):
    def test_30fps(self):
        ''' Checks 4 seconds at 30 fps - 120 frames
        '''
        frames = fcpxml_reader.get_frames_from_time(4, 30)
        self.assertEqual(frames, 120)

    def test_25fps(self):
        ''' Checks 4 seconds at 25 fps - 100 frames
        '''
        frames = fcpxml_reader.get_frames_from_time(4, 25)
        self.assertEqual(frames, 100)

if __name__ == '__main__':
    unittest.main()
