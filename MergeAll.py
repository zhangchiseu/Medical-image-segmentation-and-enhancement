import numpy as np
import SimpleITK as sitk
import os
import matplotlib.pyplot as plt
input_dir = "D:/TotalSegmentator/data_all/PulmonaryCT/s0029/segmentations"
output_path = "D:/TotalSegmentator/data_all/PulmonaryCT/s0029/merged_segmentation.nii.gz"
merged_image = None

for i, filename in enumerate(sorted(os.listdir(input_dir))):
    if filename.endswith(".nii.gz"):
        file_path = os.path.join(input_dir, filename)
        image = sitk.ReadImage(file_path)
        array = sitk.GetArrayFromImage(image)
        if merged_image is None:
            merged_image = np.zeros_like(array, dtype=np.uint16)

        merged_image[array == 1] = i + 1

merged_image = sitk.GetImageFromArray(merged_image)
merged_image.CopyInformation(image)
sitk.WriteImage(merged_image, output_path)

print(f"Merged segmentation saved to {output_path}")
