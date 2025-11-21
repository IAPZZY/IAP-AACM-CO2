# %%
import numpy as np
import pandas as pd
import xarray as xr
import netCDF4 as nc
import cftime
from pylab import *
from matplotlib.ticker import  MultipleLocator
from matplotlib.ticker import  FormatStrFormatter
import glob 

# %%
names_naq = glob.glob(r'D:\论文撰写\NAQPMS多源模式验证与加拿大模拟\数据作图\obspack_naq_ct.r3\naq.o\*')
names_ct = glob.glob(r'D:\论文撰写\NAQPMS多源模式验证与加拿大模拟\数据作图\obspack_naq_ct.r3\ct.o\*')

# %%
xx = [  datetime.datetime.strptime('2010',"%Y"),\
        datetime.datetime.strptime('2011',"%Y"),\
        datetime.datetime.strptime('2012',"%Y"),\
        datetime.datetime.strptime('2013',"%Y"),\
        datetime.datetime.strptime('2014',"%Y"),\
        datetime.datetime.strptime('2015',"%Y"),\
        datetime.datetime.strptime('2016',"%Y"),\
        datetime.datetime.strptime('2017',"%Y"),\
        datetime.datetime.strptime('2018',"%Y"),\
        datetime.datetime.strptime('2019',"%Y"),\
        datetime.datetime.strptime('2020',"%Y")]

st_date = datetime.datetime.strptime('2010-01-01',"%Y-%m-%d")
ed_date = datetime.datetime.strptime('2020-01-01',"%Y-%m-%d")

# %%
from collections import defaultdict
import re

# 定义文件路径列表
file_list = names_naq

# 使用 defaultdict 按 tag 分组
tag_dict = defaultdict(list)

# 遍历文件路径
for file_path in file_list:
    # 提取文件名
    file_name = file_path.split('\\')[-1]
    # 使用正则表达式提取 tag，忽略高度信息（如30magl）
    match = re.search(r'_(allvalid|representative|allhours|baseline|allhours|nonlocal|marine|Continental|Baseline )', file_name)
    if match:
        tag = match.group(1)  # 提取分组中的主要标签
        tag_dict[tag].append(file_path)

# 打印结果
for tag, files in tag_dict.items():
    print(f"Tag: {tag}, Count: {len(files)}")
    for file in files:
        print(f"  {file}")


# %%
from collections import defaultdict
import re

# 定义文件路径列表
file_list2 = names_ct

# 使用 defaultdict 按 tag 分组
tag_dict2 = defaultdict(list)

# 遍历文件路径
for file_path2 in file_list2:
    # 提取文件名
    file_name2 = file_path2.split('\\')[-1]
    # 使用正则表达式提取 tag，忽略高度信息（如30magl）
    match = re.search(r'_(allvalid|representative|allhours|baseline|allhours|nonlocal|marine|Continental|Baseline )', file_name2)
    if match:
        tag = match.group(1)  # 提取分组中的主要标签
        tag_dict2[tag].append(file_path2)

# 打印结果
for tag, files in tag_dict2.items():
    print(f"Tag: {tag}, Count: {len(files)}")
    for file in files:
        print(f"  {file}")


# %%
import os

# 假设 tag_dict['allvalid'] 和 tag_dict2['allvalid'] 已经存在，并包含了完整的文件路径
# 提取文件名（不包括路径）
names_naq = glob.glob(r'D:\论文撰写\NAQPMS多源模式验证与加拿大模拟\数据作图\obspack_naq_ct.r3\naq.o\*')
names_ct = glob.glob(r'D:\论文撰写\NAQPMS多源模式验证与加拿大模拟\数据作图\obspack_naq_ct.r3\ct.o\*')

files_in_group1 = [os.path.basename(path) for path in names_naq]
files_in_group2 = [os.path.basename(path) for path in names_ct]

# 转换为集合并进行差集操作
set_group1 = set(files_in_group1)
set_group2 = set(files_in_group2)

# 找出 group1 中有，而 group2 中没有的文件名
files_in_group1_not_in_group2 = set_group1 - set_group2
print("Files in group1 but not in group2:", files_in_group1_not_in_group2)

# 找出 group2 中有，而 group1 中没有的文件名
files_in_group2_not_in_group1 = set_group2 - set_group1
print("Files in group2 but not in group1:", files_in_group2_not_in_group1)


# %%
stats = []
for tag in ['allhours','allvalid','representative','baseline','marine','nonlocal']:
    for id in arange(len(tag_dict[tag])):
    #for id in arange(1):
        if tag_dict[tag][id] =='D:\\论文撰写\\NAQPMS多源模式验证与加拿大模拟\\数据作图\\obspack_naq_ct.r3\\naq.o\\co2_cpt_surface-insitu_36_marine.csv' :
            continue
        elif tag_dict[tag][id] =='D:\\论文撰写\\NAQPMS多源模式验证与加拿大模拟\\数据作图\\obspack_naq_ct.r3\\naq.o\\co2_con_aircraft-insitu_42_allvalid.csv':
            continue
        else:
            print(tag_dict[tag][id])
            iname = tag_dict[tag][id]
            iname2 = tag_dict2[tag][id]
            df = pd.read_csv(iname)
            df2 = pd.read_csv(iname2)
            #df['time'] = pd.to_datetime(df['time'].str.strip(), format='%Y/%m/%d')
            for ii in range(len(df['time'].values)):
                date_string = df['time'].values[ii][:-9]
                date_format = "%Y-%m-%d"
                date = datetime.datetime.strptime(date_string, date_format)
                df['time'].values[ii] = date
            for ii in range(len(df2['time'].values)):
                date_string = df2['time'].values[ii][:-9]
                date_format = "%Y-%m-%d"
                date = datetime.datetime.strptime(date_string, date_format)
                df2['time'].values[ii] = date
            #    #test = df.groupby(['time']).mean().reset_index() # 获取组内记录数目
            end_date = datetime.datetime.strptime("2019-12-31", "%Y-%m-%d")
            df = df[df['time'] <= end_date]
            df2 = df2[df2['time'] <= end_date]

            test = df.groupby(['time']).mean().reset_index()
            test2 = df2.groupby(['time']).mean().reset_index()

            # 提取用于计算的观测值和模拟值
            obs_values = test['sta_value_out'].values
            obs_values2 = test2['sta_value_out'].values
            sim_values = test['naq_value_out'].values
            ct_values = test2['ct_value_out'].values
            # 计算相关系数 (r)
            r = np.corrcoef(obs_values, sim_values)[0, 1]
            r2 = np.corrcoef(obs_values2, ct_values*1000)[0, 1]
            # 计算均方根误差 (RMSE)
            rmse = np.sqrt(np.mean((sim_values - obs_values) ** 2))
            rmse2 = np.sqrt(np.mean((ct_values*1000 - obs_values2) ** 2))
            # 计算平均偏差 (MB)
            mb = np.mean(sim_values - obs_values)
            mb2 = np.mean(ct_values*1000 - obs_values2)
            # 计算平均绝对误差 (ME)
            me = np.mean(np.abs(sim_values - obs_values))
            me2 = np.mean(np.abs(ct_values*1000 - obs_values2))
            stats.append({
                "id": id,
                "iname": iname[51:-4],
                "r": r,
                "r2" :r2,
                "RMSE": rmse,
                "RMSE2": rmse2,
                "MB": mb,
                "MB2":mb2,
                "ME": me,
                "ME2":me2,
                "Point_num": len(test['sta_value_out'])
                })

            # 添加统计参数标注
            #stat_text = (f'   CT  IAP-AACM\n'
            #            f"      r:{r2:.2f}  {r:.2f}   \n"
            #            f"RMSE:{rmse2:.2f}  {rmse:.2f}  \n"
            #            f"    MB:{mb2:.2f}  {mb:.2f}   \n"
            #           )
            stat_text = (
                "  IAP-AACM   CT\n"
                f"r   :{r:.2f}  {r2:.2f}\n"
                f"RMSE:{rmse:.2f}  {rmse2:.2f}\n"
                f"MB  :{mb:.2f}  {mb2:.2f}"
            )


            fig = plt.figure(figsize=(5,2.8))
            ax = fig.add_subplot(1,1,1)

            #ax.text(0.98, -0.05, stat_text, transform=ax.transAxes, fontsize=12,
            #        verticalalignment='bottom', horizontalalignment='right', bbox=dict(facecolor='white', alpha=0.0))
            ax.text(
                0.56, 0.05,           # 图中相对坐标（右下角）
                stat_text,
                transform=ax.transAxes,
                fontsize=12,
                fontfamily='monospace',  # 使用等宽字体对齐数字
                verticalalignment='bottom',
                horizontalalignment='left',
                bbox=dict(facecolor='white', alpha=0.6, edgecolor='gray')  # 可选：背景框
            )

            plt.scatter(test['time'].values[::],test['sta_value_out'].values[::],color='black',s=2,label='OBS')
            plt.scatter(test2['time'].values[::],test2['ct_value_out'].values[::]*1000,color='green',s=2,label='CT')
            plt.scatter(test['time'].values[::],test['naq_value_out'].values[::],color='red',s=2,label='IAP-AACM')

            leg=ax.legend(prop={'size':12},frameon=False,loc="upper left",\
                    ncol=3,bbox_to_anchor=(0.0,0.95),borderaxespad = 0.,markerscale=5.,handletextpad=0.1,labelspacing=0.2,columnspacing=0.1) #图例

            xmajorLocator = MultipleLocator(400) #设置x轴次标签为24h显示一格（注意，在设置好标签长度和宽度之后再指定）
            ax.xaxis.set_major_locator(xmajorLocator) #将得到的标签加入图中


            plt.xlim([st_date,ed_date]) #设置y轴的范围
            #ax.set_xlabel('time', loc='center' ,  fontsize =15,labelpad=4)
            ax.set_ylabel('CO$_2$ (ppm)', loc='center', fontsize =15, labelpad=4)
            plt.xticks(fontsize=15)
            plt.yticks(fontsize=15)
            #plt.xticks(xx[:],['2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020',],rotation=90)
            plt.xticks(xx[::2],['2010','2012','2014','2016','2018','2020'],rotation=0)
            plt.title(iname[56:-4],fontsize=17)
            plt.rcParams['savefig.dpi'] = 300

            plt.savefig(r'D:\论文撰写\NAQPMS多源模式验证与加拿大模拟\数据作图\NOAA多站点对比数据统计筛选r4\{}\{}.png'.format(tag,iname[56:-4]),bbox_inches='tight')


# %%
# 转换为 DataFrame
df_stats = pd.DataFrame(stats)

# 保存为 CSV
df_stats.to_csv("D:/论文撰写/NAQPMS多源模式验证与加拿大模拟/数据作图/NOAA多站点对比数据统计筛选r2/statistics_results.r2.csv")  # index=False 表示不保存索引

# %%
'''

            fig = plt.figure(figsize=(5,2.8))
            ax = fig.add_subplot(1,1,1)

            ax.text(0.98, 0.04, stat_text, transform=ax.transAxes, fontsize=12,
                    verticalalignment='bottom', horizontalalignment='right', bbox=dict(facecolor='white', alpha=0.0))


            plt.scatter(test['time'].values[::],test['sta_value_out'].values[::],color='black',s=2,label='OBS')
            plt.scatter(test2['time'].values[::],test2['ct_value_out'].values[::]*1000,color='green',s=2,label='CT')
            plt.scatter(test['time'].values[::],test['naq_value_out'].values[::],color='red',s=2,label='NAQ')

            leg=ax.legend(prop={'size':12},frameon=False,loc="upper left",\
                    ncol=3,bbox_to_anchor=(0.0,0.95),borderaxespad = 0.,markerscale=5.,handletextpad=0.1,labelspacing=0.2,columnspacing=0.1) #图例

            xmajorLocator = MultipleLocator(400) #设置x轴次标签为24h显示一格（注意，在设置好标签长度和宽度之后再指定）
            ax.xaxis.set_major_locator(xmajorLocator) #将得到的标签加入图中


            plt.xlim([st_date,ed_date]) #设置y轴的范围
            #ax.set_xlabel('time', loc='center' ,  fontsize =15,labelpad=4)
            ax.set_ylabel('CO$_2$ (ppm)', loc='center', fontsize =15, labelpad=4)
            plt.xticks(fontsize=15)
            plt.yticks(fontsize=15)
            #plt.xticks(xx[:],['2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020',],rotation=90)
            plt.xticks(xx[::2],['2010','2012','2014','2016','2018','2020'],rotation=0)
            plt.title(iname[56:-4],fontsize=17)
            plt.rcParams['savefig.dpi'] = 300

            plt.savefig(r'D:\论文撰写\NAQPMS多源模式验证与加拿大模拟\数据作图\NOAA多站点对比数据统计筛选r2\{}\{}.png'.format(tag,iname[56:-4]),bbox_inches='tight')

'''


