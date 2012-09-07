import logging
import zmq
import cdec, cdec.scfg
import config

logger = logging.getLogger()

def translation_server(translator, host, port):
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://%s:%d" % (host, port))
    logger.info('Translation server ready')
    try:
        while True:
            sentence = socket.recv().decode('utf8')
            logger.info('I[%s]', sentence)
            translation = translator(sentence) if sentence else ''
            logger.info('O[%s]', translation)
            socket.send(translation.encode('utf8'))
    except KeyboardInterrupt:
        logger.info('Interrupted')

def translator():
    extractor = cdec.scfg.GrammarExtractor(config.__dict__)
    decoder = cdec.Decoder(config.cdec_config)
    decoder.read_weights(config.cdec_weights)

    def translate(sentence):
        grammar = extractor.grammar(sentence)
        forest = decoder.translate(sentence, grammar=grammar)
        return forest.viterbi()
    
    return translate

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format=' * %(message)s')
    translation_server(translator(), config.tserver_host, config.tserver_port)
