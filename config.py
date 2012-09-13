_prefix = '/home/vchahune/data/global_voices/baseline'
sa_config = _prefix+'/sa-mg-en.ini'

# Translation server
tserver_port = 9000
tserver_host = '127.0.0.1'
cdec_config = open(_prefix+'/cdec-mg-en.ini').read()
cdec_weights = _prefix+'/weights-mg-en.ini'
