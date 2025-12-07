#!/usr/bin/env python
# POC: Guoqing.Ge@noaa.gov
#
import os
import sys
# list of available observers
dcObserver = {
    "adpsfc_t181": "adpsfc_airTemperature_181",
    "adpsfc_t183": "adpsfc_airTemperature_183",
    "adpsfc_t187": "adpsfc_airTemperature_187",
    "adpsfc_q181": "adpsfc_specificHumidity_181",
    "adpsfc_q183": "adpsfc_specificHumidity_183",
    "adpsfc_q187": "adpsfc_specificHumidity_187",
    "adpsfc_ps181": "adpsfc_stationPressure_181",
    "adpsfc_ps187": "adpsfc_stationPressure_187",
    "adpsfc_uv281": "adpsfc_winds_281",
    "adpsfc_uv284": "adpsfc_winds_284",
    "adpsfc_uv287": "adpsfc_winds_287",
# adpupa
    "adpupa_t120": "adpupa_airTemperature_120",
    "adpupa_t132": "adpupa_airTemperature_132",
    "adpupa_q120": "adpupa_specificHumidity_120",
    "adpupa_q132": "adpupa_specificHumidity_132",
    "adpupa_ps120": "adpupa_stationPressure_120",
    "adpupa_uv220": "adpupa_winds_220",
    "adpupa_uv232": "adpupa_winds_232",
# aircar, aircft
    "aircar_t133": "aircar_airTemperature_133",
    "aircar_q133": "aircar_specificHumidity_133",
    "aircar_uv233": "aircar_winds_233",
    "aircft_t130": "aircft_airTemperature_130",
    "aircft_t131": "aircft_airTemperature_131",
    "aircft_t134": "aircft_airTemperature_134",
    "aircft_t135": "aircft_airTemperature_135",
    "aircft_q134": "aircft_specificHumidity_134",
    "aircft_uv230": "aircft_winds_230",
    "aircft_uv231": "aircft_winds_231",
    "aircft_uv234": "aircft_winds_234",
    "aircft_uv235": "aircft_winds_235",
# ztd, msonet, proflr, rassda
    "gnss_ztd": "gnss_zenithTotalDelay",
    "msonet_t188": "msonet_airTemperature_188",
    "msonet_q188": "msonet_specificHumidity_188",
    "msonet_ps188": "msonet_stationPressure_188",
    "msonet_uv288": "msonet_winds_288",
    "proflr_uv227": "proflr_winds_227",
    "rassda_t126": "rassda_airTemperature_126",
# sfcshp, vadwnd
    "sfcshp_t180": "sfcshp_airTemperature_180",
    "sfcshp_t182": "sfcshp_airTemperature_182",
    "sfcshp_t183": "sfcshp_airTemperature_183",
    "sfcshp_q180": "sfcshp_specificHumidity_180",
    "sfcshp_q182": "sfcshp_specificHumidity_182",
    "sfcshp_q183": "sfcshp_specificHumidity_183",
    "sfcshp_ps180": "sfcshp_stationPressure_180",
# "sfcshp_ps182": "sfcshp_stationPressure_182",
    "sfcshp_uv280": "sfcshp_winds_280",
    "sfcshp_uv282": "sfcshp_winds_282",
    "sfcshp_uv284": "sfcshp_winds_284",
    "vadwnd_uv224": "vadwnd_winds_224",
# AMV
    "satwnd_uv245_270": "satwnd_winds_245_270",
    "satwnd_uv245_272": "satwnd_winds_245_272",
    "satwnd_uv246_270": "satwnd_winds_246_270",
    "satwnd_uv246_272": "satwnd_winds_246_272",
# satellite obs
    "rad_amsua_n19": "amsua_n19",
    "rad_atms_n20": "atms_n20",
    "rad_atms_npp": "atms_npp",
    "rad_abi_g16": "abi_g16",
    "rad_abi_g18": "abi_g18",
    "rad_atms_n21": "atms_n21",
    "rad_amsua_metop-b": "amsua_metop-b",
    "rad_amsua_metop-c": "amsua_metop-c",
    }

#
# read observers under jcb-rdas, make modifications and output to jcb-obs1/
#
for key, value in dcObserver.items():
    real_key = key
    if key.startswith("rad_"):
        real_key = key[4:]
    finput = "./jcb-rdas/" + value + ".yaml.j2"
    outfile = open("./jcb-obs1/" + value + ".yaml.j2", 'w')
    # link to link2rrfs
    os.makedirs('./link2rrfs', exist_ok=True)
    dest = f"./link2rrfs/{real_key}.yaml"
    if os.path.exists(dest):
        os.remove(dest)
    os.symlink(f"../jcb-obs1/{value}.yaml.j2", dest)
    # read all lines from an observer
    block = []
    with open(finput, 'r') as infile:
        for line in infile:
            block.append(line)

    # replace, comment, change
    comment_zone = False
    for i, line in enumerate(block):
        if value in line:
            line = line.replace(value, real_key)
            if ".nc4" in line:
                line = line.replace(".nc4", ".nc")
        elif "gnss_ztd_zenithTotalDelay" in line:
            line = line.replace("gnss_ztd_zenithTotalDelay", "gnss_ztd")
        elif "{{distribution}}" in line:
            line = line.replace("{{distribution}}", "RoundRobin")
        elif "{{empty_obs_space_action}}" in line:
            line = line.replace("{{empty_obs_space_action}}", "@emptyObsSpaceAction@")

        # comment out temporal thinning by default
        elif "# Duplicate Check" in line:
            comment_zone=True
        elif comment_zone:
            # nspaces = len(line) - len(line.lstrip())
            line="#" + line
            if "reduce obs space" in line:
                comment_zone=False
            elif "{{atmosphere_background_time_iso}}" in line:
                line=line.replace("{{atmosphere_background_time_iso}}", "@analysisDate@")
        # ~~~~~~~~
        block[i]=line

    # remove the following block
    # # Reduce observation error and turn off ObsErrorFactorPressureCheck
    for i, line in enumerate(block):
        if '# Reduce observation error and turn off ObsErrorFactorPressureCheck' in line:
            pos=i
            del block[pos:pos + 8]
            break

    # remove the first two unnessary filters excpet wind288
    knt=0
    for i, line in enumerate(block):
        if "- filter:" in line:
            knt += 1
            if knt == 1:
                pos1=i
            elif knt == 3:
                pos2=i
                break
    # remove lines from pos1 to pos2-1
    if block[pos1 - 1].strip().startswith("#"):
        pos1 -= 1
    if block[pos2 - 1].strip().startswith("#"):
        pos2 -= 1
    if not "msonet_winds_288.yaml" in finput and not key.startswith("rad_"):
        del block[pos1:pos2]
    else:
        # remove the two unnessary filters for uv288
        for i, line in enumerate(block):
            if "# Accept, reject, or passivate (monitor)" in line:
                pos=i
                del block[pos:pos + 24]
                break

    # write out lines
    for line in block:
        outfile.write(line)
#
# print out information
#
print("files under 'jcb-obs1/' updated")
print("links under 'link2rrfs/' made")
