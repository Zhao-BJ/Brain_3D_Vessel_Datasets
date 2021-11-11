## Brain 3D Vessel Datasets

本项目的目的是介绍大脑血管相关的3D数据集。公开的数据集包括MIDAS、TubeTK。

### 数据集

#### MIDAS

##### 数据描述

数据集来自the CASILab at The University of North Carolina at Chapel Hill，并通过MIDAS Data Server at Kitware, Inc发布。其目标之一是通过对大脑MR图像定义的结构形状进行统计分析来评估疾病。这种评估的要求是了解健康解剖结构的形状范围。

作者提供了一个设计的MR数据库，包含100名健康受试者的大脑图像，其中每十年为一组扫描20名患者（18-29、30-39、40-49、50-59和60+），每组均等按性别划分，并排除任何糖尿病、高血压、头部外伤、精神疾病或其他可能影响大脑的症状或病史的受试者。

图像是在标准化协议下在3T单元上获取的。图像包括以$ 1\times1\times1 \quad mm^3 $获取的T1和T2、以$ 0.5 \times 0.5 \times 0.8 \quad mm^3 $获取的磁共振血管造影（MRA）以及使用6个方向和体素大小为$ 2 \times 2 \times 2 \quad mm^3 $的扩散张量成像（DTI）。除了年龄和性别外，还记录了惯用手和种族。

