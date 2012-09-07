_prefix = '/home/vchahune/data/global_voices/baseline'
# Grammar extractor
max_len = 5
max_nt = 2
max_size = 15
min_gap = 1
rank1 = 100
rank2 = 10
bitext = _prefix+'/sa-mg-en/bitext/bitext'
f_sa_file = bitext+'/f.sa.bin'
e_file = bitext+'/e.bin'
a_file = bitext+'/a/gdfa/a.bin'
lex_file = bitext+'/a/gdfa/lex.bin'
precompute_file = bitext+'/precomp.%d.%d.%d.%d.%d.%d.bin' % (max_len, max_nt, max_size, min_gap, rank1, rank2)

# Translation server
tserver_port = 9000
tserver_host = '127.0.0.1'
cdec_config = open(_prefix+'/cdec-mg-en.ini').read()
cdec_weights = _prefix+'/weights-mg-en.ini'
