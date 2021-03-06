import pytest
import hrm_class

def test_for_anomalies_class():
    """Unit test for anomaly method in ecg_data
        class based approach

        Testing for multiple times

        :param  None
        :rtype: Assertions
    """


    myHrm = hrm_class.HrmData('test_data/test_data1.csv')
    bradyTF = myHrm.brady_tf
    tachyTF = myHrm.tachy_tf

    """assert round(bradyTimes[0],0)==30
    assert round(tachyTimes[0],0)==75
    assert round(bradyTimes[1],0)==150
    assert round(tachyTimes[1],0)==195
    """
    assert bradyTF[29]=='true'
    assert tachyTF[29]=='false'