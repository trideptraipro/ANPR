import cv2
import numpy as np


kernel = np.ones((3, 3), np.uint8)
img = cv2.imread("pl.jpg")  # đọc ảnh
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Chuyển ảnh sang xám
noise_removal = cv2.bilateralFilter(imgGray, 9, 75, 75)  # Remove noise, giảm noise tăng edge
equalHistogram = cv2.equalizeHist(noise_removal)
# Căn bằng lại histogram(Biểu đò tần suất thống kê xuất hiện mức sáng) làm cho ảnh k quá sáng hoặc quá tối
kernel1 = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
imgMorph = cv2.morphologyEx(equalHistogram, cv2.MORPH_OPEN, kernel1, iterations=20)
# Morphogoly open mục đích là giảm edge nhiễu, edge thật thêm sắc nhọn bằng cv2.morpholygyEx sử dụng kernel 5x5
imgSubMorph = cv2.subtract(equalHistogram, imgMorph)
# Xóa phông background k cần thiết
ret, imgThresh = cv2.threshold(imgSubMorph, 0, 255, cv2.THRESH_OTSU)
# Dùng threshold OTSU(làm việc rất tốt trong bimodel histogram) đưa ảnh về trắng đen tách biệt background và interesting
imgCanny = cv2.Canny(imgThresh, 250, 255)
# Thuật toán Canny phát hiện cạnh Tham khảo thuật toán Canny tại: https://minhng.info/tutorials/xu-ly-anh-opencv-hien-thuc-canny-edge.html
ImgDilated = cv2.dilate(imgCanny, kernel, iterations=1)
# Dilated sẽ shape cho edge, tức là gắn kết những điểm bị gãy

cv2.imshow("Image Dilated", ImgDilated)


contours, hierarchy = cv2.findContours(ImgDilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# Tìm contour trả về 3 giá trị chỉ quan tâm giá trị 2
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
# Lọc contours chỉ lấy 10 contours có giá trị lớn nhất
screenCnt = None
for c in contours:
    peri = cv2.arcLength(c, True)  # Lấy chu vi của contour
    approx = cv2.approxPolyDP(c, 0.06 * peri, True)
    # xác định đa giác ở đây cần tìm, vì biểu số xe là hình chữ nhật nên t chỉ lấy contour nào 4 cạnh
    if len(approx) == 4:
        screenCnt = approx
        break

mask=np.zeros(ImgDilated.shape)
cv2.drawContours(mask,[screenCnt], -1,255, thickness=-1)

y_nonzeros, x_nonzeros=np.nonzero(mask)
x_min=np.min(x_nonzeros)
y_min=np.min(y_nonzeros)
x_max=np.max(x_nonzeros)
y_max=np.max(y_nonzeros)
cv2.imshow("new", img)





# Segmentation các kí tự trên biển số xe
roi=img[y_min:y_max,x_min:x_max]
roiGray=cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
roiBlur=cv2.GaussianBlur(roiGray,(3,3),1)
#Lọc nhiễu
ret, roiThresh=cv2.threshold(roiBlur,120,255,cv2.THRESH_BINARY_INV)
#Đưa ảnh về trắng đen
kernel2=cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
threshMorph=cv2.morphologyEx(roiThresh, cv2.MORPH_DILATE, kernel2)
cont,hier=cv2.findContours(threshMorph, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
#Tiếp tục tìm contours cho kí tự

#####Tìm Tập hợp cái index #####
areas_index={}
areas=[]
for ind, cnt in enumerate(cont):
    area=cv2.contourArea(cnt)
    areas_index[area]=ind
    areas.append(area)
areas=sorted(areas, reverse=True)[0:10]
for i in areas:
    (x,y,w,h)= cv2.boundingRect(cont[areas_index[i]])
    cv2.rectangle(roi, (x,y),(x+w, y+h), (0,255,0), 2)

print(areas)

plt.imshow(cv2.cvtColor(roi, cv2.COLOR_BGR2RGB))
cv2.imshow("Thresh", roiThresh)
cv2.imshow("THresh Morphology", threshMorph)
cv2.imshow("r", roi)
cv2.waitKey(0)
