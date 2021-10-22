import pandas, pytest
from DIL import Generalization


@pytest.fixture
def generalization_fixture(datas_fixture):
    dataSetting = Generalization(datas_fixture.copy())

    return dataSetting


class TestGeneralization:
    @pytest.fixture(autouse=True)
    def _generalizationInit(self, generalization_fixture):
        self._generalization = generalization_fixture

    @pytest.mark.parametrize(
        "local_scope",
        [
            [0, 3],
            [1, 4],
            [5, 100],
            [2, 3],
            [20, 30],
        ],
    )
    def test_local_target(self, local_scope):
        targetColumn = "성별"
        self._generalization.local(column=targetColumn, currentIndexList=local_scope)

        local_values = self._generalization.datas
        for value in local_values[targetColumn][local_scope[0] : local_scope[1] + 1]:
            assert value == "남성 ~ 여성"

    @pytest.mark.parametrize(
        "local_scope",
        [
            [0, 3],
            [1, 4],
            [5, 100],
            [2, 3],
            [20, 30],
        ],
    )
    def test_local_non_target(self, local_scope):
        targetColumn = "성별"
        self._generalization.local(column=targetColumn, currentIndexList=local_scope)

        local_values = self._generalization.datas
        for value in local_values[targetColumn][local_scope[1] + 1 :]:
            assert value != "남성 ~ 여성"

    def test_categorizion(self):
        targetColumn = "성별"
        category = "Gender"

        self._generalization.categorizion(
            column=targetColumn, replaceList=["남성", "여성"], category=category
        )

        categorizion_values = self._generalization.datas
        for value in categorizion_values[targetColumn]:
            assert value == category
