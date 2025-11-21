from obs_staSim_lib import output_staSim
import datetime as dt
from multiprocessing import Pool
from NAQPMS_GLOBAL import *
# 2022-08-19 20:44:41 Sola v4 修改为使用Pool进行并行
# 2022-08-21 17:59:39 Sola v5 使用model_info进行简化
time_zone       = dt.timezone.utc
start_date      = dt.datetime(2014, 1, 1, tzinfo=time_zone)
end_date        = dt.datetime(2020, 12, 31, tzinfo=time_zone)
time_delta      = dt.timedelta(days=1)
sat_file_dir    = '/public/home/tangxiao/zhouxu/Su-D-data/e-datasets/oco_2_L2_Lite_v10r'
sat_type        = 'oco2'
quality_flag    = 'good'
output_dir      = './naqpms.gr.country.71.co2'
tag             = 'zhouRunAll'
output_varlist  = ['time', 'staID', 'type', 'lon', 'lat', 'height', 'xco2', \
            'co2', 'pm25', 'pm10', 'so2', 'no2', 'co', 'o3']
max_job         = 1
def fun_file_name(time):
    #dir = '/data/tangxiao/wuhj/onlineDA_ICEmis/ForeSys/zhouRun/out/data'
    dir = '/data/tangxiao/zouzy/wrfnaq.glb.10yr/data_save/naqpms.gr.country.71.co2/data'
    file_dir = dir + '/testd1.' + dt.datetime.utcfromtimestamp(time).strftime("%Y%m%d%H") + '.grd'
    return file_dir
model_info                  = NAQPMS_GLOBAL()
#model_info.sim_ctl_dir      = '/data/tangxiao/wuhj/onlineDA_ICEmis/ForeSys/zhouRun/out/data/testd1.2018010100.ctl'
model_info.sim_ctl_dir      = '/data/tangxiao/zouzy/naq_co2/data_save/naqpms.n030/testd1.base.w.ctl'
model_info.fun_sim_dat_dir  = fun_file_name
model_info.grid_ctl_dir     = '/data/tangxiao/zhouxu/Su-A-important/model_temp/NAQPMS_GLOBAL_1x1/d01.ctl'
model_info.grid_dat_dir     = '/data/tangxiao/zhouxu/Su-A-important/model_temp/NAQPMS_GLOBAL_1x1/wrfd01.dat'
#model_info.sim_ctl_dir      = '/data/tangxiao/zouzy/naq_co2/data_save/naqpms.n033/data/testd1.2018010100.ctl'
#model_info.grid_ctl_dir     = '/data/tangxiao/zhouxu/Su-A-important/model_temp/NAQPMS_GLOBAL_1x1/d01.ctl'
#model_info.grid_dat_dir     = '/data/tangxiao/zhouxu/Su-A-important/model_temp/NAQPMS_GLOBAL_1x1/wrfd01.dat'

# ============================================================================ #
# 以下不需要修改
with Pool(processes=max_job) as p:
    run_date = start_date
    while run_date <= end_date:
        p.apply_async(
            output_staSim,
            args=(
                sat_file_dir,
                model_info,
                run_date.timestamp(),
            ),
            kwds={
                'output_dir'        : output_dir,
                'sat_type'          : sat_type,
                'quality_flag'      : quality_flag,
                'output_var_list'   : output_varlist,
                'tag'               : tag,
            }
        )
        run_date = run_date + dt.timedelta(days=1)
    p.close()
    p.join()
print('[FINISH]')
