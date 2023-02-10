import pytest
import allure

@allure.title('пропущен по причине...')
@pytest.mark.skip(reason='причина пропуска')
def test_skip():
    assert True

@allure.title('функция помечена как xfail потому, что...')
@pytest.mark.xfail(condition=True, reason='причина, по которой тестовая функция помечена как xfail')
def test_xfail_1():
    '''
    если тест упадет, он пометится как skipped - тест пропущен
    если тест пройдет, он пометится как passed - тест пройден
    в обоих случаях в отчет добавится тег ожидаемый сбой
    '''
    assert False

@allure.title('функция помечена как xfail потому, что...')
@pytest.mark.xfail(condition=True, reason='причина, по которой тестовая функция помечена как xfail')
def test_xfail_2():
    assert True

@allure.title('пропущен по причине несоответствия условию') #дает название тесту в отчете allure
@pytest.mark.skipif(condition='2 + 2 != 5')
def test_skip_by_triggered_condition():
    pass

@allure.title('пропущен по причине невыполнения всех параметров')
@pytest.mark.parametrize('param', [1, 2, 3, 4, 6])
def test_parametrize(param):
    assert (param % 2) == 0