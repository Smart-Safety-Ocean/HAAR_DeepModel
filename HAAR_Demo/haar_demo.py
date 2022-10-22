# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
import argparse
import glob
import multiprocessing as mp
import os
import time
import cv2
import tqdm

from detectron2.data.detection_utils import read_image
from detectron2.utils.logger import setup_logger

from predictor import VisualizationDemo
from adet.config import get_cfg

# constants
WINDOW_NAME = "HAAR DETECTION RESULT"


def setup_cfg(args):
    # load config from file and command-line arguments
    cfg = get_cfg()
    cfg.merge_from_file(args.config_file)
    cfg.merge_from_list(args.opts)
    # Set score_threshold for builtin models
    cfg.MODEL.RETINANET.SCORE_THRESH_TEST = args.confidence_threshold
    cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = args.confidence_threshold
    cfg.MODEL.FCOS.INFERENCE_TH_TEST = args.confidence_threshold
    cfg.MODEL.MEInst.INFERENCE_TH_TEST = args.confidence_threshold
    cfg.MODEL.PANOPTIC_FPN.COMBINE.INSTANCES_CONFIDENCE_THRESH = args.confidence_threshold
    cfg.freeze()
    return cfg


def get_parser():
    parser = argparse.ArgumentParser(description="HAAR Demo")
    parser.add_argument(
        "--config-file",
        default="/media/hongss/T7/HAAR_DeepModel/AdelaiDet/configs/FCPose/R_50_3X.yaml",
        metavar="FILE",
        help="path to config file",
    )
    parser.add_argument(
        "--detection-mode",
        default="object",
        help="select detection mode = object or key-point"
    )
    parser.add_argument("--video-input", help="Path to video file.")
    parser.add_argument(
        "--confidence-threshold",
        type=float,
        default=0.3,
        help="Minimum score for instance predictions to be shown",
    )
    parser.add_argument(
        "--speed",
        type=int,
        default=2,
        help="Do inference per number of frame",
    )
    parser.add_argument(
        "--opts",
        help="Modify config options using the command-line 'KEY VALUE' pairs",
        default=[],
        nargs=argparse.REMAINDER,
    )
    return parser


if __name__ == "__main__":
    mp.set_start_method("spawn", force=True)
    args = get_parser().parse_args()
    logger = setup_logger()
    logger.info("Arguments: " + str(args))

    cfg = setup_cfg(args)

    demo = VisualizationDemo(cfg)


   #VIDEO INPUT -> OUTPUT WINDOWS
    video = cv2.VideoCapture(args.video_input)
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    frames_per_second = video.get(cv2.CAP_PROP_FPS)
    num_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    basename = WINDOW_NAME + " : " + os.path.basename(args.video_input)
    assert os.path.isfile(args.video_input)
    for vis_frame in tqdm.tqdm(demo.run_on_video(video, speedValue=args.speed), total=num_frames):
        cv2.namedWindow(basename, cv2.WINDOW_NORMAL)
        cv2.resizeWindow(basename, width=1280, height=720)
        textLocationFPS = (50,30)
        cv2.putText(vis_frame,"FPS : "+str(frames_per_second),
                    fontFace=cv2.FONT_HERSHEY_DUPLEX,fontScale=1.0,color=(0,0,0),org=textLocationFPS)
        cv2.imshow(basename, vis_frame)
        if cv2.waitKey(1) == 27:
            break  # esc to quit
    video.release()
    cv2.destroyAllWindows()
# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
import argparse
import glob
import multiprocessing as mp
import os
import time
import cv2
import tqdm

from detectron2.data.detection_utils import read_image
from detectron2.utils.logger import setup_logger

from predictor import VisualizationDemo
from adet.config import get_cfg

# constants
WINDOW_NAME = "HAAR DETECTION RESULT"


def setup_cfg(args):
    # load config from file and command-line arguments
    cfg = get_cfg()
    if(args.detection_mode == "key-point"):
        args.config_file = "/media/hongss/T7/HAAR_DeepModel/AdelaiDet/configs/FCPose/R_50_3X.yaml"
        cfg.merge_from_file(args.config_file)
    elif (args.detection_mode == "FCOS"):
        args.config_file = "/media/hongss/T7/HAAR_DeepModel/AdelaiDet/configs/FCOS-Detection/MS_R_101_2x.yaml"
        cfg.merge_from_file(args.config_file)
    elif (args.detection_mode == "BoxInst"):
        args.config_file = "/media/hongss/T7/HAAR_DeepModel/AdelaiDet/configs/BoxInst/MS_R_101_3x.yaml"
        cfg.merge_from_file(args.config_file)
    cfg.merge_from_list(args.opts)
    # Set score_threshold for builtin models
    cfg.MODEL.RETINANET.SCORE_THRESH_TEST = args.confidence_threshold
    cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = args.confidence_threshold
    cfg.MODEL.FCOS.INFERENCE_TH_TEST = args.confidence_threshold
    cfg.MODEL.MEInst.INFERENCE_TH_TEST = args.confidence_threshold
    cfg.MODEL.PANOPTIC_FPN.COMBINE.INSTANCES_CONFIDENCE_THRESH = args.confidence_threshold
    cfg.freeze()
    return cfg


def get_parser():
    parser = argparse.ArgumentParser(description="HAAR Demo")
    parser.add_argument(
        "--config-file",
        default="/media/hongss/T7/HAAR_DeepModel/AdelaiDet/configs/FCPose/R_50_3X.yaml",
        metavar="FILE",
        help="path to config file",
    )
    parser.add_argument(
        "--detection-mode",
        default="object",
        help="select detection mode = object or key-point"
    )
    parser.add_argument("--video-input", help="Path to video file.")
    parser.add_argument(
        "--confidence-threshold",
        type=float,
        default=0.3,
        help="Minimum score for instance predictions to be shown",
    )
    parser.add_argument(
        "--speed",
        type=int,
        default=2,
        help="Do inference per number of frame",
    )
    parser.add_argument(
        "--opts",
        help="Modify config options using the command-line 'KEY VALUE' pairs",
        default=[],
        nargs=argparse.REMAINDER,
    )
    return parser


if __name__ == "__main__":
    mp.set_start_method("spawn", force=True)
    args = get_parser().parse_args()

    logger = setup_logger()
    logger.info("Arguments: " + str(args))

    cfg = setup_cfg(args)

    demo = VisualizationDemo(cfg)

   #VIDEO INPUT -> OUTPUT WINDOWS
    video = cv2.VideoCapture(args.video_input)
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    frames_per_second = video.get(cv2.CAP_PROP_FPS)
    num_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    basename = WINDOW_NAME + " : " + os.path.basename(args.video_input)
    assert os.path.isfile(args.video_input)
    for vis_frame in tqdm.tqdm(demo.run_on_video(video, speedValue=args.speed), total=num_frames):
        cv2.namedWindow(basename, cv2.WINDOW_NORMAL)
        cv2.resizeWindow(basename, width=1280, height=720)
        textLocationFPS = (50,30)
        cv2.putText(vis_frame,"FPS : "+str(frames_per_second),
                    fontFace=cv2.FONT_HERSHEY_DUPLEX,fontScale=1.0,color=(0,0,0),org=textLocationFPS)
        cv2.imshow(basename, vis_frame)
        if cv2.waitKey(1) == 27:
            break  # esc to quit
    video.release()
    cv2.destroyAllWindows()
