#!/usr/bin/python
import matplotlib.pyplot as plt

def show_list_images_and_predictions(imgs, preds, title1 = 'image',title2 = 'prediction'):
    n_img = len(imgs)
    fig, m_axs = plt.subplots(2, n_img, figsize = (n_img*2, 4))
    i = 0
    for (c_im, c_lab) in m_axs.T:
        c_im.imshow(imgs[i])
        c_im.axis('off')
        c_im.set_title(title1)

        c_lab.imshow(y_train[ind])
        c_lab.axis('off')
        c_lab.set_title(title2) 
        i+=1
        
def show_list_images(imgs, titles=None):
    n_img = len(imgs)
    fig, m_axs = plt.subplots(1, n_img, figsize = (n_img*2, 4))
    i = 0
    for (c_im) in m_axs.T:
        c_im.imshow(imgs[i])
        c_im.axis('off')
        if (titles is not None):
            c_im.set_title(titles[i])
        i+=1
