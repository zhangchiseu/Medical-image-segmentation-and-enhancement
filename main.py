import SimpleITK as sitk
import numpy as np
from scipy.spatial.distance import directed_hausdorff
pred = sitk.ReadImage("D:/TotalSegmentator/data_all/PulmonaryCT/s0029/result/lung_lower_lobe_left.nii.gz")
gt = sitk.ReadImage("D:/TotalSegmentator/data_all/PulmonaryCT/s0029/segmentations/lung_lower_lobe_left.nii.gz")

pred_array = sitk.GetArrayFromImage(pred)
gt_array = sitk.GetArrayFromImage(gt)


def dice_score(pred, gt):
    pred = (pred > 0.5).astype(int)
    gt = (gt > 0.5).astype(int)
    intersection = (pred * gt).sum()
    denominator = pred.sum() + gt.sum()
    if denominator == 0:
        return 1.0
    return (2.0 * intersection) / denominator


dice = dice_score(pred_array, gt_array)
print(f"Dice Score: {dice}")


def jaccard_index(pred, gt):
    pred = (pred > 0.5).astype(int)
    gt = (gt > 0.5).astype(int)
    intersection = (pred * gt).sum()
    union = pred.sum() + gt.sum() - intersection
    if union == 0:
        return 1.0
    return intersection / union


iou = jaccard_index(pred_array, gt_array)
print(f"Jaccard Index (IoU): {iou}")

from scipy.spatial.distance import directed_hausdorff


def hausdorff_distance(pred, gt):
    pred = pred.astype(bool)
    gt = gt.astype(bool)
    pred_coords = np.argwhere(pred)
    gt_coords = np.argwhere(gt)

    if len(pred_coords) == 0 or len(gt_coords) == 0:
        return np.inf

    hd_forward = directed_hausdorff(pred_coords, gt_coords)[0]
    hd_backward = directed_hausdorff(gt_coords, pred_coords)[0]

    return max(hd_forward, hd_backward)


hd = hausdorff_distance(pred_array, gt_array)
print(f"Hausdorff Distance: {hd}")
