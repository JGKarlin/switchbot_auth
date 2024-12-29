import time
import uuid
import hmac
import hashlib
import base64
from datetime import timedelta

from homeassistant.components.sensor import SensorEntity
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType
from homeassistant.helpers.event import async_track_time_interval

SCAN_INTERVAL = timedelta(seconds=55)  # Refresh before 60-second timeout


class SwitchBotAuthSensor(SensorEntity):
    """Representation of a SwitchBot Auth Sensor."""

    def __init__(self, hass: HomeAssistant, token: str, secret: str):
        """Initialize the sensor."""
        self._hass = hass
        self._token = token.strip()
        self._secret = secret.strip()
        self._state = None
        self._attrs = {}
        self._attr_name = "switchbot_auth"
        self._attr_unique_id = "switchbot_auth"

    async def async_added_to_hass(self):
        """Handle added to Hass."""
        self._update_auth()
        # Update every SCAN_INTERVAL
        self.async_on_remove(
            async_track_time_interval(
                self._hass, lambda _: self._update_auth(), SCAN_INTERVAL
            )
        )

    def _update_auth(self):
        """Update authentication parameters."""
        # Generate timestamp (13 digits)
        t = str(int(round(time.time() * 1000)))
        
        # Generate random UUID
        nonce = str(uuid.uuid4())
        
        # Create the string to sign: token + t + nonce
        string_to_sign = f'{self._token}{t}{nonce}'
        
        # Calculate signature using HMAC-SHA256
        sign = base64.b64encode(
            hmac.new(
                self._secret.encode('utf-8'),  # Use secret as key
                msg=string_to_sign.encode('utf-8'),
                digestmod=hashlib.sha256
            ).digest()
        ).decode('utf-8')

        # Set state and attributes with explicit string conversion
        self._state = "valid"
        self._attrs = {
            "authorization": str(self._token),  # Ensure string type
            "t": str(t),                        # Timestamp as plain string
            "nonce": str(nonce),                # Random UUID as plain string
            "sign": str(sign)                   # Calculated signature as plain string
        }
        self.async_write_ha_state()

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def extra_state_attributes(self):
        """Return the state attributes."""
        return self._attrs


async def async_setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    async_add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None,
) -> None:
    """Set up the sensor platform."""
    token = config.get("token")
    secret = config.get("secret")
    
    if not token or not secret:
        raise ValueError("Both token and secret must be provided in configuration")

    async_add_entities([SwitchBotAuthSensor(hass, token, secret)])
