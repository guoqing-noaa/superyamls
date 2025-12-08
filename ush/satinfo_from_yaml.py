#!/usr/bin/env python
import yaml

def parse_channels(s):
    if "-" in s:  # range format like "7-16"
        start, end = map(int, s.split("-"))
        return list(range(start, end + 1))
    else:  # comma-separated format like "7,8,9,10,11,12,13,14,15"
        return list(map(int, s.split(",")))

yfile = open("jedivar.yaml", "r")
data = yaml.safe_load(yfile)
observers = data["cost function"]["observations"]["observers"]

for obs in observers:
    obsSpace = obs["obs space"]
    obsName = obsSpace["name"]

    channels, use_flag, use_flag_clddet, error, obserr_bound_max = [], [], [], [], []
    if "_anchor_channels" in obsSpace.keys():
        channels = parse_channels(obsSpace["_anchor_channels"])
    elif "_anchor_use_flag" in obsSpace.keys():
        use_flag = obsSpace["_anchor_use_flag"]
    elif "_anchor_use_flag_clddet" in obsSpace.keys():
        use_flag_clddet = obsSpace["_anchor_use_flag_clddet"]
    elif "_anchor_error" in obsSpace.keys():
        error = obsSpace["_anchor_error"]
    elif "_anchor_obserr_bound_max" in obsSpace.keys():
        obserr_bound_max = obsSpace["_anchor_obserr_bound_max"]

    if not use_flag_clddet:
        use_flag_clddet = [-1] * len(channels)

    if channels:  # an radiance observer
        for ch, iuse in zip(channels, use_flag):
            line = f" {obsName<21}{ch:4}{iuse:4}{}"

