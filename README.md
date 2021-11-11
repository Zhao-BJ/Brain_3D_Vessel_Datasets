## Brain 3D Vessel Datasets

本项目的目的是介绍大脑血管相关的3D数据集。公开的数据集包括MIDAS、TubeTK。

### 数据集

#### Designed Database of MR Brain Images of Healthy Volunteers

##### 数据描述

数据集来自the CASILab at The University of North Carolina at Chapel Hill，其目标之一是通过对大脑MR图像定义的结构形状进行统计分析来评估疾病。这种评估的要求是了解健康解剖结构的形状范围。

作者提供了一个设计的MR数据库，包含100名健康受试者的大脑图像，其中每十年为一组扫描20名患者（18-29、30-39、40-49、50-59和60+），每组均等按性别划分，并排除任何糖尿病、高血压、头部外伤、精神疾病或其他可能影响大脑的症状或病史的受试者。

图像是在标准化协议下通过Siemens Allegra head-only 3T MR system获取的。T1和T2图像以$ 1\times1\times1 \quad mm^3 $，体积大小为$ 176 \times 256 \times 176 \quad voxel $。MRA图像以$ 0.5 \times 0.5 \times 0.8 \quad mm^3 $获取，体积大小为$ 448 \times 448 \times 128 \quad voxel $。以及使用6个方向和体素大小为$ 2 \times 2 \times 2 \quad mm^3 $的扩散张量成像（DTI）。除了年龄和性别外，还记录了惯用手和种族。

##### 数据地址

数据集最终提供了109个样本，每个样本均包含MRA模态和可能包含其他模态的图像。有两个地址可以下载该数据集，一个是通过MIDAS Data Server at Kitware, Inc发布，另一个则是在开源工具TubeTK社区。

##### MIDAS (https://www.insight-journal.org/midas/community/view/21)

MIDAS并没有提供血管的标记。但有一个德国研究机构在一篇论文研究中提供了20个样本的动脉血管标签。

* 研究机构：CLAIM - Charité Lab for AI in Medicine, Charité Universitätsmedizin Berlin

* 研究论文：[BRAVE-NET: Fully Automated Arterial Brain Vessel Segmentation in Patients With Cerebrovascular Disease](https://www.frontiersin.org/articles/10.3389/frai.2020.552258/full?utm_source=S-TWT&utm_medium=SNET&utm_campaign=ECO_FRAI_FDATA_XXXXXXXX_auto-dlvrit)

* 标签地址：https://zenodo.org/record/3968844#.YYyQ8GBByUk

##### TubeTK (https://public.kitware.com/Wiki/TubeTK/Data)

TubeTK除了完整的数据集外，还比MIDAS多了一个子集，这个子集是在42个样本中提取的颅内血管系统（中心线 + 半径）。具有子集的样本可在辅组数据文件夹中找到血管网络注释。

然而，辅组数据文件夹内的血管网络注释是后缀为'.tre'的文件，文件内对中心线上的每个点的坐标和半径进行了注释。需要将'.tre'文件转换为矩阵。注释文件的详细信息见：[TubeTK/TubeTK_VascularNetwork_annotation.md](https://github.com/Zhao-BJ/Brain_3D_Vessel_Datasets/blob/main/TubeTK/TubeTK_VascularNetwork_annotation.md)。将'.tre'文件转换为矩阵，并保存到NIfTI文件的代码在：[]()。

