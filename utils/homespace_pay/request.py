from requests import Session
from webcrypt.jwe import JWE
import json


class HomespacePaySession(Session):
    def __init__(self, user):
        super().__init__()
        self.user = user

    def request(self, method, url, *args, **kwargs):
        payload = {
            "referenceAccountId": str(self.user.current_condominium.id)
        }
        json_payload = json.dumps(payload)
        jwk = JWE(algorithm=JWE.Algorithm.PBES2_HS512_A256KW,
                  key="Secret")

        cookie = jwk.encrypt(bytes(json_payload, "utf-8"))
        headers = kwargs.pop("headers", {})
        headers["token"] = cookie
        return super().request(method, url, *args, headers=headers, **kwargs)
