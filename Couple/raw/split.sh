#!/bin/bash

head -n $1 raw.svm > raw.train.svm
tail -n $2 raw.svm > raw.test.svm

