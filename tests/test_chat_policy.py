import unittest
from showcase.chat_policy import IncomingMessage, decide_response


class ChatPolicyTests(unittest.TestCase):
    def test_mention_triggers_response(self):
        self.assertTrue(decide_response(IncomingMessage("hello", mentioned_bot=True)).should_respond)

    def test_opt_out_wins_over_mention(self):
        result = decide_response(IncomingMessage("hello", mentioned_bot=True, user_opted_out=True))
        self.assertFalse(result.should_respond)
        self.assertIn("opted out", result.reason)

    def test_quiet_hours_block_non_admin(self):
        self.assertFalse(decide_response(IncomingMessage("hello", mentioned_bot=True, quiet_hours=True)).should_respond)

    def test_admin_command_can_be_handled_during_quiet_hours(self):
        self.assertTrue(decide_response(IncomingMessage("/status", quiet_hours=True, admin_command=True)).should_respond)


if __name__ == "__main__":
    unittest.main()
