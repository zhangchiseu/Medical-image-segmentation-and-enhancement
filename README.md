# Medical-image-segmentation-and-enhancement

***

## 各文件含义：

(1). CTcase_num.txt: 其中包含51个病例编号。这是从totalsegmentatorCT数据集中制作的肺部CT子集中的病例号；

(2). DiceJaccardHausdorff.py: 计算Dice score、 Jaccard index和hausdorff distance；

(3). MedianfilePlusGaussianfilter.py: 对得到的数据集进行中值滤波和高斯滤波；

(4). MergeAll.py: 将totalsegmentator: 数据集中的真实分割结果合并为一个图像;

(5). Medical Image Segmentation and Enhancement.pdf: 报告。

***

## 复现各项目所用到的命令：

(1). Totalsegmentator

官方github：https://github.com/wasserth/TotalSegmentator

分割：TotalSegmentator -i D:/TotalSegmentator/s0011/ct.nii.gz  -o D:/TotalSegmentator/seg

注意 -i后接原始数据的路径， -o后接分割结果的存储位置

(2). nnUNet

官方github：https://github.com/MIC-DKFZ/nnUNet

预处理：nnUNetv2_plan_and_preprocess -d 2 --verify\_dataset\_integrity 

其中-d后的数字代表任务名，取决于任务数据集的命名

训练:

nnUNetv2\_train 2 3d\_fullres 0

nnUNetv2\_train 2 3d\_fullres 1  

nnUNetv2\_train 2 3d\_fullres 2  

nnUNetv2\_train 2 3d\_fullres 3 

nnUNetv2\_train 2 3d\_fullres 4  

其中
3d\_fullres可替换为3d\_lowres(低分辨率）、2d(2D U-Net). 本文使用3d_lowres

(3). Deformation recovery diffusion model

官方github：https://github.com/jianqingzheng/def_diff_rec


数据增强：

python DRDM_augment.py --config Config/config_lct.yaml

注意，应先cd到项目文件下的DRDM_augment.py文件所在的位置，再运行该命令




详细复现过程与结果见Medical Image Segmentation and Enhancement.pdf
