from rsa import Rsa


def main():
    print('>>===== RSA暗号 =====<<')
    rsa = Rsa()
    e, n = rsa.get_enc_key()
    d, n1 = rsa.get_dec_key()
    print('==== 暗号化鍵 ====')
    print(F'e : {e}\n' + F'n : {n}\n')
    print('==== 複合化鍵 ====')
    print(F'd : {d}\n')
    while True:
        mode = input('動作モードを選択してください (1: 暗号化, 2: 複合化, 3: 終了) >> ')
        try:
            if mode == '1':
                text = input('平文 >> ')
                result = data_transaction(text, e, n)
                print(F'暗号文 : {result}')
            elif mode == '2':
                text = input('暗号文 >> ')
                result = data_transaction(text, d, n)
                print(F'平文 : {result}')
            elif mode == '3':
                break
            else:
                print('入力値が正しくありません')
        except ValueError:
            print('入力値が正しくありません')


def convert_to_dec(data: list, n: int) -> int:
    length = len(data)
    result = 0
    for i in range(1, length+1):
        result += data[-i] * pow(n, i-1)
    return result


def convert_to_n(data: int, n: int) -> list:
    digit = 0
    for i in range(pow(10, 9)):
        if data < pow(n, i):
            digit += i
            break
    result = [0]*digit
    offset = 0
    for i in range(1, digit+1):
        target = data // pow(n, digit-i)
        result[offset] = target
        offset += 1
        data -= target * pow(n, digit-i)
    return result


def data_transaction(data: str, key: int, n: int) -> str:
    input_to_int = []
    for char in data:
        asc = ord(char)
        if 31 < asc & asc < 128:
            input_to_int.append(asc-32)
        else:
            raise ValueError
    c = pow(convert_to_dec(input_to_int, 95), key, n)
    output_int = convert_to_n(c, 95)
    result = ''.join(chr(i+32) for i in output_int)
    return result


if __name__ == '__main__':
    main()