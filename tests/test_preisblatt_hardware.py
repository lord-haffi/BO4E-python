import pytest  # type:ignore[import]

from bo4e.bo.preisblatthardware import PreisblattHardware, PreisblattHardwareSchema
from bo4e.enum.bilanzierungsmethode import Bilanzierungsmethode
from bo4e.enum.dienstleistungstyp import Dienstleistungstyp
from bo4e.enum.netzebene import Netzebene
from bo4e.enum.preisstatus import Preisstatus
from bo4e.enum.sparte import Sparte
from tests.serialization_helper import assert_serialization_roundtrip  # type:ignore[import]
from tests.test_geraeteeigenschaften import example_geraeteeigenschaften  # type:ignore[import]
from tests.test_marktteilnehmer import example_marktteilnehmer  # type:ignore[import]
from tests.test_preisposition import example_preisposition  # type:ignore[import]
from tests.test_zeitraum import example_zeitraum  # type:ignore[import]


class TestPreisblattHardware:
    @pytest.mark.parametrize(
        "preisblatt_hardware",
        [
            pytest.param(
                PreisblattHardware(
                    bezeichnung="foo",
                    sparte=Sparte.STROM,
                    preisstatus=Preisstatus.ENDGUELTIG,
                    preispositionen=[example_preisposition],
                    gueltigkeit=example_zeitraum,
                    herausgeber=example_marktteilnehmer,
                    bilanzierungsmethode=Bilanzierungsmethode.TLP_GEMEINSAM,
                    messebene=Netzebene.MSP,
                    inklusive_dienstleistungen=[Dienstleistungstyp.AUSLESUNG_FERNAUSLESUNG_ZUSAETZLICH_MSB],
                    basisgeraet=example_geraeteeigenschaften,
                    inklusive_geraete=[example_geraeteeigenschaften],
                )
            ),
        ],
    )
    def test_serialization_roundtrip(self, preisblatt_hardware: PreisblattHardware):
        """
        Test de-/serialisation
        """
        assert_serialization_roundtrip(preisblatt_hardware, PreisblattHardwareSchema())

    def test_missing_required_attribute(self):
        with pytest.raises(TypeError) as excinfo:
            _ = PreisblattHardware()
        assert "missing 8 required" in str(excinfo.value)  # 5 from preisblatt + 3 from preisblatt hardware
