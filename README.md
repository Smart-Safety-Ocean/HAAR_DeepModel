## SSL_HAAR_Model (v.0.5)

여객의 이상행동을 탐지하기 위한 모델 구축.

(이상행동, 위험지역 접근 및 이를 이용한 추락탐지)

/HAAR_Demo 폴더 내의 haar_demo.py를 실행하여 탐지 결과를 확인할 수 있음

요구사항
* Cuda, Cudnn : Cuda support GPU Device (We implemented RTX 3090)
* Detectron 2 
  * Linux or macOS with Python ≥ 3.7
  * PyTorch ≥ 1.8 and torchvision that matches the PyTorch installation. Install them together at pytorch.org to make sure of this
  * OpenCV is optional but needed by demo and visualization
  * See [Detectron Install.md](https://github.com/facebookresearch/detectron2/blob/main/INSTALL.md)
* AdelaiDet
  * Detectron2 base
  * See [AedlaiDet Install.md](https://github.com/aim-uofa/AdelaiDet)
  * FCPose

[Download pretrain Model](https://github.com/aim-uofa/AdelaiDet/blob/master/configs/FCPose/README.md)

[Sample Run Script]
```
python HAAR_Demo/haar_demo.py \
--video-input ./HAAR_Demo/cctv_demo.mp4 \
--opts MODEL.WEIGHTS ./models/fcpose50.pth
```
