import torch
import time
from torchvision import models
from torchvision.models import MobileNet_V2_Weights
from PIL import Image

# -------------------------
# Load pretrained model (modern API)
# -------------------------
weights = MobileNet_V2_Weights.DEFAULT
model = models.mobilenet_v2(weights=weights)
model.eval()

# -------------------------
# Load ImageNet labels
# -------------------------
with open("imagenet_classes.txt") as f:
    labels = [line.strip() for line in f.readlines()]

# -------------------------
# Load and preprocess image
# -------------------------
img = Image.open("test.png").convert("RGB")
preprocess = weights.transforms()
input_tensor = preprocess(img).unsqueeze(0)

# -------------------------
# Warm-up (important for benchmarking)
# -------------------------
for _ in range(5):
    with torch.no_grad():
        model(input_tensor)

# -------------------------
# Measure inference latency
# -------------------------
start = time.time()
with torch.no_grad():
    output = model(input_tensor)
end = time.time()

latency_ms = (end - start) * 1000

# -------------------------
# Compute probabilities and top-5 predictions
# -------------------------
probabilities = torch.nn.functional.softmax(output[0], dim=0)
top5_prob, top5_idx = torch.topk(probabilities, 5)

print("\n===== CNN Inference Result =====")
for i in range(5):
    print(f"Rank {i+1}: {labels[top5_idx[i]]}  (Prob = {top5_prob[i].item():.4f})")

print("\nInference Latency: %.3f ms" % latency_ms)
print("FPS (Frames Per Second): %.2f" % (1000/latency_ms))
