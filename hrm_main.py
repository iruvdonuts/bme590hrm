import hrm_class

def main(filename,
        user_specified_time1=0,
        user_specified_time2=30,
        brady_threshold=50,
        tachy_threshold=100,
        brady_time=5,
        tachy_time=5,
        inst=False,
        avg=False,
        ano=False,
        units=1):
    hrm_object = hrm_class.HrmData(filename);

if __name__ == '__main__':
    main('test_data/test_data1.csv',units=1)

