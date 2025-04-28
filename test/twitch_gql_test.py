import sys
sys.path.append('../')
from src.luscioustwitch import *
import json
import unittest

class TestGqlAPI(unittest.TestCase):
  @classmethod
  def setUpClass(self):
    self.gql = TwitchGQL_API()
    
  def test_get_clip(self):
    clip_id = "PlainFurryRaisinBrokeBack-7bzdbBoHeUT6XupJ"
    clip = self.gql.get_clip(clip_id)
    
    self.assertEqual(clip.clipId, '2382936331')
    self.assertEqual(clip.playbackAccessToken.value["clip_slug"], clip_id)
    
  def test_download_clip(self):
    clip_id = "EnchantingSilkyYakDogFace-OdB69-PvUTV7MSQs"
    
    success = self.gql.download_clip(clip_id, "./tmp.mp4", True)
    
    self.assertTrue(success)
    
    if os.path.exists("./tmp.mp4"):
      os.remove("./tmp.mp4")
    
    
  def test_get_video(self):
    video_id = "635766592"
    video = self.gql.get_video(video_id)
    
    self.assertEqual(video.videoId, video_id)
    self.assertEqual(video.owner["displayName"].lower(), "twitch")
    
if __name__ == '__main__':
  unittest.main()