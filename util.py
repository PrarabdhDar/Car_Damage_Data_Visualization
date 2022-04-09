def polygon(image_path, data):
    image =  image = cv2.imread(image_path)
    height, width = image.shape[:2]

    color = (rng.randint(0,256), rng.randint(0,256), rng.randint(0,256))

    overlay = image.copy()

    for p in pts:
        image = cv2.polylines(image, np.int32([p]),
                            True, color, 3)
        cv2.fillPoly(overlay, np.int32([p]), color)
        poly_image = cv2.addWeighted(overlay, opacity, image, 1-opacity, 0)

        return asarray(poly_image)

#Second Image Visualization function
def bb(image_path, data):
    image =  image = cv2.imread(image_path)
    height, width = image.shape[:2]

    for i in range(num):
        color = (rng.randint(0,256), rng.randint(0,256), rng.randint(0,256))
        cv2.rectangle(image, start[i], end[i], color, 2)
        bottom.append((top[i][0] + 10*len(label[i]), top[i][1]))
        cv2.rectangle(image, (top[i][0], top[i][1] - 15), bottom[i], (0,0,0), -1)
        cv2.putText(image, label[i], top[i], cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1)

    return asarray(image)
