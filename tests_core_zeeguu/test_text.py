from tests_core_zeeguu.model_test_mixin import ModelTestMixIn
from tests_core_zeeguu.rules.bookmark_rule import BookmarkRule
from tests_core_zeeguu.rules.language_rule import LanguageRule
from tests_core_zeeguu.rules.text_rule import TextRule
from tests_core_zeeguu.rules.user_rule import UserRule
from tests_core_zeeguu.rules.user_word_rule import UserWordRule
from zeeguu.model.user_word import UserWord


class TextTest(ModelTestMixIn):
    def setUp(self):
        super().setUp()

        self.text_rule = TextRule()
        self.user_rule = UserRule()
        self.bookmark_rule = BookmarkRule(self.user_rule.user)

    def test_user_word_count(self):

        self.assertIsNotNone (self.text_rule.text.content_hash)