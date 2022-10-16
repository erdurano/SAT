from satDash.scheduleclasses import TestItem


class Test_TestItem:
    def testItem_test(self):
        assert isinstance(TestItem(item_name="testing TestItem"), TestItem)
