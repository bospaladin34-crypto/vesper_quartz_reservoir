#!/usr/bin/env python3
import tensorflow as tf
import numpy as np
import os

NU_P = 0.17259029
F0 = 15.965
PHI = 1.6180339887
TWO_PI = 6.28318530718

print("[|||] NEPHILIM NPU CONVERTER v0.1")

class PhasonModel(tf.Module):
    def __init__(self):
        super().__init__()
        self.nu_p = tf.Variable(NU_P, trainable=False, dtype=tf.float32)
        self.f0 = tf.Variable(F0, trainable=False, dtype=tf.float32)
        self.two_pi = tf.constant(TWO_PI, dtype=tf.float32)
    @tf.function(input_signature=[tf.TensorSpec(shape=[1], dtype=tf.float32)])
    def __call__(self, t):
        angle = self.two_pi * self.f0 * t
        real = self.nu_p * tf.cos(angle)
        imag = self.nu_p * tf.sin(angle)
        return tf.stack([real, imag])

phason = PhasonModel()
tf.saved_model.save(phason, "phason_saved")

class StomachionGenerator(tf.Module):
    def __init__(self):
        super().__init__()
        seeds = [(i * NU_P) % 1.0 for i in range(536)]
        self.seeds = tf.constant(seeds, dtype=tf.float32)
        self.phi = tf.constant(PHI, dtype=tf.float32)
    @tf.function(input_signature=[tf.TensorSpec(shape=[], dtype=tf.int32)])
    def __call__(self, index):
        seed = self.seeds[index]
        pieces = []
        for i in tf.range(14):
            angle = seed * 3.14159 * tf.cast(i+1, tf.float32) * self.phi
            x = tf.cos(angle) * seed
            y = tf.sin(angle) * seed
            pieces.append(tf.stack([x, y]))
        return tf.stack(pieces)

stomachion = StomachionGenerator()
tf.saved_model.save(stomachion, "stomachion_saved")

def convert(saved, out):
    converter = tf.lite.TFLiteConverter.from_saved_model(saved)
    converter.optimizations = [tf.lite.Optimize.DEFAULT]
    tfl = converter.convert()
    open(out, "wb").write(tfl)
    print("Created", out, os.path.getsize(out), "bytes")

convert("phason_saved", "phason_npu.tflite")
convert("stomachion_saved", "stomachion_npu.tflite")
