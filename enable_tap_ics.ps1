# enable_ics.ps1
$netshare = New-Object -ComObject HNetCfg.HNetShare

$publicAdapter = $null
$privateAdapter = $null

foreach ($conn in $netshare.EnumEveryConnection()) {
    $props = $netshare.NetConnectionProps($conn)

    if ($props.Name -eq "TAP0") {
        $privateAdapter = $conn
        continue
    }

    $config = $netshare.INetSharingConfigurationForINetConnection($conn)
    $deviceType = $props.DeviceName
    $status = $props.Status
    if (($status -eq 2) -and ($deviceType -match "Ethernet|Wi-Fi")) {
        $publicAdapter = $conn
    }
}

$netshare.INetSharingConfigurationForINetConnection($publicAdapter).EnableSharing(0)
$netshare.INetSharingConfigurationForINetConnection($privateAdapter).EnableSharing(1)
