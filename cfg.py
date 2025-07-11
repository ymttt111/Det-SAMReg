import argparse


def parse_args():    
    parser = argparse.ArgumentParser()
    parser.add_argument('-net', type=str, default='sam2', help='net type')
    parser.add_argument('-checkpoint_path', type=str, default='work_dir/checkpoint', help='net type')
    parser.add_argument('-encoder', type=str, default='vit_b', help='encoder type')
    parser.add_argument('-exp_name', default='prstate_experiment', type=str, help='experiment name')
    parser.add_argument('-vis', type=bool, default=False, help='Generate visualisation during validation')
    parser.add_argument('-train_vis', type=bool, default=False, help='Generate visualisation during training')
    parser.add_argument('-prompt', type=str, default='bbox', help='type of prompt, bbox or click')
    parser.add_argument('-prompt_freq', type=int, default=1, help='frequency of giving prompt in 3D images')
    parser.add_argument('-pretrain', type=str, help='path of pretrain weights',default='/home/adminer/code/auto_reg/checkpoints/sam2_hiera_small.pt')
    parser.add_argument('-mr_pretrain', type=str, help='path of pretrain weights',default= '/home/adminer/code/Det-SAMReg-demo/checkpoint/MR-SAM.pth')
    parser.add_argument('-us_pretrain', type=str, help='path of pretrain weights',default='/home/adminer/code/Det-SAMReg-demo/checkpoint/US-SAM.pth')

    parser.add_argument('-val_freq',type=int,default=1,help='interval between each validation')
    parser.add_argument('-gpu', type=bool, default=True, help='use gpu or not')
    parser.add_argument('-gpu_device', type=int, default=0, help='use which gpu')
    parser.add_argument('-image_size', type=int, default=1024, help='image_size')
    parser.add_argument('-out_size', type=int, default=1024, help='output_size')
    parser.add_argument('-distributed', default='none' ,type=str,help='multi GPU ids to use')
    parser.add_argument('-dataset', default='prostate' ,type=str,help='dataset name')
    parser.add_argument('-sam_ckpt', type=str, 
                        default='checkpoints/sam2_hiera_small.pt' , help='sam checkpoint address')
    parser.add_argument('-sam_config', type=str, default='sam2_hiera_s' , help='sam checkpoint address')
    parser.add_argument('-video_length', type=int,default=3,  help='sam checkpoint address') # 
    parser.add_argument('-b', type=int, default=1, help='batch size for dataloader')
    parser.add_argument('-lr', type=float, default=1e-4, help='initial learning rate')
    parser.add_argument('-weights', type=str, default = 0, help='the weights file you want to test')
    parser.add_argument('-multimask_output', type=int, default=1 , help='the number of masks output for multi-class segmentation')
    parser.add_argument('-memory_bank_size', type=int, default=16, help='sam 2d memory bank size')
    parser.add_argument('-data_num', type=int, default=14)
    parser.add_argument('-noise', type=int, default=0)
    parser.add_argument(
    '-data_path',
    type=str,
    default='The path of data',
    help='The path of segmentation data')
    opt = parser.parse_args()

    return opt
