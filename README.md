# safe_detection
## 一些训练参数

yolo task=detect mode=train model=yolov8n.pt data=detect.yaml device=0 batch=15 imgsz=800 workers=1


yolo task=detect mode=val model=runs/detect/train34/weights/best.pt data=detect.yaml device=0 iou=0.5 conf=0.4 imgsz=800 workers=1


yolo task=detect mode=val model=runs/detect/train19/weights/best.pt data=detect.yaml batch=15 device=0 workers=1


yolo task=detect mode=predict model=runs/detect/train34/weights/best.pt data=detect.yaml device=0 source=data/images/test conf=0.4 iou=0.6 save_txt=true hide_conf=false

## 结果保存在pred.zip中

## 修改了ultralytics/utils/loss.py中的损失权重以适应本任务，改动幅度很小，不再上传ultralytics的代码
