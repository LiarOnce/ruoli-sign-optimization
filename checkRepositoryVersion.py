import hashlib
import os


class VersionInfo:
    codeVersion = "V-T3.8.4b"
    # 代码文件列表
    codeList = ("todayLoginService.py", "actions/autoSign.py", "actions/collection.py", "actions/sleepCheck.py", "actions/workLog.py",
                "actions/sendMessage.py", "actions/teacherSign.py", "login/Utils.py", "login/casLogin.py", "login/iapLogin.py", "login/RSALogin.py", "index.py", 'liteTools.py')
    # 代码文件哈希列表
    codeStandardHashDict = {'todayLoginService.py': '39acd0282ce498b85d33423ac9971b061fa1e5b9b567b33eafa2af7ee0bc6800', 'actions/autoSign.py': 'f34d66bd61c6faebe77398674ebf746158ea304c99908140d2cf92c987c1b5b6', 'actions/collection.py': '95cd60c60814ac3165c42c7d91771745ff69b8e97da3042d7564483fb88cf605', 'actions/sleepCheck.py': '4f97c11b4b4b92ab780e0e71f98c6844a865015968dc8c30e0f2954bf6557056', 'actions/workLog.py': '935afc4ed491cddf47d76e2b75c9ffaf9d91e8d19ec156e97870a367a621e39e', 'actions/sendMessage.py': '0292530e61381610d6babb18ddd68727f4f4683a82beeabb42245032f321886b',
                            'actions/teacherSign.py': '241322f04defe072357c26ae36c033ddfc3f70fe622bbdb6f245027bdd89e443', 'login/Utils.py': 'd5da76b333cf204515a4b6e76903fd7ddd7f7039e7fd135ba0b40475f5aa16f3', 'login/casLogin.py': '4c164cda7592382061bacfcace2168e34bfb7ae4b024a53387a72a6b8ef0f0b4', 'login/iapLogin.py': 'ed2775a15dc628b8c0c01429d7a2f84ee3fef56f0623b4118b51d733081b6b40', 'login/RSALogin.py': '9ec9bb985b95564ab00216df14ab892ce2f262e08a216538f60ca293f1a12c12', 'index.py': '5c3e178bac8f1cab8eb276d30b3f26ff700db615865b8d04a968d2b39d770fab', 'liteTools.py': '5e19d384cc4f608e8734cb0099c0d09a183614314641972b867a509625f409e2'}


class HSF:
    """Hashing String And File"""
    @staticmethod
    def geneHashObj(hash_type):
        if hash_type == 1:
            return hashlib.sha1()
        elif hash_type == 224:
            return hashlib.sha224()
        elif hash_type == 256:
            return hashlib.sha256()
        elif hash_type == 384:
            return hashlib.sha384()
        elif hash_type == 512:
            return hashlib.sha512()
        elif hash_type == 5:
            return hashlib.md5()
        elif hash_type == 3.224:
            return hashlib.sha3_224()
        elif hash_type == 3.256:
            return hashlib.sha3_256()
        elif hash_type == 3.384:
            return hashlib.sha3_384()
        elif hash_type == 3.512:
            return hashlib.sha3_512()
        else:
            raise Exception('类型错误, 初始化失败')

    @staticmethod
    def fileHash(path, hash_type):
        """计算文件哈希
        :param path: 文件路径
        :param hash_type: 哈希算法类型
            1       sha-1
            224     sha-224
            256      sha-256
            384     sha-384
            512     sha-512
            5       md5
            3.256   sha3-256
            3.384   sha3-384
            3.512   sha3-512
        """
        hashObj = HSF.geneHashObj(hash_type)
        if os.path.isfile(path):
            try:
                with open(path, "rb") as f:
                    for byte_block in iter(lambda: f.read(1048576), b""):
                        hashObj.update(byte_block)
                    return hashObj.hexdigest()
            except Exception as e:
                raise Exception('%s计算哈希出错: %s' % (path, e))
        else:
            raise Exception('路径错误, 没有指向文件: "%s"')

    @staticmethod
    def strHash(str_: str, hash_type, charset='utf-8'):
        """计算字符串哈希
        :param str_: 字符串
        :param hash_type: 哈希算法类型
        :param charset: 字符编码类型
            1       sha-1
            224     sha-224
            256      sha-256
            384     sha-384
            512     sha-512
            5       md5
            3.256   sha3-256
            3.384   sha3-384
            3.512   sha3-512
        """
        hashObj = HSF.geneHashObj(hash_type)
        bstr = str_.encode(charset)
        hashObj.update(bstr)
        return hashObj.hexdigest()


def checkCodeVersion(outputCodeHash=False):
    '''检查代码文件哈希是否与预设的哈希一致'''
    codeHash = {}
    # 计算代码文件哈希
    for i in VersionInfo.codeList:
        codeHash[i] = HSF.fileHash(i, 256)
    if codeHash == VersionInfo.codeStandardHashDict:
        VersionNumber = VersionInfo.codeVersion
    else:
        VersionNumber = VersionInfo.codeVersion+'-?'
    if outputCodeHash:
        print(VersionNumber)
        print(codeHash)
    return VersionNumber


if __name__ == '__main__':
    checkCodeVersion(True)
