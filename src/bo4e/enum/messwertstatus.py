# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class Messwertstatus(StrEnum):
    """
    Der Status eines Zählerstandes
    """

    ABGELESEN = "ABGELESEN"  #: ABGELESEN
    ERSATZWERT = "ERSATZWERT"  #: ERSATZWERT
    VORSCHLAGSWERT = "VORSCHLAGSWERT"  #: VORSCHLAGSWERT
    NICHT_VERWENDBAR = "NICHT_VERWENDBAR"  #: NICHT_VERWENDBAR
    PROGNOSEWERT = "PROGNOSEWERT"  #: PROGNOSEWERT
    VORLAEUFIGERWERT = "VORLAEUFIGERWERT"  #: VORLAEUFIGERWERT
    ENERGIEMENGESUMMIERT = "ENERGIEMENGESUMMIERT"  #: ENERGIEMENGESUMMIERT
    FEHLT = "FEHLT"  #: FEHLT