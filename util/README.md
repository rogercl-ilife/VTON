
# Resizing cloth
* The implementation of data_processing is based on codes repo [M3D-VTON](https://github.com/fyviezhao/M3D-VTON)

Follwing parts are used to calculate roi.
```
parse_roi = (parse_array == 14).astype(np.float32) + \
            (parse_array == 15).astype(np.float32) + \
            (parse_array == 5).astype(np.float32)
```

* Parsing table could be found in [2D-Human-Parsing](https://github.com/fyviezhao/2D-Human-Parsing)

| Part       | index | Part        | index |
|------------|-------|------------ |-------| 
| background |  0    | neck        | 10    |
| hat        |  1    | scarf       | 11    |
| hair       |  2    | skirt       | 12    |
| -	 |  3    | face        | 13    |
| sunglass   |  4    | left arm    | 14    |
| shirt	 |  5    | right arm   | 15    | 
| dress	 |  6    | left leg    | 16    |  
| coats	 |  7    | right leg   | 17    | 
| -	 |  8    | left shoe   | 18    | 
| pant	 |  9    | right shoe  | 19    | 


# Appling DensePose 
* The steps are referred from [HR-VITON](https://github.com/sangyun884/HR-VITON/issues/45)





# Acknowledgement and Citations
* The implementation of data_processing is based on codes repo [M3D-VTON](https://github.com/fyviezhao/M3D-VTON) <br />
```
   @InProceedings{M3D-VTON,
    author    = {Zhao, Fuwei and Xie, Zhenyu and Kampffmeyer, Michael and Dong, Haoye and Han, Songfang and Zheng, Tianxiang and Zhang, Tao and Liang, Xiaodan},
    title     = {M3D-VTON: A Monocular-to-3D Virtual Try-On Network},
    booktitle = {Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)},
    month     = {October},
    year      = {2021},
    pages     = {13239-13249}
}
```
