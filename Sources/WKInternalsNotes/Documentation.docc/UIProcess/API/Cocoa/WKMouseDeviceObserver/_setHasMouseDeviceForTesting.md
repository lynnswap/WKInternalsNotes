# ``WKInternalsNotes/WKMouseDeviceObserver/_setHasMouseDeviceForTesting(_:)``

テスト用に接続状態を強制設定する。

## Objective-C Declaration
```objective-c
- (void)_setHasMouseDeviceForTesting:(BOOL)hasMouseDevice;
```

## Discussion
Swift 実装の `_setHasMouseDevice(forTesting:)` が `connectedDeviceCount` を 1/0 に切り替える。

## References
- [WKMouseDeviceObserver.h#L43](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKMouseDeviceObserver.h#L43)
- [WKMouseDeviceObserver.swift#L110](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/WKMouseDeviceObserver.swift#L110)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
