WLDCDriver
============
Driver to make requests to weatherlink.com, both for archive and for loop data.

Designed to work with both Python 2.7 and Python 3

## Installation


- Download the latest release of wldc : https://github.com/richardjarvis/weatherlinkdotcom-driver-weewx/releases
- Install the driver : ```wee_extension --install wldc.zip```
- Install require libs Python : ```pip install requests```
- Find on **weewx.conf** ```station_type``` and change by this : ```station_type = wldc```
- If you want to retrieve new data when the driver fail, set ```loop_on_init = True``` on **weewx.conf**
- Restart weewx : ```service weewx restart```

### Accumulator for rainRate

When install the driver, a parameter is write to the **weewx.conf** :
```
[Accumulator]
      [[rainRate]]
        extractor = max
```

**Not delete this** because this allow the driver
to set the correct rainRate max each archive interval of Weewx.

## Configuration on Weewx

After installing driver, a new stanza appear at the end of the file **weewx.conf**.

The correct syntax for set a parameter is : ```blabla = 1```

### Default setting needed to run the driver

- ```max_tries``` - Max tries before Weewx raise an exception and finished the loop.<br />
- ```retry_wait``` - Time to retry in second between each.<br />
- ```poll_interval``` - Time to sleep in second between 2 requests.<br/>
- ```realtime_enable``` - Enable realtime each 3 secondes for Wind and Rain.<br />
- ```hostname``` - Set your IP or hostname of WLL module.<br />
- ```time_out``` - Set this for timeout in second of HTTP and realtime request.<br />
- ```device_id``` - Set the ID of your ISS that you've configured on the WLL Module.<br />
- ```wl_archive_enable``` - Enable retrieve data from Weatherlink.com.<br />

NB : For the driver work good, set ```retry_wait = 2 x poll_interval```. In this case, the driver do not sent a lot of requests.<br/>
To calculate the time after the driver raise en exception and stop Weewx, do ```max_tries x retry_wait```

### Realtime for wind and rain

**/!\ Realtime not work if Weewx is out of your lan network.**

With the WLLDriver, you can enable realtime to retrieve data from wind and rain sensors each 2.5s.<br/>
If you have enabled ```realtime_enable = 1```, please note that all others sensors would be reach each ```poll_interval```<br />
So, make sur that ```poll_interval``` has a number wich is more than 2 * 2.5s. For better use, set ```poll_interval = 10```<br/>
The temperature or barometer for example does not vary greatly.<br/>

### Retrieve data from Weatherlink.com

If you want to use weatherlink.com to retrieve lost data when Weewx crash for example, <br/>you have to create an API Key :

- Create your API Key v2 on https://www.weatherlink.com/account
- Use this tool to know your station ID : https://repl.it/repls/MeaslyExternalMegabyte#main.php by change ```api-key``` and ```api-secret``` and run the script.

Enable the feature ```wl_archive_enable = 1``` and set parameters on **weewx.conf** in [WLLDriver] :

- ```wl_apikey``` - Create an API Key on your Weatherlink account.
- ```wl_apisecret``` - By creating API Key, you've also need an API Secret.
- ```wl_stationid``` - Check your station ID by using the method explain before.
- ```wl_archive_interval``` - Be careful when settings this because it depending on your subscription on Weatherlink.com. For better use, please set the same archive interval than the Weewx engine.

### Wind gust 2min

**/!\ Not supported if realtime is enabled.**

Weatherlink Live module can calculate wind gust each 2min instead of 10min by default. <br/>
To enable this, set this parameter on [WLLDriver] : ```wind_gust_2min_enable = 1```

### Change HTTP port

You can change the default port 80 to set a new port to request to the WLL module. To change to 8080 for example, set this parameter on [WLLDriver] : ```port = 8080```

### Health status of ISS & WLL

**/!\ If you disable ```wl_archive_enable = 0```, you will not have the health status.**

WLLDriver recuperate value for health ISS and WLL module each 15 minutes on Weatherlink.com :

| Parameter        | Type |
| ------|-----|
| **txBatteryStatus** | Transmitter battery |
| **rxCheckPercent** | Signal quality |
| **consBatteryVoltage** | Battery in volt of the WLL module |
| **supplyVoltage** | Supply voltage of the WLL module |

## Default value for each parameter

| Parameter        | Default value      | Min/Max |
| ------|-----|-----|
| **max_tries** | 10 | 0/200 |
| **retry_wait** | 10 | 0/600	|
| **poll_interval** 	| 5 | 0/600 |
| **realtime_enable** | 0 | 0 = Disable / 1 = Enable |
| **time_out** | 10 | 0/15 |
| **wl_archive_enable** | 0 | 0 = Disable / 1 = Enable |
| **device_id** | iss:1 | Please refer to the chapter extraSensor |
| **wl_archive_interval** | User need to set manually | 1, 5 or 15 |
| **wind_gust_2min_enable** | Not set so, 0 | 0 = Disable / 1 = Enable |
| **port** | 80 | 1/65535 |

## Credits

The starting point for this was a fork of Drealine/weatherlinklive-driver-weewx. Many thanks.


