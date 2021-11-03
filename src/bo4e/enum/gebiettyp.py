# pylint:disable=missing-module-docstring

from bo4e.enum.strenum import StrEnum


class Gebiettyp(StrEnum):
    """
    List of possible Gebiettypen.
    """

    REGELZONE = "REGELZONE"
    MARKTGEBIET = "MARKTGEBIET"
    BILANZIERUNGSGEBIET = "BILANZIERUNGSGEBIET"
    VERTEILNETZ = "VERTEILNETZ"
    TRANSPORTNETZ = "TRANSPORTNETZ"
    REGIONALNETZ = "REGIONALNETZ"
    AREALNETZ = "AREALNETZ"
    GRUNDVERSORGUNGSGEBIET = "GRUNDVERSORGUNGSGEBIET"
    VERSORGUNGSGEBIET = "VERSORGUNGSGEBIET"
