import base64

MESSAGE = '''
EUYFHAYRSx4cSVRVTk0GBAwEBglBT0kXAAIGBBcOEBcJTVVOUwodHgQTBAAWCUFPSREJCAUTAhpC
UhRNSAcaDBwPBR8LCRcJQU9JFQwGAwQADAgXQBlITk5PSR8PGgYGGUsJSEJUSBwLAxQAEQEJTVVO
UxwPDARRRUVVSAIASVRVTk0WHwdEVVM=
'''

KEY = 'javier.monton'

result = []
for i, c in enumerate(base64.b64decode(MESSAGE)):
    result.append(chr(ord(c) ^ ord(KEY[i % len(KEY)])))

print(''.join(result))