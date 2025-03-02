import SimpleITK as sitk

input_file = 'D:/TotalSegmentator/data_all/TotalsegmentatorMRI_dataset_v200/s0029/mri.nii.gz'
image = sitk.ReadImage(input_file)

#median
median_radius = 2  #!!!!!!!!!!!!!!!!!!!!!
median_filter = sitk.MedianImageFilter()
median_filter.SetRadius(median_radius)
median_image = median_filter.Execute(image)

#gauss
sigma = 1.5  #!!!!!!!!!!!!!!!!!!!!!!!!!
gaussian_filter = sitk.DiscreteGaussianImageFilter()
gaussian_filter.SetVariance(sigma**2)
smoothed_image = gaussian_filter.Execute(image)

output_file = 'D:/TotalSegmentator/data_all/TotalsegmentatorMRI_dataset_v200/s0029/preCT.nii.gz'
sitk.WriteImage(smoothed_image, output_file)

print(f"Processed image (Median + Gaussian) saved to {output_file}")
