import argparse
import pandas as pd
import os.path as osp

if __name__ == '__main__':


    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--data_root', type=str, default='/covis/C-VTON/data/viton',help='path to the dataset')
    parser.add_argument('--dataset',   type=str, default='viton',help='viton or viton-hd dataset')
    parser.add_argument('--datamode',  type=str, default='train',help='train or test stage')
    parser.add_argument('--ofile',     type=str, default='viton_train_pairs_new.txt',help='new pair list')
    opt, _ = parser.parse_known_args()

    data_root = opt.data_root
    dataset   = opt.dataset
    datamode  = opt.datamode

    # read file list
    #======================================================================================
    if dataset == "viton" :
         filepath_df = pd.read_csv(osp.join(data_root, "viton_%s_pairs.txt" % ("test" if datamode == "test" else "train")), sep=" ", names=["image", "cloth"])
         ofile = "viton_%s_pairs_new.txt" % ("test" if datamode == "test" else "train")

    f = open(ofile, "w") 

    # check if file exists or not
    #======================================================================================
    cnt = 0 
    for i in range(len(filepath_df)):
      img   = osp.join("data/image",filepath_df.loc[i].at["image"])
      cloth = osp.join("data/cloth",filepath_df.loc[i].at["cloth"])
      if osp.isfile(img) and osp.isfile(cloth) :
         msg = filepath_df.loc[i].at["image"] + " " + filepath_df.loc[i].at["cloth"] + "\n"
         f.write(msg)
         cnt = cnt + 1
    
    # Display message
    #======================================================================================
    msg = "Original list has " + str(len(filepath_df)) + "pairs!"
    print(msg)

    msg = "new list has " + str(cnt) + "pairs!"
    print(msg)

    f.close()
