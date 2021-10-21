import pandas, pytest
from DIL import Suppression


@pytest.fixture
def suppression_fixture(datas_fixture):
    dataSetting = Suppression(datas_fixture.copy())

    return dataSetting


class TestSuppression:
    @pytest.fixture(autouse=True)
    def _suppressionInit(self, suppression_fixture):
        self._suppression = suppression_fixture

    def test_general(self):
        origeralColumn = list(self._suppression.datas)
        currentColumn = ["전화번호", "주소"]

        self._suppression.general(["전화번호", "주소"])

        assert sorted(list(set(origeralColumn) - set(currentColumn))) == sorted(
            list(self._suppression.datas)
        )


# 일반 삭제
# suppressionTest.general(['전화번호', '주소'])

# 부분 삭제
# suppressionTest.partial('이름', [1, 2])

# 레코드 삭제
# suppressionTest.record([0])
# suppressionTest.record([0, 2])

# 로컬 삭제
# suppressionTest.local('이름', [0])
# suppressionTest.local('이름', [0, 2])

# 마스킹
# suppressionTest.masking('이름', [1, 3])

# 주소 부분 삭제
# suppressionTest.address('주소', 1)
# suppressionTest.address("주소", 2)

# print(excel.head())
