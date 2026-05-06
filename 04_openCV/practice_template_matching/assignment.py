
import cv2
import matplotlib.pyplot as plt
import numpy as np

# 이미지 불러오기  
SCENE_PATH = "scene.jpg"
TEMPLATE_PATH = "template.jpg"
RESULT_PATH = "result.png"

def load_image(path):
    image = cv2.imread(path)
    if image is None:
        raise FileNotFoundError(f"Cannot load image: {path}")
    return image

scene = load_image(SCENE_PATH)
template = load_image(TEMPLATE_PATH)

# 1. 이미지 전처리 
# 그레이 스케일 변환 
scene_gray = cv2.cvtColor(scene, cv2.COLOR_BGR2GRAY)
template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

# 가우시안 블러 적용 
scene_blur = cv2.GaussianBlur(scene_gray, (5, 5), 0) # (5,5) 일반적, 홀수만 사용 가능 


# 블러 적용 전 후 비교 출력 
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.imshow(scene_gray, cmap="gray")
plt.title("Before Blur")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(scene_blur, cmap="gray")
plt.title("After Gaussian Blur")
plt.axis("off")
plt.tight_layout()
plt.show()


# 2. 템플릿 매칭 수행 
# 가장 유사한 위치 탐색 
match_result = cv2.matchTemplate(scene_blur, template_gray, cv2.TM_CCOEFF_NORMED) # 1에 가까수록 비슷 
# 최적 위치(좌표) 추출 
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(match_result)

# 매칭 유사도 출력 
top_left = max_loc
template_h, template_w = template_gray.shape
bottom_right = (top_left[0] + template_w, top_left[1] + template_h)

print(f"Best match location: {top_left}")
print(f"Similarity score: {max_val:.4f}")


# 3. 결과 시각화 
result_image = scene.copy()
# 바운딩 박스 그리기 
cv2.rectangle(result_image, top_left, bottom_right, (0, 0, 255), 3) # (0, 0, 255)R 빨간색, 3 두께
# 텍스트 표시 
cv2.putText(
    result_image,
    "Found!",
    (top_left[0], max(30, top_left[1] - 10)),
    cv2.FONT_HERSHEY_SIMPLEX,
    1.0,
    (0, 0, 255),
    2,
    cv2.LINE_AA,
)

# 박스와 글자 그려진 이미지 저장 
cv2.imwrite(RESULT_PATH, result_image)

# 원본과 결과 이미지 출력 
scene_rgb = cv2.cvtColor(scene, cv2.COLOR_BGR2RGB)
result_rgb = cv2.cvtColor(result_image, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.imshow(scene_rgb)
plt.title("Original Scene")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(result_rgb)
plt.title("Template Matching Result")
plt.axis("off")
plt.tight_layout()
plt.show()


# 4. 이진화로 후처리 시각화 
threshold = 0.8
binary_heatmap = np.where(match_result >= threshold, 255, 0).astype(np.uint8)

plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.imshow(match_result, cmap="hot")
plt.title("Template Matching Heatmap")
plt.colorbar()
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(binary_heatmap, cmap="gray")
plt.title(f"Binary Heatmap (threshold={threshold})")
plt.axis("off")
plt.tight_layout()
plt.show()
