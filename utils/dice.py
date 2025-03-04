# utils.py

import numpy as np


def dice_coef(y_true, y_pred, smooth=1e-6):
    '''
    returns the dice coefficient for y_true and y_pred
    y_true and y_pred must be one label
    '''
    y_true_f = y_true.flatten()
    y_pred_f = y_pred.flatten()
    intersection = np.sum(y_true_f * y_pred_f)
    y_sum = np.sum(y_true_f) + np.sum(y_pred_f)
    return (2 * intersection + smooth) / (y_sum + smooth)

    # y_true_f = y_true.contiguous().view(-1)
    # y_pred_f = y_pred.contiguous().view(-1)
    # intersection = (y_true_f * y_pred_f).sum()
    # return (2. * intersection + smooth) / (y_true_f.sum() + y_pred_f.sum() + smooth)


def dice_coef_multilabel(y_true, y_pred, numLabels):
    '''
    returns the dice coefficient for y_true and y_pred for multilabels
    '''
    dice = 0
    for i in range(1, numLabels):
        y_true_norm = np.where(y_true == i, 1, 0).astype(np.uint8)
        y_pred_norm = np.where(y_pred == i, 1, 0).astype(np.uint8)
        dice += dice_coef(y_true_norm, y_pred_norm)
        
    # @MPR
    return dice / numLabels


def dice_coef_per_label(y_true, y_pred, numLabels):
    '''
    returns the dice coefficient for y_true and y_pred for each label
    '''
    label_dice_dict = {}
    for i in range(1, numLabels):
        y_true_norm = np.where(y_true == i, 1, 0).astype(np.uint8)
        y_pred_norm = np.where(y_pred == i, 1, 0).astype(np.uint8)
        label_dice_dict[i] = dice_coef(y_true_norm, y_pred_norm)
    return label_dice_dict