import unittest
import fcpxml_reader
import os


class seconds_to_frames_logic(unittest.TestCase):
    def test_seconds_to_frames_logic(self):
        # Seconds to frames at 30 fps
        frames = fcpxml_reader.get_frames_from_time(4, 30)
        self.assertEqual(frames, 120)

        # Seconds to frames at 25 fps
        frames = fcpxml_reader.get_frames_from_time(4, 25)
        self.assertEqual(frames, 100)


class framerate_logic(unittest.TestCase):
    def test_framerate_logic(self):
        self.data_fldr = os.getcwd() + r'\data'

        data = [[self.data_fldr + r'\25fps\cut\3_clip_100_50_50.fcpxml', 25],
                [self.data_fldr + r'\25fps\no cut\1_clip_25.fcpxml', 25],
                [self.data_fldr + r'\25fps\no cut\1_clip_50.fcpxml', 25],
                [self.data_fldr + r'\25fps\no cut\1_clip_100.fcpxml', 25],
                [self.data_fldr + r'\25fps\no cut\1_clip_150.fcpxml', 25],
                [self.data_fldr + r'\25fps\no cut\1_clip_200.fcpxml', 25],

                [self.data_fldr + r'\30fps\cut\3_clip_100_50_50.fcpxml', 30],
                [self.data_fldr + r'\30fps\cut\3_clip_100_200_200.fcpxml', 30],
                [self.data_fldr + r'\30fps\no cut\1_clip_25.fcpxml', 30],
                [self.data_fldr + r'\30fps\no cut\1_clip_50.fcpxml', 30],
                [self.data_fldr + r'\30fps\no cut\1_clip_100.fcpxml', 30],
                [self.data_fldr + r'\30fps\no cut\1_clip_150.fcpxml', 30],
                [self.data_fldr + r'\30fps\no cut\1_clip_200.fcpxml', 30]]

        for current in data:
            wrapper = fcpxml_reader.fcpxml_wrapper(current[0])
            self.assertEqual(wrapper.framerate, current[1])

if __name__ == '__main__':
    unittest.main()
