#!/usr/bin/env python3
import psutil

percentile = psutil.cpu_percent()

vm = psutil.virtual_memory()

print(dict(vm._asdict()))

print(vm.percent)

print(percentile)

print(vm.available * 100 / vm.total)
