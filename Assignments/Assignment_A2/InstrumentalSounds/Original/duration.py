import csv
import wave
import contextlib
import statistics

final_list = ['acco_gref_mg_qu_mf_sol2_12', 'acco_gref_mg_qu_mf_sol3_12', 'acco_gref_mg_qu_mf_sol4_12', 'acco_gref_mg_qu_mf_sol5_1', 'acco_gref_mg_se_mf_sol0_12',
              'acco_gref_mg_se_mf_sol1_12', 'acco_gref_mg_se_mf_sol2_12', 'acco_gref_mg_se_mf_sol3_12', 'acco_gref_mg_se_mf_sol4_12', 'bsn_gref_mf_sol1_12',
              'bsn_gref_mf_sol2_12', 'bsn_gref_mf_sol3_12', 'cb_d_gref_mf_sol1_12', 'cb_d_gref_mf_sol2_12', 'cb_g_gref_mf_sol1_12', 'cb_g_gref_mf_sol2_12',
              'cb_g_gref_mf_sol3_12', 'clsb_gref_mf_sol2_12', 'clsb_gref_mf_sol3_12', 'clsb_gref_mf_sol4_12', 'clsb_gref_mf_sol5_12', 'fltu_gref_mf_sol3_12',
              'fltu_gref_mf_sol4_12', 'fltu_gref_mf_sol5_12', 'gui_gref_a_mf_sol2_12', 'gui_gref_b_mf_sol3_12', 'gui_gref_d_mf_sol2_12', 'gui_gref_d_mf_sol3_12',
              'gui_gref_el_mf_sol1_12', 'gui_gref_el_mf_sol2_12', 'gui_gref_e_mf_sol3_12', 'gui_gref_e_mf_sol4_12', 'gui_gref_g_mf_sol2_12', 'gui_gref_g_mf_sol3_12',
              'harp_gref_mf_sol0_12', 'harp_gref_mf_sol1_12', 'harp_gref_mf_sol2_12', 'harp_gref_mf_sol3_12', 'harp_gref_mf_sol4_12', 'harp_gref_mf_sol5_12',
              'harp_gref_mf_sol6_12', 'others_101137__cgeffex__Organ_play-ball-old1', 'others_101137__cgeffex__Organ_play-ball', 'others_158628__Hammond-tonewheel-organ',
              'others_168578_wah-clavinet-funky', 'others_196006__corsica-s__fender', 'others_208055__ueffects__deep-noise', 'others_25483__raggaman__rhodes-loop-01-116',
              'per_102802__mhc__acoustic-tom6', 'per_117005__cbeeching__soft-cymbal', 'per_132585__rob10__kick-drum-e', 'per_139501__robertmcdonald__big-hit-1',
              'per_173838__rocknessmonster89__tom-high', 'per_183109__dwsd__prc-phat909roomtom', 'per_212208__alexthegr81__tapesnare-15', 'per_34828__zin__hi-snare-1',
              'per_39663__markgia__cymbal-swish-long', 'per_41439__sandyrb__srbm-tom-003', 'per_56436__surfjira__kick-feltbeater-medium', 'per_56454__surfjira__snare-rimshot-hard3',
              'per_56461__surfjira__tom1-medium', 'per_56471__surfjira__tom2-medium', 'per_86334__zgump__tom-0104', 'per_snare', 'sax_gref_mf_sol2_12', 'sax_gref_mf_sol3_12',
              'sax_gref_mf_sol4_12', 'tbtb_gref_mf_sol1_12', 'tbtb_gref_mf_sol2_12', 'tbtb_gref_mf_sol3_12', 'trpu_gref_mf_sol2_12', 'trpu_gref_mf_sol3_12', 'trpu_gref_mf_sol4_12',
              'tubb_gref_mf_sol0_12', 'tubb_gref_mf_sol1_12', 'vcl_gref_a_mf_sol3_12', 'vcl_gref_a_mf_sol4_12', 'vcl_gref_c_mf_sol1_12', 'vcl_gref_c_mf_sol2_12',
              'vcl_gref_d_mf_sol2_12', 'vcl_gref_d_mf_sol3_12', 'vcl_gref_g_mf_sol1_12', 'vcl_gref_g_mf_sol2_12', 'vln_gref_a_mf_sol4_12', 'vln_gref_a_mf_sol5_12',
              'vln_gref_d_mf_sol3_12', 'vln_gref_d_mf_sol4_12', 'vln_gref_e_mf_sol4_12', 'vln_gref_e_mf_sol5_12', 'vln_gref_g_mf_sol2_12', 'vln_gref_g_mf_sol3_12']

effectiveduration = [
    4.387641906738281, 5.603061199188232, 4.958072662353516, 4.873854637145996, 5.011768817901611,
    5.428662300109863, 4.802018165588379, 5.976304054260254, 4.23231315612793, 6.312222003936768,
    6.448185920715332, 6.129138469696045, 5.144126892089844, 4.703968048095703, 4.427346706390381,
    4.357573509216309, 4.137165546417236, 7.379614353179932, 7.018526077270508, 6.856621265411377,
    6.759455680847168, 7.6737189292907715, 7.597165584564209, 7.634331226348877, 1.7018593549728394,
    1.7839909791946411, 1.8504761457443237, 1.6975964307785034, 1.9583446979522705, 1.6292062997817993,
    1.6968934535980225, 1.6543763875961304, 1.9968934059143066, 1.7616779804229736, 2.2377777099609375,
    2.5442631244659424, 1.841927409172058, 2.207573652267456, 1.57315194606781, 1.54464852809906,
    1.493945598602295, 2.2235147953033447, 1.277301549911499, 1.2943763732910156, 0.28999999165534973,
    0.8249433040618896, 0.9801813960075378, 0.20047618448734283, 1.1573243141174316, 1.628866195678711,
    0.4066893458366394, 0.9795238375663757, 1.5392743349075317, 0.3496145009994507, 0.3321315050125122,
    1.4215645790100098, 2.9527437686920166, 1.4076417684555054, 0.10337868332862854, 0.27659863233566284,
    0.8858050107955933, 1.7231972217559814, 0.6079818606376648, 0.3064625859260559, 8.340770721435547,
    8.335556030273438, 9.440340042114258, 5.947845935821533, 6.316190242767334, 6.255260944366455,
    7.16145133972168, 6.171065807342529, 6.683084011077881, 3.682539701461792, 4.033650875091553, 7.71113395690918,
    7.176576137542725, 6.552312850952148, 7.174807071685791, 6.957868576049805, 5.254603385925293,
    7.271111011505127, 7.463787078857422, 7.553083896636963, 5.82190465927124, 7.344308376312256,
    6.717891216278076, 6.960838794708252, 7.800045490264893, 7.463787078857422, 6.588095188140869
]

duration = {}
duration_l = []

for fname in final_list:
    filename = fname+'.wav'
    with contextlib.closing(wave.open(filename,'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration[fname] = frames / float(rate)
        duration_l.append(frames / float(rate))

counter = 0
csv_file = "duration.csv"
with open(csv_file, 'w') as f:
    for i in final_list:
        my_char = "not sustained"
        # print(duration[i])
        # print(effectiveduration[counter])
        # break
        if (duration[i]*0.60 < effectiveduration[counter]) :
            my_char = "sustained"

        value = i+ ', ' + str(duration[i])+ ', ' + str(effectiveduration[counter]) + ', ' + my_char + '\n'
        f.write(value)
        counter += 1

dur = statistics.mean(duration_l)
eff = statistics.mean(effectiveduration)
print("mean of duration: ", dur)
print("mean of effective duration: ", eff)
print("eff/dur = ", 100*eff/dur)
# print(len(effectiveduration))
# print(len(final_list))