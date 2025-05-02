import numpy as np
import math
from math import cos,sin
import open3d
import scipy.linalg as la
import cv2

# 绕x轴旋转
def rotation_x(θ):
    return np.array([[1,           0,            0],
                     [0, math.cos(θ), -math.sin(θ)],
                     [0, math.sin(θ),  math.cos(θ)]])
# 绕y轴旋转
def rotation_y(θ):
    return np.array([[ math.cos(θ), 0, math.sin(θ)],
                     [           0, 1,           0],
                     [-math.sin(θ), 0, math.cos(θ)]])
# 绕z轴旋转
def rotation_z(θ):
    return np.array([[math.cos(θ), -math.sin(θ), 0],
                     [math.sin(θ),  math.cos(θ), 0],
                     [0          ,            0, 1]])

# 绕任意轴旋转
def rotation_k_θ(k,θ):
    '''
    input:
        k   :   [x,y,z], symmetry_axis
        θ   :   rad, rotation angle
    output:
        R   :   rotation matrix R(k,θ)
    '''
    return np.array([[k[0]*k[0]*(1-cos(θ))+cos(θ)     , k[1]*k[0]*(1-cos(θ))-k[2]*sin(θ), k[2]*k[0]*(1-cos(θ))+k[1]*sin(θ)],
                        [k[0]*k[1]*(1-cos(θ))+k[2]*sin(θ), k[1]*k[1]*(1-cos(θ))+cos(θ)     , k[2]*k[1]*(1-cos(θ))-k[0]*sin(θ)],
                        [k[0]*k[2]*(1-cos(θ))-k[1]*sin(θ), k[1]*k[2]*(1-cos(θ))+k[0]*sin(θ), k[2]*k[2]*(1-cos(θ))+cos(θ)]])

# 旋转矩阵与RPY角
def R2rpy(R):
    beta_y = np.arctan2(-R[2][0],np.sqrt(np.sum(np.square(R[0][0])+np.square(R[1][0]))))*180.0/np.pi
    alpha_z = np.arctan2(R[1][0],R[0][0])*180.0/np.pi
    gamma_x = np.arctan2(R[2][1],R[2][2])*180.0/np.pi
    return gamma_x , beta_y , alpha_z

def rpy2R(gamma_x , beta_y , alpha_z):
    return np.dot(rotation_z(alpha_z),rotation_y(beta_y)).dot(rotation_x(gamma_x))

