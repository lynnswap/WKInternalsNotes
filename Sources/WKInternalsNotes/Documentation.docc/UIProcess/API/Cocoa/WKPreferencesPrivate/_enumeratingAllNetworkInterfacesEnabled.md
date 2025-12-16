# ``WKInternalsNotes/WKPreferencesPrivate/_enumeratingAllNetworkInterfacesEnabled``

Enumerating All Network Interfaces を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setEnumeratingAllNetworkInterfacesEnabled:) BOOL _enumeratingAllNetworkInterfacesEnabled WK_API_AVAILABLE(macos(10.13), ios(11.0));
```

## Default Value
iOS: `NO` / macOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_enumeratingAllNetworkInterfacesEnabled = YES`: Enumerating All Network Interfaces を有効化する。
- `_enumeratingAllNetworkInterfacesEnabled = NO`: Enumerating All Network Interfaces を無効化する。
- Implementation: [`Source/WebKit/UIProcess/WebPageProxy.cpp#L12069`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/WebPageProxy.cpp#L12069) の `WebProcessPool::urlSchemesWithCustomProtocolHandlers` が `enumeratingAllNetworkInterfacesEnabled()` を参照する。

## Details
- WebPreferences key: `EnumeratingAllNetworkInterfacesEnabled`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L122`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L122)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L750`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L750)
- [`Source/WebKit/UIProcess/WebPageProxy.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/WebPageProxy.cpp)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L2688`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L2688) (key: `EnumeratingAllNetworkInterfacesEnabled`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
