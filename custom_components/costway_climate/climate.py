import tinytuya
from homeassistant.components.climate import ClimateEntity
from homeassistant.components.climate.const import (
    HVAC_MODE_OFF,
    HVAC_MODE_HEAT,
    HVAC_MODE_COOL,
    SUPPORT_FAN_MODE,
    SUPPORT_TARGET_TEMPERATURE,
)
from homeassistant.const import TEMP_CELSIUS
from .const import DOMAIN, CONF_DEVICE_ID, CONF_LOCAL_KEY, CONF_IP, DEFAULT_NAME

SUPPORT_FLAGS = SUPPORT_FAN_MODE | SUPPORT_TARGET_TEMPERATURE

FAN_MODES = ["low", "medium", "high"]

class CostwayClimate(ClimateEntity):
    def __init__(self, device_id, local_key, ip):
        self._device_id = device_id
        self._local_key = local_key
        self._ip = ip
        self._name = DEFAULT_NAME
        self._hvac_mode = HVAC_MODE_OFF
        self._target_temp = 22
        self._fan_mode = FAN_MODES[0]

        self._device = tinytuya.Device(device_id, ip, local_key)
        self._device.set_version(3.3)

    @property
    def name(self):
        return self._name

    @property
    def supported_features(self):
        return SUPPORT_FLAGS

    @property
    def temperature_unit(self):
        return TEMP_CELSIUS

    @property
    def target_temperature(self):
        return self._target_temp

    @property
    def hvac_mode(self):
        return self._hvac_mode

    @property
    def hvac_modes(self):
        return [HVAC_MODE_OFF, HVAC_MODE_HEAT, HVAC_MODE_COOL]

    @property
    def fan_mode(self):
        return self._fan_mode

    @property
    def fan_modes(self):
        return FAN_MODES

    def set_temperature(self, **kwargs):
        temp = kwargs.get("temperature")
        if temp:
            self._target_temp = temp
            self._device.set_dps(temp, "2")

    def set_hvac_mode(self, hvac_mode):
        self._hvac_mode = hvac_mode
        if hvac_mode == HVAC_MODE_OFF:
            self._device.set_dps(False, "1")
        elif hvac_mode == HVAC_MODE_HEAT:
            self._device.set_dps(True, "1")
            self._device.set_dps("heat", "4")
        elif hvac_mode == HVAC_MODE_COOL:
            self._device.set_dps(True, "1")
            self._device.set_dps("cool", "4")

    def set_fan_mode(self, fan_mode):
        self._fan_mode = fan_mode
        self._device.set_dps(fan_mode, "3")

    def update(self):
        data = self._device.status()
        dps = data.get("dps", {})
        self._target_temp = dps.get("2", self._target_temp)
        mode = dps.get("4", "off")
        if not dps.get("1"):
            self._hvac_mode = HVAC_MODE_OFF
        elif mode == "heat":
            self._hvac_mode = HVAC_MODE_HEAT
        elif mode == "cool":
            self._hvac_mode = HVAC_MODE_COOL
        self._fan_mode = dps.get("3", self._fan_mode)
