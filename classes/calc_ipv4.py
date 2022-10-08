import re


class CalcIpv4:
    def __init__(self, ip, mascara=None, prefixo=None):
        self.ip = ip
        self.mascara = mascara
        self.prefixo = prefixo

        if mascara is not None and prefixo is not None:
            print('A máscara e o prefixo não podem ser usadas ao mesmo tempo.')
            return

        self._set_broadcast()
        self._set_rede()

    @property
    def ip(self):
        return self._ip

    @ip.setter
    def ip(self, v):
        if not self._valida_ip(v):
            raise ValueError('Ip inválido.')

        self._ip = v
        self._ip_bin = self._ip_to_bin(v)

    @property
    def mascara(self):
        return self._mascara

    @mascara.setter
    def mascara(self, v):
        if not v:
            return
        if not self._valida_ip(v):
            raise ValueError('Máscara inválida.')

        self._mascara = v
        self._mascara_bin = self._ip_to_bin(v)  # 1 ao 0

        if not hasattr(self, 'prefixo'):
            self.prefixo = self._mascara_bin.count('1')

    @property
    def prefixo(self):
        return self._prefixo

    @prefixo.setter
    def prefixo(self, v):
        if not v:
            return

        if not isinstance(v, int):
            raise TypeError('Prefixo precisa ser um número inteiro.')

        if v > 32 or v < 0:
            raise ValueError('Prefixo precisa ter 32 bits.')

        self._prefixo = v
        self._mascara_bin = (v * '1').ljust(32, '0')

        if not hasattr(self, 'mascara'):
            self.mascara = self._bin_to_ip(self._mascara_bin)

    @property
    def rede(self):
        return self._rede

    @property
    def broadcast(self):
        return self._broadcast

    @property
    def numero_ips(self):
        return self._get_numeros_ips()

    @staticmethod
    def _valida_ip(ip):
        regexp = re.compile(
            r'^([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3})$'
        )

        if regexp.search(ip):
            return True

    @staticmethod
    def _ip_to_bin(ip):
        blocos = ip.split('.')
        blocos_binarios = [
            format(int(x), '08b') for x in blocos  # ou bin(int(x))[2:].zfill(8)
        ]
        return ''.join(blocos_binarios)

    @staticmethod
    def _bin_to_ip(ip):
        n = 8
        blocos = [
            int(ip[i:n + i], 2) for i in range(0, 32, n)
            # fatiando a cada 8 numeros e convertendo para inteiro
        ]
        ip_decimal = [str(x) for x in blocos]  # convertendo para string para poder usar o join
        return '.'.join(ip_decimal)

    def _set_broadcast(self):
        # host =
        host_bits = 32 - self.prefixo
        self._broadcast_bin = self._ip_bin[:self.prefixo] + (host_bits * '1')
        self._broadcast = self._bin_to_ip(self._broadcast_bin)

        return self._broadcast

    def _set_rede(self):
        host_bits = 32 - self.prefixo
        self._rede_bin = self._ip_bin[:self.prefixo] + (host_bits * '0')
        self._rede = self._bin_to_ip(self._rede_bin)

        return self._rede

    def _get_numeros_ips(self):
        return 2 ** (32 - self.prefixo) - 2
